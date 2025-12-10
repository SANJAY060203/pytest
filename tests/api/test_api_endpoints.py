def test_api_hello(client):
    res = client.get("/hello/Bob")
    assert res.json() == {"message": "Hello Bob"}

def test_profile_api(client):
    res = client.get("/profile")
    assert "email" in res.json()
