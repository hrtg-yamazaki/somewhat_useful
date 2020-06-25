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


def debug():
    """
    デバッグ用の関数。
    個別の関数を呼び出し、正常に動いているかを確かめるのに使う。
    """
    print(general.next_id("csv/users.csv"))


def main(func):
    """
    このプログラムの実行関数。
    コマンドライン引数を受け取って、起動する関数を振り分ける。
    """
    if func == "createsuperuser":
        pretend.createsuperuser()
    elif func == "runserver":
        pretend.runserver()
    elif func == "debug":
        debug()
    else:
        default_message()


if __name__ == "__main__":

    parser = argparse.ArgumentParser(description="pretend \"createsuperuser\"")
    parser.add_argument(
        "function", default="default", nargs="?",
        choices=["default", "createsuperuser", "runserver", "debug"],
        help="利用機能の選択。 createsuperuser / runserver"
    )
    args = parser.parse_args()

    try:
        main(args.function)
    except KeyboardInterrupt:
        print("\nOperation cancelled.")
