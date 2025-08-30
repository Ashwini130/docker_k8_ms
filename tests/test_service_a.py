import requests

def test_service_a_calls_b():
    url = "http://localhost:5000"
    r = requests.get(url).json()

    assert "message" in r
    assert "data" in r
    assert "counter" in r["data"]
