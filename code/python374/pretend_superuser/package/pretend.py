from .user import User, Validator


def main():
    """
    パッケージモジュールのメイン実行関数。
    現在開発中...
    """
    # 入力を受け取る
    v = Validator()
    username = v.validate_username(input("Username: "))
    email = input("Email address: ")
    password = input("Password: ")
    password_conf = input("Password (again): ")
    # password1, 2の入力内容一致確認
    if password == password_conf:
        # 一致していればUserインスタンス作成
        user = User(username, email, password)
        print("Pretend to create superuser successfully.")
        user.print_data()
    else:
        # していなければメッセージを表示して再帰
        print("Your passwords didn\'t match.")
        main()
