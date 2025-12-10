from src.auth import login

def test_unknown_user():
    assert login("charlie", "x")["status"] == "FAIL"
