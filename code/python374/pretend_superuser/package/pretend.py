from .pretend_func import registration, sign_in_admin, reset_csv_file
from .general import str_now, receive_input
from .user import User, Users, USERS_CSV_PATH


def createsuperuser():
    """
    コマンドライン引数に createsuperuser を受け取った場合の実行関数。
    現在開発中...
    """
    username, email, password = registration()
    user = User.new_user(
        username, email, password,
        str_now(), superuser=True
    )
    user.create_user(USERS_CSV_PATH)
    print("Pretend to create superuser successfully.")


def runserver():
    """
    コマンドライン引数に runserver を受け取った場合の実行関数。
    未実装。
    """
    print("[ Exit: Ctrl + c ]")
    runserver_message = (
        "Although there are no server running actually, "
        "you can use the following functions instead."
        "\nPlease select."
    )
    print(runserver_message)
    while True:
        choice = receive_input("1: admin\n2: signup\n0: exit\n")
        if choice == "1":
            admin()
        elif choice == "2":
            signup()
        elif choice == "0":
            print("Operation finished.")
            break
        else:
            print("please retry to select.")


def admin():
    """
    superuser=Trueのデータでログイン後、
    Usersのデータの閲覧などができる
    開発中。。。
    """
    # ログインできなければ関数終了
    if not sign_in_admin():
        return
    # 選択画面
    while True:
        choice = receive_input(
            "1: show all users\n2: reset csv file\n0: exit\n"
        )
        if choice == "1":
            print("show all users")
        elif choice == "2":
            reset_csv_file(USERS_CSV_PATH)
        elif choice == "0":
            print("Exited from admin-mode...")
            break
        else:
            print("please retry to select.")


def signup():
    """
    superuser=FalseのUserを作ることができる関数。
    """
    username, email, password = registration()
    user = User.new_user(username, email, password, str_now())
    user.create_user(USERS_CSV_PATH)
    print("--Your info--")
    for k, v in user.info().items():
        print(k, v, sep=": ", end=", ")
    print("\n-----")
    print("Pretend to signup successfully!")
