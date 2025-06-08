import os
import streamlit as st
from openai import OpenAI
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Initialize OpenAI client
client = OpenAI(
    api_key=os.getenv("OPENAI_API_KEY"),
    base_url="https://api.openai.com/v1"
)

def check_grammar(text,additional_prompt):
    """
    Check grammar using OpenAI API
    """
    try:
        response = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system",
                  "content": f"You are a professional English grammar checker. Check the following text for grammar errors and provide corrections. Format your response as follows:\n1. List all grammar errors found\n2. Provide the corrected version\n3. Explain the corrections made\n{additional_prompt}  "},
                {"role": "user", "content": text}
            ],
            temperature=0.3
        )
        return response.choices[0].message.content
    except Exception as e:
        return f"Error: {str(e)}"

# Streamlit UI
st.title("English Grammar Checker")
st.write("Enter your text below to check for grammar errors:")

# Text input
text_input = st.text_area("Input Text", height=200)
additional_prompt = st.text_area("Additional Prompt", height=100)
if st.button("Check Grammar"):
    if text_input:
        with st.spinner("Checking grammar..."):
            result = check_grammar(text_input,additional_prompt)
            st.write("### Results:")
            st.write(result)
    else:
        st.warning("Please enter some text to check.") 