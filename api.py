from fastapi import FastAPI, UploadFile, File, HTTPException
from pdf_reader import PDFProcessor
import uvicorn
import os
import shutil
import tempfile

app = FastAPI()

@app.post("/process-pdf/")
async def process_pdf(file: UploadFile = File(...)):
    with tempfile.NamedTemporaryFile(delete=False) as temp_file:
        shutil.copyfileobj(file.file, temp_file)
        temp_file_path = temp_file.name  

    try:
        processor = PDFProcessor(temp_file_path)
        total = processor.extract_values()
        return {"total": total}
    finally:
        if os.path.exists(temp_file_path):
            os.remove(temp_file_path)

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
