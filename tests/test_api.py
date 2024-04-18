from fastapi.testclient import TestClient
from src.api import app

client = TestClient(app)

def test_process_pdf():
    response = client.post(
        "/process-pdf/",
        files={"file": ("filename.pdf", open("temp/filled_form_0.pdf", "rb"), "application/pdf")}
    )
    assert response.status_code == 200
    assert 123 in response.json()['numbers']  # Assuming 123 is expected in the PDF
