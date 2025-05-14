from fastapi.testclient import TestClient
from main import app

client = TestClient(app)


def test_get_root():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": "Hello From FastAPI in Docker!"}
    
    
def test_greet_user():
    response  = client.post("/greet/maxbhauoo")
    assert response.status_code == 200
    assert response.json() == {"message": "Hello maxbhauoo!"}