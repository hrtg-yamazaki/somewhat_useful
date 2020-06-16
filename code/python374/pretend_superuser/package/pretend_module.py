from .user import User, Validator


def receive_inputs():
    """
    コンソールからの入力を受け取る関数。
    返り値はタプルで、呼び出し元にてアンパック代入。
    """
    v = Validator()
    username = v.validate_username(input("Username: "))
    email = v.validate_email(input("Email address: "))
    password = v.validate_password(input("Password: "))
    
    return username, email, password


def new_user(*args, **kwargs):
    """
    Userクラスのインスタンスを作成する関数。
    """
    # セキュリティ？的に問題なければ*args, **kwargsのまま飛ばしたい
    # 他の方法で「呼び出し元依存の superuser T/F 設定」ができるならあとで修正
    user = User(*args, **kwargs)
    return user
