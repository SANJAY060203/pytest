from src.auth import login
from src.calculator import add

def test_user_flow():
    result = login("alice", "1234")
    assert result["status"] == "OK"

    total = add(10, 20)
    assert total == 30
