from .user import User


def main():
    print("Now developing....")
    user = User("testuser", "test@test.com", "password")
    user.print_data()
