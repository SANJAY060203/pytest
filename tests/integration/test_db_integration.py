def test_db_integration(fake_db):
    user_id = fake_db.insert("Alice")
    assert fake_db.get(user_id) == "Alice"
