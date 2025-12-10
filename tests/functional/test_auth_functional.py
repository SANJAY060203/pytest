from src.auth import login

def test_login_success():
    assert login("alice", "1234")["status"] == "OK"
