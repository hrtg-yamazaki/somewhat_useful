from .pretend_func import receive_inputs
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
    # adminとuser(su=False)の機能をここにつける
    # 他にも startapp あたりのレスキューを後々作っておきたい
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
            print("Operation cancelled.")
            break
        else:
            print("please retry to select.")


def admin():
    """
    superuser=Trueのデータでログイン
    Usersのデータの閲覧などができる
    開発中。。。
    """
    print("admin")


def signup():
    """
    superuser=FalseのUserが作れる。
    開発中。。。
    """
    username, email, password = receive_inputs()
    user = User.new_user(username, email, password, str_now())
    user.create_user()
    print("--Your info--")
    for k, v in user.info().items():
        print(k, v, sep=": ")
    print("-----")
    print("Pretend to signup successfully!")
