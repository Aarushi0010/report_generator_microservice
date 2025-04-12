from fastapi import FastAPI
from app.routes import upload
from app.utils.rules_loader import load_rules
from app.services.report_generator import generate_report
from fastapi.responses import FileResponse
import os
import yaml

app = FastAPI(title="Report Generator Microservice")

app.include_router(upload.router, prefix="/upload", tags=["Upload"])

@app.get("/")
def root():
    return {"message": "Report Generator is up!"}

@app.get("/rules")
def get_rules():
    rules = load_rules()
    return {"transformation_rules": rules}

@app.post("/generate-report")
def generate():
    output_file = generate_report()
    return {"message": "Report generated successfully", "file": output_file}

@app.get("/download-report")
def download_report():
    output_path = "data/output/output.csv"
    if os.path.exists(output_path):
        return FileResponse(output_path, media_type='text/csv', filename="report.csv")
    else:
        return {"error": "Report not found. Please generate it first."}
    
@app.post("/rules")
def update_rules(new_rules: dict):
    config_path = "config/transformation_rules.yaml"
    with open(config_path, "w") as f:
        yaml.dump({"rules": new_rules}, f)
    return {"message": "Transformation rules updated successfully"}