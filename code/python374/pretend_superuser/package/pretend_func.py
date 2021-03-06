import getpass
from .user import Users, User
from .validator import Validator
from .general import receive_input, USERS_CSV_PATH, translate_bool


def registration():
    """
    コンソールからの入力を受け取る関数。
    受け取りはカラムごとに一回ずつ。
    返り値はタプルで、呼び出し元にてアンパック代入。
    """
    v = Validator()
    # username
    username_message = \
       "Username (leave blank to use \'" + getpass.getuser() + "\'): "
    username = receive_input(username_message)
    while not v.username_is_valid(username):
        username = receive_input(username_message)
    # email
    email = receive_input("Email address: ")
    while not v.email_is_valid(email):
        email = receive_input("Email address: ")
    # password
    password = receive_input("Password: ")
    password_conf = receive_input("Password (again): ")
    while not v.password_is_valid(password, password_conf):
        password = receive_input("Password: ")
        password_conf = receive_input("Password (again): ")
    
    return username, email, password


def sign_in_admin():
    """
    admin_mode用のユーザ認証関数。
    """
    print("---sign in---")
    users = Users()
    users.users = users.read_users(USERS_CSV_PATH)
    input_username = receive_input("Username: ")
    for user in reversed(users.users): # reversedはユニーク制約作成までの凌ぎ
        if user.username == input_username:
            input_password = receive_input("Password: ")
            while user.password != input_password:
                print("Please type and enter again.")
                input_password = receive_input("Password: ")
            if user.password == input_password:
                if translate_bool(user.superuser):
                    print("Sign in successfully.")
                    return True
                else:
                    print("Permission Denied.")
                    return False
    print("No user is founded.")
    return False


def browse_users_list():
    """
    登録されているユーザーの一覧を表示する関数。
    """
    users = Users()
    users.users = users.read_users(USERS_CSV_PATH)
    print(users.show_all_users())


def reset_csv_file(path):
    """
    引数のpathで指定したファイルのcsvファイルの内容を空にする関数。
    """
    print("Are you sure you want to delete all contents in")
    print(">>>\t" + path)
    print("Please confirm.")
    conf = receive_input("y/N: ")
    yes_list = ["y" , "Y", "Yes"]
    if conf in yes_list:
        with open(path, "w", encoding="utf-8"):
            pass
        Users.set_users_csv()
        print("Reset [", path , "] successfully.")
        print("Exiting...")
        exit()
    else:
        print("Operation cancelled.")
