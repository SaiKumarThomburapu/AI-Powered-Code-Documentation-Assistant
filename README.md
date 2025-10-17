 
#  AI-Powered Code Documentation Assistant

[![Python 3.10+](https://img.shields.io/badge/python-3.10+-blue.svg)](https://www.python.org/downloads/)
[![FastAPI](https://img.shields.io/badge/FastAPI-0.104+-green.svg)](https://fastapi.tiangolo.com/)
[![Streamlit](https://img.shields.io/badge/Streamlit-1.28+-red.svg)](https://streamlit.io/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

> An intelligent tool that automatically generates professional, concise technical documentation from code using AI. Built with FastAPI and Streamlit, powered by Google Gemini.

---

##  Overview

This project automates the creation of clear, professional code documentation using AI. It analyzes code structure, extracts key components, and generates well-formatted explanations — saving developers time and ensuring consistency in documentation quality.

**Key Value Proposition:** Transform any code into readable, professional documentation in seconds.

---

##  Features

- **Dual Input Methods** - Paste code directly or upload files (Python, JavaScript, Java, C++, Go, etc.)
-  **AI-Powered Analysis** - Uses Google Gemini to understand and explain code logic
-  **Styled Documentation** - Generates single, well-formatted `.txt` files with clear headings and structure
- **Interactive Q&A** - Ask follow-up questions about generated explanations (Streamlit UI)
-  **Independent Systems** - FastAPI backend and Streamlit frontend operate completely independently
-  **Professional Output** - Concise, technical, and easy-to-read explanations
- **Multiple Languages** - Supports Python, JavaScript, Java, C++, C, Go, and more

---

##  Architecture

┌─────────────────┐ ┌──────────────────┐
│ FastAPI Backend│ │ Streamlit UI │
│ (Independent) │ │ (Independent) │
├─────────────────┤ ├──────────────────┤
│ - File Upload │ │ - File Upload │
│ - Text Input │ │ - Text Input │
│ - Doc Generator │ │ - Doc Generator │
│ - File Storage │ │ - Q&A System │
└─────────────────┘ └──────────────────┘
│ │
└───────────┬───────────────┘
│
┌───────▼────────┐
│ Gemini AI API │
│ (Shared) │
└────────────────┘




### Project Structure

docs-assistant/
├── src/
│ ├── constants/ # Prompts and configuration
│ ├── config/ # Settings management
│ ├── components/ # Core logic (parser, generator)
│ ├── pipeline/ # Documentation generation pipeline
│ └── utils/ # Helper functions
├── api/
│ └── main.py # FastAPI server (independent)
├── ui/
│ └── app.py # Streamlit app (independent)
├── docs/ # Generated documentation files
├── tests/ # Unit tests
├── examples/ # Sample code files
├── requirements.txt # Dependencies
├── Dockerfile # Container configuration
└── README.md # This file


---

##  Quick Start

### Prerequisites

- Python 3.10 or higher
- Google Gemini API key ([Get it here](https://aistudio.google.com/app/apikey))

### Installation

1. **Clone the repository**
git clone https://github.com/SaiKumarThomburapu/AI-Powered-Documentation-Assistant.git
cd docs-assistant


2. **Create virtual environment**
python3 -m venv venv
source venv/bin/activate # On Windows: venv\Scripts\activate


3. **Install dependencies**
pip install -r requirements.txt


4. **Set up API key**
export GEMINI_API_KEY="your-api-key-here"


---

##  Usage

### Option 1: FastAPI Backend (Independent)

**Start the server:**
uvicorn api.main:app --reload --host 127.0.0.1 --port 8000


**Access the API:**
- Interactive docs: http://localhost:8000/docs
- Root endpoint: http://localhost:8000

**Example: Generate from text**
curl -X POST "http://localhost:8000/generate/text"
-H "Content-Type: application/json"
-d '{"code": "def hello():\n print("Hello World")"}'


**Example: Upload file**
curl -X POST "http://localhost:8000/generate/file"
-F "file=@example.py"


**Generated documentation will be saved in:** `docs/documentation.txt`

---

### Option 2: Streamlit UI (Independent)

**Start the app:**
streamlit run ui/app.py



**Access the UI:** http://localhost:8501

**Features:**
1. **Paste Code Tab** - Directly paste your code
2. **Upload File Tab** - Upload code files
3. **Q&A Section** - Ask questions about generated explanations
4. **Download Button** - Save documentation locally

---

##  Example Output

### Input Code:
def calculate_average(numbers):
total = sum(numbers)
return total / len(numbers)


### Generated Documentation:

==============================================================
CODE DOCUMENTATION
File: example.py
Lines of Code: 3
Functions: 1
Classes: 0

==============================================================

Overview
==============================================================

This code defines a utility function to compute the arithmetic
mean of a list of numbers.

Key Components
Function: calculate_average

Accepts a list of numbers as input

Computes sum using built-in sum() function

Returns average by dividing total by count

Technical Details
Uses Python's sum() and len() built-ins for efficiency.
No error handling for empty lists or non-numeric inputs.

==============================================================
Generated by AI Documentation Assistant

---

##  Testing

Run tests with pytest:
pytest tests/ -v


---

## Configuration

### Environment Variables

| Variable | Description | Required |
|----------|-------------|----------|
| `GEMINI_API_KEY` | Google Gemini API key | Yes |

### Supported File Types

- Python (`.py`)
- JavaScript (`.js`)
- Java (`.java`)
- C++ (`.cpp`)
- C (`.c`)
- Go (`.go`)
- Markdown (`.md`)
- Text (`.txt`)

---

##  Code Quality & Design

- **Modular Architecture** - Clear separation of concerns (parser, generator, pipeline)
- **MLOps Pattern** - Industry-standard project structure
- **Error Handling** - Graceful failures with helpful messages
- **Type Hints** - Enhanced code readability and IDE support
- **Environment Configuration** - Secure API key management
- **Independent Systems** - Backend and frontend don't depend on each other

---

##  Technical Decisions

### Why Google Gemini?
- Fast inference times
- Excellent code understanding
- Free tier available
- Strong multi-language support

### Why FastAPI + Streamlit?
- **FastAPI**: High performance, automatic API docs, async support
- **Streamlit**: Rapid prototyping, beautiful UI, no frontend code needed
- **Independence**: Each can be deployed separately

### Why Single File Output?
- Easier to read and share
- Clear structure with styled headings
- Professional appearance
- Reduced file management overhead

##  Contact

**Saikumar**  
 Hyderabad, India  
saikumarthomburapu@gmail.com  
 

---

##  Acknowledgments

- Google Gemini AI for powerful language models
- FastAPI framework for excellent API development experience
- Streamlit for making beautiful UIs accessible to Python developers
- The open-source community for inspiration and tools

**Built with ❤️ for the Technical Writer Assessment**

*Showcasing AI/ML expertise, automation workflows, and technical documentation skills*
