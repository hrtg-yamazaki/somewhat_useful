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
    email = input("Email address: ")
    password = input("Password: ")
    password_conf = input("Password (again): ")
    # パスワードとパスワード確認用入力の一致確認
    if password != password_conf:
        print("Your passwords didn\'t match.")
        receive_inputs()
    
    return username, email, password