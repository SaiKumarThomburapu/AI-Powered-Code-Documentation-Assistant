import ast
from typing import List, Dict

def extract_code_structure(source: str) -> Dict:
    """Extract functions and classes from source code."""
    try:
        tree = ast.parse(source)
        functions = []
        classes = []
        
        for node in ast.walk(tree):
            if isinstance(node, (ast.FunctionDef, ast.AsyncFunctionDef)):
                functions.append(node.name)
            elif isinstance(node, ast.ClassDef):
                classes.append(node.name)
        
        return {
            "functions": functions,
            "classes": classes,
            "total_lines": len(source.split('\n'))
        }
    except:
        return {"functions": [], "classes": [], "total_lines": len(source.split('\n'))}


