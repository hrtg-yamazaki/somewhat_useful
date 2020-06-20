from .pretend_func import receive_inputs, sign_in_admin
from .general import str_now
from .user import User, Users


def createsuperuser():
    """
    コマンドライン引数に createsuperuser を受け取った場合の実行関数。
    現在開発中...
    """
    username, email, password = receive_inputs()
    user = User.new_user(
        username, email, password,
        str_now(), superuser=True
    )
    user.create_user()
    print("Pretend to create superuser successfully.")


def runserver():
    """
    コマンドライン引数に runserver を受け取った場合の実行関数。
    未実装。
    """
    runserver_message = (
        "Although there are no server running actually, "
        "you can use the following functions instead."
        "\nPlease select."
    )
    print(runserver_message)
    while True:
        choice = input("1: admin\n2: signup\n0: exit\n")
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
        choice = input(
            "1: show all users\n2: reset csv file\n0: exit\n"
        )
        if choice == "1":
            print("show_all_users")
        elif choice == "2":
            print("reset csv file")
        elif choice == "0":
            print("Exited from admin-mode...")
            break
        else:
            print("please retry to select.")


def signup():
    """
    superuser=FalseのUserを作ることができる関数。
    """
    username, email, password = receive_inputs()
    user = User.new_user(username, email, password, str_now())
    user.create_user()
    print("--Your info--")
    for k, v in user.info().items():
        print(k, v, sep=": ", end=", ")
    print("\n-----")
    print("Pretend to signup successfully!")
