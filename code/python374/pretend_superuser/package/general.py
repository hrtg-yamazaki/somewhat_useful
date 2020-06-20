import os
from pathlib import Path
from datetime import datetime


os.chdir(Path(__file__).parent.parent)


USERS_CSV_PATH = "csv/users.csv"


def str_now():
    """
    現在時刻を表示用フォーマットの文字列に変換して返す関数
    """
    return datetime.now().strftime("%Y/%m/%d_%H:%M:%S")


def set_users_csv():
    """
    users.csvファイルがなければ作成しておくための関数。
    """
    with open(USERS_CSV_PATH, "a", encoding="utf-8"):
        pass


def next_id(path):
    """
    csvファイルの行数を数え、0なら1を返す。
    0でなければ、最終行のレコードのid + 1 を返す。
    """
    with open(path, "r", encoding="utf-8") as f:
        count = 0
        for row in f:
            count += 1
    if count == 0:
        id = count + 1
    else:
        id = int(row.rstrip().split(",")[0]) + 1
    return id
