from fastapi import FastAPI, UploadFile, File, Body, HTTPException
from fastapi.responses import FileResponse
import os
from src.pipeline.generation_pipeline import create_documentation

app = FastAPI(title="AI Documentation Generator API")

ALLOWED_EXTENSIONS = {".py", ".txt", ".md", ".js", ".java", ".cpp", ".c", ".go"}

@app.get("/")
def root():
    return {"message": "AI Documentation Generator API", "status": "active"}

@app.post("/generate/text")
async def generate_from_text(code: str = Body(..., embed=True)):
    """Generate documentation from pasted code text."""
    if not code.strip():
        raise HTTPException(status_code=400, detail="Code cannot be empty")
    
    try:
        result = create_documentation(code, "pasted_code.txt")
        
        # Write to docs folder
        os.makedirs("docs", exist_ok=True)
        doc_path = "docs/documentation.txt"
        
        with open(doc_path, "w", encoding="utf-8") as f:
            f.write(result["document"])
        
        return {
            "message": "Documentation generated successfully",
            "file_path": doc_path,
            "preview": result["explanation"][:500] + "..."
        }
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.post("/generate/file")
async def generate_from_file(file: UploadFile = File(...)):
    """Generate documentation from uploaded code file."""
    ext = os.path.splitext(file.filename)[1].lower()
    
    if ext not in ALLOWED_EXTENSIONS:
        raise HTTPException(
            status_code=400,
            detail=f"Unsupported file type. Allowed: {', '.join(ALLOWED_EXTENSIONS)}"
        )
    
    try:
        contents = await file.read()
        code = contents.decode("utf-8")
        
        result = create_documentation(code, file.filename)
        
        # Write to docs folder
        os.makedirs("docs", exist_ok=True)
        doc_path = f"docs/{os.path.splitext(file.filename)[0]}_documentation.txt"
        
        with open(doc_path, "w", encoding="utf-8") as f:
            f.write(result["document"])
        
        return {
            "message": "Documentation generated successfully",
            "filename": file.filename,
            "file_path": doc_path,
            "structure": result["structure"]
        }
    except UnicodeDecodeError:
        raise HTTPException(status_code=400, detail="Unable to decode file as text")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.get("/download/{filename}")
def download_documentation(filename: str):
    """Download generated documentation."""
    file_path = f"docs/{filename}"
    if not os.path.exists(file_path):
        raise HTTPException(status_code=404, detail="Documentation file not found")
    return FileResponse(file_path, filename=filename)





