import argparse
import os
from pathlib import Path

from package import pretend
from package.user import USERS_CSV_PATH


os.chdir(Path(__file__).parent)


def createsuperuser():
    """
    このプログラムで動かしたいメインの関数。
    現在開発中・・・・
    """
    pretend.createsuperuser()


def default_message():
    """
    コマンドライン引数が何も受け取らなかった時に起動する関数。
    メッセージを表示してプログラムを終了する。
    """
    print("Please execute this with the command \"pretendsuperuser\"!")


def set_users_csv():
    """
    users.csvファイルがなければ作成しておくための関数。
    """
    with open(USERS_CSV_PATH, "a", encoding="utf-8") as f:
      pass


def main(func):
    """
    このプログラムの実行関数。
    コマンドライン引数を受け取って、起動する関数を振り分ける。
    """
    set_users_csv()
    if func == "createsuperuser":
        createsuperuser()
    else:
        default_message()


if __name__ == "__main__":

    parser = argparse.ArgumentParser(description="pretend \"createsuperuser\"")
    parser.add_argument(
        "function", default="default", nargs="?", choices=["default", "createsuperuser"],
        help="利用機能の選択。 exec / createsuperuser "
    )
    args = parser.parse_args()

    try:
        main(args.function)
    except KeyboardInterrupt:
        print("\nOperation cancelled.")
