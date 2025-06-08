# AI Language Assistant

An intelligent language processing tool developed with Streamlit and OpenAI API, offering multiple language-related functionalities.

## Features

The tool integrates the following main features:

1. **Grammar Check**
   - Check English text for grammatical errors
   - Provide detailed error analysis and correction suggestions

2. **Translation**
   - English to Chinese translation
   - Chinese to English translation
   - Translation process explanation

3. **Text Enhancement**
   - Text Polish
   - Text Simplification
   - Text Summarization

4. **Role-based Writing**
   - Rewrite text in different role styles
   - Writing process explanation

5. **Special Features**
   - Braille Writing
   - Fun Feature: Cat Foot Typing

## Tech Stack

- Python
- Streamlit
- OpenAI API (GPT-3.5-turbo)
- LangChain
- langchain-openai
- langchain-community
- dotenv
- pytest (for testing)

## Installation

1. Clone the repository:
```bash
git clone [repository-url]
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

3. Configure environment variables:
Create a `.env` file and add:
```
OPENAI_API_KEY=your_api_key_here
```

## Usage

1. Run the application:
```bash
python -m streamlit run Language_tool.py --server.headless true
```

2. Open the displayed address in your browser (usually http://localhost:8501)

3. Enter your request in the text box, for example:
   - "Please check the grammar of this English text"
   - "Translate this Chinese text to English"
   - "Rewrite this text as a professional writer"

## Running Tests

1. Make sure all dependencies are installed:
```bash
pip install -r requirements.txt
```

2. Run the test suite using pytest:
```bash
python -m pytest test_language_tool.py -v
```
- All tests should pass. If you want to run all test files, use:
```bash
python -m pytest -v
```

3. Check the terminal output for detailed test results.

## Important Notes

- Valid OpenAI API key is required
- Stable internet connection is recommended
- Some features may require longer processing time

## Contributing

Issues and improvement suggestions are welcome!

## License

[Add license information] 
