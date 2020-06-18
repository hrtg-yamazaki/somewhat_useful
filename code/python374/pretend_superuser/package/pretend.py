from .pretend_module import receive_inputs
from .user import User


def createsuperuser():
    """
    コマンドライン引数に createsuperuser を受け取った場合の実行関数。
    現在開発中...
    """
    username, email, password = receive_inputs()
    user = User.new_user(username, email, password)
    print("Pretend to create superuser successfully.")
    print(user.data())


def runserver():
    """
    コマンドライン引数に runserver を受け取った場合の実行関数。
    未実装。
    """
    # adminとuser(su=False)の機能をここにつける
    # 他にも startapp あたりのレスキューを後々作っておきたい
    pass