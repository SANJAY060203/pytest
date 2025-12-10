def test_profile_contract(client):
    res = client.get("/profile")
    assert set(res.json().keys()) == {"id", "name", "email"}
