from .pretend_func import receive_inputs
from .general import str_now
from .user import User, Users


def createsuperuser():
    """
    コマンドライン引数に createsuperuser を受け取った場合の実行関数。
    現在開発中...
    """
    username, email, password = receive_inputs()
    user = User.new_user(username, email, password, str_now())
    user.create_user()
    print("Pretend to create superuser successfully.")


def runserver():
    """
    コマンドライン引数に runserver を受け取った場合の実行関数。
    未実装。
    """
    # adminとuser(su=False)の機能をここにつける
    # 他にも startapp あたりのレスキューを後々作っておきたい
    print("Now developing.....")

    users = Users()
    users.read_users()
    user = users.latest_user()
    print(user.data())
