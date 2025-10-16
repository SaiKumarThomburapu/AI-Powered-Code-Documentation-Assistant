import google.generativeai as genai
from src.config.config_entity import settings
from src.constants import CODE_EXPLANATION_PROMPT
from src.utils.helpers import format_prompt, style_documentation

genai.configure(api_key=settings.GEMINI_API_KEY)

def clean_gemini_response(response) -> str:
    """Extract and clean text from Gemini response."""
    try:
        # Get the text content
        raw_text = response.text
        
        # Remove code block markers if present
        raw_text = raw_text.replace('``````', '')
        
        # Replace escaped newlines with actual newlines
        raw_text = raw_text.replace('\\n', '\n')
        
        # Remove extra spaces
        lines = [line.strip() for line in raw_text.split('\n') if line.strip()]
        
        return '\n'.join(lines)
    except:
        # Fallback method
        return str(response.candidates[0].content.parts[0].text)

def generate_explanation(code: str) -> str:
    """Generate professional explanation for code."""
    prompt = format_prompt(code, CODE_EXPLANATION_PROMPT)
    model = genai.GenerativeModel("gemini-2.0-flash-exp")
    response = model.generate_content(prompt)
    
    # Clean the response
    clean_text = clean_gemini_response(response)
    
    # Apply styling
    styled_content = style_documentation(clean_text)
    
    return styled_content




