# Sai-Data-Science-Project

```bash
git clone https://github.com/saishreyakumar/Sai-Data-Science-Project.git
cd Sai-Data-Science-Project
```
## Set up a virtual environment:

```bash
python -m venv venv
source venv/bin/activate 
```

## Install the required dependencies:
```bash
pip install -r requirements.txt
```


## For Command Line Interface, run:


```bash
python src/cli.py /temp/filled_form_0.pdf # Or whatever Form you want to calculate the sum in, just add that particular pdf on to the temp folder
```

## For REST API
### Start the FastAPI application:

```bash
uvicorn src.api:app --reload --host 0.0.0.0 --port 8000
```
### The API is accessible at http://localhost:8000. Use the endpoint /process-pdf/ to process PDF files:

```bash
curl -X 'POST' \
  'http://localhost:8000/process-pdf/' \
  -H 'accept: application/json' \
  -H 'Content-Type: multipart/form-data' \
  -F 'file=@/path/to/your/file.pdf;type=application/pdf' # please replace the path/to/your/file.pdf with the location of you actual file, which you can get through VS Code and copy path from the temp folder
```
## Docker
### To build and run the Docker container:

```bash
docker build -t my-pdf-app .
docker run -p 8000:80 my-pdf-app
```

## Testing
### Execute tests using pytest:

```bash
pytest tests/
```
