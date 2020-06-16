import argparse
import os
from pathlib import Path

from package import pretend


os.chdir(Path(__file__).parent)


def pretend_superuser():
    """
    このプログラムで動かしたいメインの関数。
    現在開発中・・・・
    """
    pretend.main()


def default_message():
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
    if func == "pretendsuperuser":
        pretend_superuser()
    else:
        default_message()


if __name__ == "__main__":

    parser = argparse.ArgumentParser(description="pretend \"createsuperuser\"")
    parser.add_argument(
        "function", default="default", nargs="?", choices=["default", "pretendsuperuser"],
        help="利用機能の選択。 exec / pretendsuperuser "
    )
    args = parser.parse_args()

    main(args.function)
