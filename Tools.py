import os
import streamlit as st
from openai import OpenAI
from dotenv import load_dotenv
from langchain.agents import initialize_agent, Tool
from langchain_openai import ChatOpenAI
from langchain.agents.agent_types import AgentType
from langchain.callbacks import StreamlitCallbackHandler
import requests
from bs4 import BeautifulSoup
import re
from product_analysis_prompt import get_product_analysis_tool, get_product_analysis_prompt

# Set page config
st.set_page_config(
    page_title="Web Content Analyzer",
    page_icon="🔍",
    layout="wide"
)

# Add custom CSS
st.markdown("""
    <style>
    .main {
        padding: 2rem;
    }
    .stTextInput>div>div>input {
        font-size: 1.2rem;
    }
    </style>
""", unsafe_allow_html=True)

# Load environment variables
load_dotenv()

# Initialize OpenAI client
client = OpenAI(
    api_key=os.getenv("OPENAI_API_KEY"),
    base_url="https://api.openai.com/v1"
)

# Initialize LLM
llm = ChatOpenAI(
    temperature=0.3,
    openai_api_key=os.getenv("OPENAI_API_KEY")
)

def clean_text(text):
    """Clean and format the extracted text"""
    # Remove extra whitespace
    text = re.sub(r'\s+', ' ', text)
    # Remove special characters
    text = re.sub(r'[^\w\s.,!?-]', '', text)
    return text.strip()

def get_web_text(url: str):
    """
    Extract text directly from a webpage
    
    Args:
        url (str): URL of the webpage to analyze
    Returns:
        str: Extracted and cleaned text from the webpage
    """
    try:
        # Add headers to mimic a browser request
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
        }
        
        # Get the webpage content
        response = requests.get(url, headers=headers, timeout=10)
        response.raise_for_status()  # Raise an exception for bad status codes
        
        # Parse the HTML content
        soup = BeautifulSoup(response.text, 'html.parser')
        
        # Remove script and style elements
        for script in soup(["script", "style", "nav", "footer", "header"]):
            script.decompose()
        
        # Get text content
        text = soup.get_text()
        
        # Clean the text
        cleaned_text = clean_text(text)
        
        if not cleaned_text:
            raise ValueError("No text content found on the webpage")
            
        return cleaned_text
        
    except requests.RequestException as e:
        st.error(f"Error accessing the webpage: {str(e)}")
        return None
    except Exception as e:
        st.error(f"Error processing the webpage: {str(e)}")
        return None

#analyze the text based on prompt
def analyze_text(text: str, is_product_analysis: bool = False):
    """
    Analyze text with optional product analysis prompt
    
    Args:
        text (str): Text to analyze
        is_product_analysis (bool): Whether to use product analysis prompt
    """
    if not text:
        return "No text to analyze."
        
    if is_product_analysis:
        prompt = get_product_analysis_prompt(text)
        messages = [{"role": "user", "content": prompt}]
    else:
        messages = [{"role": "user", "content": f"Analyze the following text: {text}"}]
    
    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=messages
    )
    return response.choices[0].message.content
                   
tools = [
    Tool(
        name="GetWebText",
        func=get_web_text,
        description="Use this tool when user wants to get a text from a url"
    ),
    Tool(
        name="AnalyzeText",
        func=analyze_text,
        description="Use this tool when user wants to analyze a text"
    )
]

# Initialize Agent (zero-shot type)
agent = initialize_agent(
    tools=tools,
    llm=llm,
    agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION,
    verbose=True,
    handle_parsing_errors=True  # Add error handling
)

# Main UI
def main():
    st.title("Amazon Product Analysis")
    st.markdown("---")
    
    # URL input
    url = st.text_input("Enter the URL to analyze:", placeholder="https://example.com")
    
    # Analysis type selection
    analysis_type = "Product Analysis"  # 直接设置为产品分析
    # Process button
    if st.button("Analyze Content", type="primary"):
        if url:
            with st.spinner("Analyzing content..."):
                try:
                    # Get text from URL
                    text = get_web_text(url)
                    
                    if text:
                        # Show extracted text in expander
                        with st.expander("View Extracted Text"):
                            st.text(text)
                            
                        # Analyze text
                        is_product_analysis = analysis_type == "Product Analysis"
                        analysis_result = analyze_text(text, is_product_analysis)
                        
                        # Display results
                        st.markdown("### Analysis Results")
                        st.markdown("---")
                        st.write(analysis_result)
                    
                except Exception as e:
                    st.error(f"An error occurred: {str(e)}")
        else:
            st.warning("Please enter a URL to analyze.")

if __name__ == "__main__":
    main()