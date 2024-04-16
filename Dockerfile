FROM python:3.8-slim

WORKDIR /app

COPY . /app

RUN pip install --trusted-host pypi.python.org -r requirements.txt

CMD ["uvicorn", "api:app", "--host", "0.0.0.0", "--port", "80"]
