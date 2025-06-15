import requests
import pdfkit
from typing import Optional
import os

def web_to_pdf(url: str, output_path: Optional[str] = None) -> str:
    """
    Convert a webpage to PDF format
    
    Args:
        url (str): The URL of the webpage to convert
        output_path (str, optional): The path where the PDF should be saved. 
                                   If not provided, will use the webpage title as filename
    
    Returns:
        str: Path to the generated PDF file
    """
    try:
        # Get webpage content
        response = requests.get(url)
        response.raise_for_status()
        
        # If no output path is provided, use the webpage title
        if not output_path:
            # Create output directory if it doesn't exist
            if not os.path.exists('output'):
                os.makedirs('output')
            output_path = os.path.join('output', 'webpage.pdf')
        
        # Configure pdfkit options
        options = {
            'page-size': 'A4',
            'margin-top': '0mm',
            'margin-right': '0mm',
            'margin-bottom': '0mm',
            'margin-left': '0mm',
            'encoding': 'UTF-8',
            'no-outline': None
        }
        
        # Convert webpage to PDF
        pdfkit.from_url(url, output_path, options=options)
        
        return output_path
    
    except requests.RequestException as e:
        raise Exception(f"Error fetching webpage: {str(e)}")
    except Exception as e:
        raise Exception(f"Error converting to PDF: {str(e)}")

# Example usage
if __name__ == "__main__":
    url = "https://example.com"
    try:
        pdf_path = web_to_pdf(url)
        print(f"PDF has been created successfully at: {pdf_path}")
    except Exception as e:
        print(f"Error: {str(e)}") 