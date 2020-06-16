from .user import User, Validator


def main():
    """
    パッケージモジュールのメイン実行関数。
    現在開発中...
    """
    username, email, password = receive_inputs()
    user = User(username, email, password, superuser=True)
    print("Pretend to create superuser successfully.")
    user.print_data()


def receive_inputs():
    """
    コンソールからの入力を受け取る関数。
    返り値はタプルで、main()にてアンパック代入。
    """
    v = Validator()
    username = v.validate_username(input("Username: "))
    email = v.validate_email(input("Email address: "))
    password = v.validate_password(input("Password: "))
    
    return username, email, password