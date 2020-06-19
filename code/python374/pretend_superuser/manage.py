import argparse
import os
from pathlib import Path

from package import pretend, user, general


os.chdir(Path(__file__).parent)


def default_message():
    """
    コマンドライン引数が何も受け取らなかった時に起動する関数。
    メッセージを表示してプログラムを終了する。
    """
    print("Please execute this with the command \"createsuperuser\"!")


def main(func):
    """
    このプログラムの実行関数。
    コマンドライン引数を受け取って、起動する関数を振り分ける。
    """
    general.set_users_csv()
    if func == "createsuperuser":
        pretend.createsuperuser()
    elif func == "runserver":
        pretend.runserver()
    else:
        default_message()


if __name__ == "__main__":

    parser = argparse.ArgumentParser(description="pretend \"createsuperuser\"")
    parser.add_argument(
        "function", default="default", nargs="?",
        choices=["default", "createsuperuser", "runserver"],
        help="利用機能の選択。 createsuperuser / runserver"
    )
    args = parser.parse_args()

    try:
        main(args.function)
    except KeyboardInterrupt:
        print("\nOperation cancelled.")
