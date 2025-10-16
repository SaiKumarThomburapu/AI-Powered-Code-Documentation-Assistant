import streamlit as st
import os
import sys
import google.generativeai as genai

# Add project root to Python path
project_root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, project_root)

from src.pipeline.generation_pipeline import create_documentation

# Configure Gemini
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY", "")
genai.configure(api_key=GEMINI_API_KEY)

# Page config
st.set_page_config(
    page_title="AI Code Documentation Assistant",
    page_icon=" ",
    layout="wide"
)

ALLOWED_EXTENSIONS = [".py", ".txt", ".md", ".js", ".java", ".cpp", ".c", ".go"]

def answer_question(explanation: str, question: str) -> str:
    """Answer user questions about the explanation."""
    prompt = f"""
Based on this code explanation:

{explanation}

User Question: {question}

Provide a clear, professional answer in 2-4 sentences. Use flowing paragraphs, not line-by-line format.
"""
    model = genai.GenerativeModel("gemini-2.0-flash-exp")
    response = model.generate_content(prompt)
    
    # Clean the response
    try:
        clean_answer = response.text.strip()
    except:
        clean_answer = str(response.candidates[0].content.parts[0].text).strip()
    
    return clean_answer


# Title and description
st.title("AI-Powered Code Documentation Assistant")
st.markdown("Generate professional explanations for your code instantly")

# Create tabs for input methods
tab1, tab2 = st.tabs([" Paste Code", " Upload File"])

# Tab 1: Paste Code
with tab1:
    st.subheader("Paste Your Code")
    code_input = st.text_area(
        "Enter your code here:",
        height=300,
        placeholder="Paste your Python, JavaScript, or any code here..."
    )
    
    if st.button(" Generate Documentation", key="paste_btn"):
        if code_input.strip():
            with st.spinner("Analyzing code and generating documentation..."):
                try:
                    result = create_documentation(code_input, "pasted_code")
                    
                    st.success(" Documentation Generated!")
                    
                    # Display styled documentation
                    st.markdown("###  Generated Documentation")
                    st.text(result["document"])
                    
                    # Store in session state for Q&A
                    st.session_state["explanation"] = result["explanation"]
                    st.session_state["full_doc"] = result["document"]
                    
                except Exception as e:
                    st.error(f"Error: {str(e)}")
        else:
            st.warning("Please paste some code first")

# Tab 2: Upload File
with tab2:
    st.subheader("Upload Code File")
    uploaded_file = st.file_uploader(
        "Choose a code file",
        type=[ext.replace(".", "") for ext in ALLOWED_EXTENSIONS]
    )
    
    if uploaded_file:
        st.info(f" File: {uploaded_file.name}")
        
        if st.button(" Generate Documentation", key="upload_btn"):
            with st.spinner("Processing file and generating documentation..."):
                try:
                    code = uploaded_file.getvalue().decode("utf-8")
                    result = create_documentation(code, uploaded_file.name)
                    
                    st.success(" Documentation Generated!")
                    
                    # Display styled documentation
                    st.markdown("###  Generated Documentation")
                    st.text(result["document"])
                    
                    # Store in session state for Q&A
                    st.session_state["explanation"] = result["explanation"]
                    st.session_state["full_doc"] = result["document"]
                    
                except Exception as e:
                    st.error(f"Error: {str(e)}")

# Q&A Section (appears after documentation is generated)
if "explanation" in st.session_state:
    st.markdown("---")
    st.markdown("###  Ask Questions About the Code")
    
    question = st.text_input(
        "Ask anything about the generated explanation:",
        placeholder="e.g., What does the main function do?"
    )
    
    if st.button(" Get Answer"):
        if question.strip():
            with st.spinner("Thinking..."):
                try:
                    answer = answer_question(
                        st.session_state["explanation"],
                        question
                    )
                    st.markdown("####  Answer:")
                    st.info(answer)
                except Exception as e:
                    st.error(f"Error: {str(e)}")
        else:
            st.warning(" Please enter a question")
    
    # Download button
    st.markdown("---")
    st.download_button(
        label="Download Documentation",
        data=st.session_state["full_doc"],
        file_name="documentation.txt",
        mime="text/plain"
    )









