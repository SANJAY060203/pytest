users = {"alice": "1234", "bob": "abcd"}

def login(username, password):
    if username not in users:
        return {"status": "FAIL", "reason": "User not found"}
    if users[username] != password:
        return {"status": "FAIL", "reason": "Wrong password"}
    return {"status": "OK"}
