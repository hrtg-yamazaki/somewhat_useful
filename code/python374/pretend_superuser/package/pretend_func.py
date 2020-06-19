from .user import User, Validator


def receive_inputs():
    """
    コンソールからの入力を受け取る関数。
    受け取りはカラムごとに一回ずつ。
    返り値はタプルで、呼び出し元にてアンパック代入。
    """
    v = Validator()
    
    # username
    username = input("Username: ")
    while not v.username_is_valid(username):
        username = input("Username: ")
    # email
    email = input("Email address: ")
    while not v.email_is_valid(email):
        email = input("Email address: ")
    # password
    password = input("Password: ")
    password_conf = input("Password (again): ")
    while not v.password_is_valid(password, password_conf):
        password = input("Password: ")
        password_conf = input("Password (again): ")
    
    return username, email, password
