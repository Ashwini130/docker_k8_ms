import requests

def test_service_b_counter():
    url = "http://localhost:6000/data"

    r1 = requests.get(url).json()
    r2 = requests.get(url).json()

    assert r2["counter"] == r1["counter"] + 1
