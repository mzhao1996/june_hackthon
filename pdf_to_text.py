import PyPDF2
from typing import Optional, List
import os

def pdf_to_text(pdf_path: str) -> str:
    """
    Convert PDF file to text
    
    Args:
        pdf_path (str): Path to the PDF file
        
    Returns:
        str: Extracted text from the PDF
    """
    try:
        text = ""
        with open(pdf_path, 'rb') as file:
            # Create PDF reader object
            pdf_reader = PyPDF2.PdfReader(file)
            
            # Get number of pages
            num_pages = len(pdf_reader.pages)
            
            # Extract text from each page
            for page_num in range(num_pages):
                page = pdf_reader.pages[page_num]
                text += page.extract_text() + "\n"
                
        return text.strip()
    
    except Exception as e:
        raise Exception(f"Error converting PDF to text: {str(e)}")

def analyze_pdf_content(text: str) -> dict:
    """
    Analyze the content of the PDF text
    
    Args:
        text (str): Text content from PDF
        
    Returns:
        dict: Analysis results including word count, paragraph count, etc.
    """
    # Basic analysis
    words = text.split()
    paragraphs = text.split('\n\n')
    
    analysis = {
        'total_words': len(words),
        'total_paragraphs': len(paragraphs),
        'total_characters': len(text),
        'average_words_per_paragraph': len(words) / len(paragraphs) if paragraphs else 0,
        'first_100_words': ' '.join(words[:100]) if words else ''
    }
    
    return analysis

def process_pdf_for_analysis(pdf_path: str) -> dict:
    """
    Process PDF file and return analysis results
    
    Args:
        pdf_path (str): Path to the PDF file
        
    Returns:
        dict: Analysis results
    """
    try:
        # Convert PDF to text
        text = pdf_to_text(pdf_path)
        
        return {
            'success': True,
            'text_content': text
        }
    
    except Exception as e:
        return {
            'success': False,
            'error': str(e)
        }