import os
from pathlib import Path
import argparse


os.chdir(Path(__file__).parent)


def pretend_superuser():
    """
    このプログラムで動かしたいメインの関数。
    現在開発中・・・・
    """
    print("Now developing....")


def exec():
    """
    コマンドライン引数が何も受け取らなかった時に起動する関数。
    メッセージを表示してプログラムを終了する。
    """
    print("Please execute this with the command \"pretendsuperuser\"!")


def main(func):
    """
    このプログラムの実行関数。
    コマンドライン引数を受け取って、起動する関数を振り分ける。
    """
    if func == "exec":
        exec()
    elif func == "pretendsuperuser":
        pretend_superuser()


if __name__ == "__main__":

    parser = argparse.ArgumentParser(description="pretend \"createsuperuser\"")
    parser.add_argument(
        "function", default="exec", nargs="?", choices=["exec", "pretendsuperuser"],
        help="利用機能の選択。 exec / pretendsuperuser "
    )
    args = parser.parse_args()

    main(args.function)