from fastapi import APIRouter, UploadFile, File, HTTPException
import os
import shutil

router = APIRouter()

DATA_DIR = "data"
INPUT_DIR = os.path.join(DATA_DIR, "input")
REFERENCE_DIR = os.path.join(DATA_DIR, "reference")

os.makedirs(INPUT_DIR, exist_ok=True)
os.makedirs(REFERENCE_DIR, exist_ok=True)

@router.post("/upload/input")
async def upload_input_file(file: UploadFile = File(...)):
    if not file.filename.endswith(".csv"):
        raise HTTPException(status_code=400, detail="Only .csv files are allowed.")
    file_path = os.path.join(INPUT_DIR, file.filename)
    with open(file_path, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)
    return {"message": f"Input file '{file.filename}' uploaded successfully."}

@router.post("/upload/reference")
async def upload_reference_file(file: UploadFile = File(...)):
    if not file.filename.endswith(".csv"):
        raise HTTPException(status_code=400, detail="Only .csv files are allowed.")
    file_path = os.path.join(REFERENCE_DIR, file.filename)
    with open(file_path, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)
    return {"message": f"Reference file '{file.filename}' uploaded successfully."}
