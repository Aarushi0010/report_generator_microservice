from fastapi import FastAPI
from app.routes import upload
from app.utils.rules_loader import load_rules


app = FastAPI(title="Report Generator Microservice")

app.include_router(upload.router, prefix="/upload", tags=["Upload"])

@app.get("/")
def root():
    return {"message": "Report Generator is up!"}

@app.get("/rules")
def get_rules():
    rules = load_rules()
    return {"transformation_rules": rules}