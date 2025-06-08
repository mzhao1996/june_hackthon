import os
import streamlit as st
from openai import OpenAI
from dotenv import load_dotenv
from langchain.agents import initialize_agent, Tool
from langchain.chat_models import ChatOpenAI
from langchain.agents.agent_types import AgentType
import random
import string

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

# Define grammar checking function
def check_grammar(text):
    """
    Check grammar using OpenAI API
    """
    try:
        response = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system",
                  "content": f"You are a professional English grammar checker. Check the following text for grammar errors and provide corrections. Format your response as follows:\n1. List all grammar errors found\n2. Provide the corrected version\n3. Explain the corrections made"},
                {"role": "user", "content": text}
            ],
            temperature=0.3
        )
        return response.choices[0].message.content
    except Exception as e:
        return f"Error: {str(e)}"
    
# Define grammar checking tool for agent
def grammar_tool(text: str) -> str:
    return check_grammar(text)

# Define English to Chinese translation function
def translate_to_chinese(text):
    """
    Translate the text to Chinese
    """
    try:
        response = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system",
                  "content": f"You are a professional English to Chinese translator. Translate the following text to Chinese. Format your response as follows:\n1. Provide the translated version\n2. Explain the translation process\n3. Provide the original text and the translated text in a table format"},
                {"role": "user", "content": text}
            ],
            temperature=0.3
        )
        return response.choices[0].message.content
    except Exception as e:
        return f"Error: {str(e)}"
    
# Define English to Chinese translation tool for agent
def translate_to_chinese_tool(text: str) -> str:
    return translate_to_chinese(text)

# Define Chinese to English translation function
def translate_to_english(text):
    """
    Translate the text to English
    """
    try:
        response = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system",
                  "content": f"You are a professional Chinese to English translator. Translate the following text to English. Format your response as follows:\n1. Provide the translated version\n2. Explain the translation process\n3. Provide the original text and the translated text in a table format"},
                {"role": "user", "content": text}
            ],
            temperature=0.3
        )
        return response.choices[0].message.content
    except Exception as e:
        return f"Error: {str(e)}"
    
# Define Chinese to English translation tool for agent
def translate_to_english_tool(text: str) -> str:
    return translate_to_english(text)

# Define text polish function
def polish_text(text):
    """
    Polish the text
    """
    try:
        response = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system",
                  "content": f"You are a professional text polish. Polish the following text. Format your response as follows:\n1. Provide the polished version\n2. Explain the polishing process\n3. Provide the original text and the polished text in a table format"},
                {"role": "user", "content": text}
            ],
            temperature=0.3
        )
        return response.choices[0].message.content
    except Exception as e:
        return f"Error: {str(e)}"
    
# Define text polish tool for agent
def polish_text_tool(text: str) -> str:
    return polish_text(text)

# Define text simplification function
def simplify_text(text):
    """
    Simplify the text
    """
    try:
        response = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system",
                  "content": f"You are a professional text simplifier. Simplify the following text. Format your response as follows:\n1. Provide the simplified version\n2. Explain the simplification process\n3. Provide the original text and the simplified text in a table format"},
                {"role": "user", "content": text}
            ],
            temperature=0.3
        )
        return response.choices[0].message.content
    except Exception as e:
        return f"Error: {str(e)}"
    
# Define text simplification tool for agent
def simplify_text_tool(text: str) -> str:
    return simplify_text(text)

# Define text summarization function
def summarize_text(text):
    """
    Summarize the text
    """
    try:
        response = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system",
                  "content": f"You are a professional text summarizer. Summarize the following text. Format your response as follows:\n1. Provide the summarized version\n2. Explain the summarization process\n3. Provide the original text and the summarized text in a table format"},
                {"role": "user", "content": text}
            ],
            temperature=0.3
        )
        return response.choices[0].message.content
    except Exception as e:
        return f"Error: {str(e)}"
    
# Define text summarization tool for agent
def summarize_text_tool(text: str) -> str:
    return summarize_text(text)

# Define role based writing function
def role_based_writing(text, role):
    """
    Role based writing
    """
    try:
        response = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system",
                  "content": f"You are a professional role based writer. Write the following text in the role of {role}. Format your response as follows:\n1. Provide the written version\n2. Explain the writing process\n3. Provide the original text and the written text in a table format"},
                {"role": "user", "content": text}
            ],
            temperature=0.3
        )
        return response.choices[0].message.content
    except Exception as e:
        return f"Error: {str(e)}"
    
# Define role based writing tool for agent
def role_based_writing_tool(text: str, role: str) -> str:
    return role_based_writing(text, role)

# Define cat foot function
def cat_foot():
    # Define character sets
    letters = string.ascii_letters
    digits = string.digits
    symbols = "!@#$%^&*()_+-=[]{}|;:,.<>?"

    # Combine all characters
    all_chars = letters + digits + symbols

    # Generate random string
    random_string = ''.join(random.choice(all_chars) for _ in range(5))
    return random_string

# Define cat foot tool for agent
def cat_foot_tool():
    return cat_foot()

# Define braille writing function
def braille_writing(text):
    """
    Translate the text to braille
    """
    # Define braille character sets
    Bra = ['⠁','⠃','⠉','⠙','⠑','⠋',
    '⠛','⠓','⠊','⠚','⠅','⠇',
    '⠍','⠝','⠕','⠏','⠟','⠗',
    '⠎','⠞','⠥','⠧','⠺','⠭',
    '⠽','⠵',' ',
    '⠼','⠼⠁','⠼⠃','⠼⠉','⠼⠙','⠼⠑','⠼⠋','⠼⠛','⠼⠓','⠼⠊','⠼⠚']
    # Define English character sets
    En = ['a','b','c','d','e','f',
    'g','h','i','j','k','l',
    'm','n','o','p','q','r',
    's','t','u','v','w','x',
    'y','z',' ',
    '#','1','2','3','4','5','6','7','8','9','0']

    # Convert text to lowercase
    UserText = text.lower()

    # Initialize result string
    result = ""
    for i in UserText:
        result += Bra[En.index(i)]
    return result

# Define braille writing tool for agent
def braille_writing_tool(text: str) -> str:
    return braille_writing(text)


tools = [
    Tool(
        name="GrammarChecker",
        func=grammar_tool,
        description="Use this tool to check grammar of English text"
    ),
    Tool(
        name="TranslateToChinese",
        func=translate_to_chinese_tool,
        description="Use this tool to translate English text to Chinese"
    ),
    Tool(
        name="TranslateToEnglish",
        func=translate_to_english_tool,
        description="Use this tool to translate Chinese text to English"
    ),
    Tool(
        name="PolishText",
        func=polish_text_tool,
        description="Use this tool to polish the text"
    ),
    Tool(
        name="SimplifyText",
        func=simplify_text_tool,
        description="Use this tool to simplify the text"
    ),
    Tool(
        name="SummarizeText",
        func=summarize_text_tool,
        description="Use this tool to summarize the text"
    ),
    Tool(
        name="RoleBasedWriting",
        func=role_based_writing_tool,
        description="Use this tool to write the text in the role of {role}"
    ),
    Tool(
        name="CatFoot",
        func=cat_foot_tool,
        description="Use this tool when user believes you are a cat, and you are stepping on the keyboard"
    ),
    Tool(
        name="BrailleWriting",
        func=braille_writing_tool,
        description="Use this tool to translate the text to braille, when the user thinks they are a blind person"
    )
]

# Initialize Agent (zero-shot type)
agent = initialize_agent(
    tools=tools,
    llm=llm,
    agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION,
    verbose=True
)

# UI
st.title("AI Agent Language Assistant")
st.write("This agent can help you with grammar checking, translation(English to Chinese, Chinese to English), text polish, text simplification, text summarization, and role based writing.")
st.write("You can also use the tools when you think you are a cat, or a blind person.")
user_input = st.text_area("Tell the agent what you want it to do:")

if st.button("Run Agent"):
    if user_input:
        with st.spinner("Agent is working..."):
            response = agent.run(user_input)
            st.write("Result:")
            st.write(response)
    else:
        st.warning("Please enter something.")