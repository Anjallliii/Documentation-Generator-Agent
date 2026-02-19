from fastapi import APIRouter, UploadFile, File
from app.schemas.generate_schema import GenerateRequest, GenerateResponse
from app.services.scaledown_client import generate_documentation
from app.utils.file_parser import parse_file

router = APIRouter(prefix="/generate", tags=["Documentation"])

@router.post("/", response_model=GenerateResponse)
def generate_docs(request: GenerateRequest):
    doc = generate_documentation(request.prompt)
    return {"documentation": doc}

@router.post("/file", response_model=GenerateResponse)
def generate_from_file(file: UploadFile = File(...)):
    content = parse_file(file)
    prompt = f"Generate professional documentation for the following code:\n{content}"
    doc = generate_documentation(prompt)
    return {"documentation": doc}
