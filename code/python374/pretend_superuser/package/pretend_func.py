from .user import Users, User, Validator


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


def sign_in_admin():
    """
    admin_mode用のユーザ認証関数。
    """
    print("---sign in---")
    users = Users()
    users.read_users()
    input_username = input("Username: ")
    for user in reversed(users.users): # reversedはユニーク制約作成までの凌ぎ
        if user.username == input_username:
            input_password = input("Password: ")
            while user.password != input_password:
                print("Please type and enter again.")
                input_password = input("Password: ")
            if user.password == input_password:
                print("Sign in successfully.")
                return True
    print("No user is founded.")
    return False


def reset_csv_file(path):
    """
    引数のpathで指定したファイルのcsvファイルの内容を空にする関数。
    """
    print("Are you sure you want to delete all contents in")
    print(">>>\t" + path)
    print("Please confirm.")
    conf = input("y/N: ")
    yes_list = ["y" , "Y", "Yes"]
    if conf in yes_list:
        with open(path, "w", encoding="utf-8") as f:
            f.write("")
        print("Reset [", path , "] successfully.")
        exit()
    else:
        print("Operation cancelled.")
