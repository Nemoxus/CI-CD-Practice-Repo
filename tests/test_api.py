from fastapi.testclient import TestClient 
# the TestClient here is used to simulate requests to the FastAPI application without running a server
from app.main import app

client = TestClient(app)

def test_health():
    res = client.get("/health")
    assert res.status_code == 200, "Health check endpoint did not return status code 200"
    assert res.json() == {"status": "ok"}

    # assert keyword checks for boolean conditions in python
    # if the condition is true, the program continues to run normally.
    # If the condition is false, an AssertionError is raised, and the program stops executing

def test_prediction_high():
    res = client.post("/predict", json={"age": 50, "cholesterol": 250})
    assert res.json()["risk"] == "high", "Prediction for high risk failed"

def test_prediction_low():
    res = client.post("/predict", json={"age": 30, "cholesterol": 180})
    assert res.json()["risk"] == "low", "Prediction for low risk failed"


# declaring 2 tests in this file to test the FastAPI application
# these tests simulate requests to the endpoints and verify the responses
# pytest module is used to run these tests and report any failures
