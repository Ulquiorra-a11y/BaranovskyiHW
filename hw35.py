class User:
    total_users = 0
    def __init__(self, login, password):
        if not isinstance(login, str) or not login.strip():
            raise ValueError("Login must not be empty")
        if not isinstance(password, str) or len(password) < 5:
            raise ValueError("Password must not be empty and contain at least 5 characters")
        self.login = login
        self.password = password
        User.total_users += 1

    @classmethod
    def get_total(cls):
        return cls.total_users

    def __str__(self):
        return f"User: {self.login}"

u1 = User("john", "1346fdsg")
# u2 = User("john2", "e5r")
u3 = User("", "sadfgafdg")

print(User.get_total())
print(u1)
# print(u2)
print(u3)
