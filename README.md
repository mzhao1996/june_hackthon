# English Grammar Checker

A simple web application that uses OpenAI's GPT-3.5 to check English grammar and provide corrections.

## Setup

1. Clone this repository
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
3. Create a `.env` file in the root directory and add your OpenAI API key:
   ```
   OPENAI_API_KEY=your_api_key_here
   ```

## Usage

1. Run the application:
   ```bash
   python -m streamlit run grammar_checker.py --server.headless true
   ```
2. Open your web browser and navigate to the URL shown in the terminal (usually http://localhost:8501)
3. Enter your text in the input area and click "Check Grammar"
4. View the grammar check results

## Features

- Real-time grammar checking
- Detailed error explanations
- Corrected version of the text
- User-friendly web interface 
