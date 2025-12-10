class FakeDB:
    def __init__(self):
        self.users = []

    def insert(self, name):
        self.users.append(name)
        return len(self.users)

    def get(self, user_id):
        return self.users[user_id - 1]
