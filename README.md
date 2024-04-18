# Sai-Data-Science-Project
```bash
git clone https://github.com/yourusername/pdf-processing-library.git
cd pdf-processing-library
```
Set up a virtual environment:
Setting up a virtual environment is recommended to manage dependencies cleanly:

bash
Copy code
python -m venv venv
source venv/bin/activate  # On Windows use `venv\Scripts\activate`
Install the required dependencies:
bash
Copy code
pip install -r requirements.txt
Usage
Command Line Interface
To process a PDF and extract numbers using the CLI, run:

bash
Copy code
python src/cli.py /path/to/your/pdf/file.pdf
REST API
Start the FastAPI application:

bash
Copy code
uvicorn src.api:app --reload --host 0.0.0.0 --port 8000
The API is accessible at http://localhost:8000. Use the endpoint /process-pdf/ to process PDF files:

bash
Copy code
curl -X 'POST' \
  'http://localhost:8000/process-pdf/' \
  -H 'accept: application/json' \
  -H 'Content-Type: multipart/form-data' \
  -F 'file=@/path/to/your/file.pdf;type=application/pdf'
Docker
To build and run the Docker container:

bash
Copy code
docker build -t my-pdf-app .
docker run -p 8000:80 my-pdf-app
Testing
Execute tests using pytest:

bash
Copy code
pytest tests/
