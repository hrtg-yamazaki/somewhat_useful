from datetime import datetime


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
