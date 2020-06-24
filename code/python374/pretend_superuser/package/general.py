import os
from pathlib import Path
from datetime import datetime


os.chdir(Path(__file__).parent.parent)


USERS_CSV_PATH = "csv/users.csv"


def receive_input(message, test_value=""):
    """
    標準入力を受け取り返す関数。
    テスト用に引数test_valueを指定でき、指定があった場合は
    標準入力を飛ばしてその値をそのまま返す。
    """
    if len(test_value) == 0:
        input_value = input(message)
        return input_value
    else:
        return test_value


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


def length_check(default, comparison):
    """
    intで与えられた引数２つを比較し、文字長の大きい方を返す関数
    """
    if default < comparison:
        default = comparison
    return default


def adjust_width(lst, width_list):
    """
    引数lstで受け取ったリストの横幅を、
    対応するwidth_listの値に合わせてスペースを追加し調整する関数。
    """
    result = []
    for line in lst:
        for i in range(len(line)):
            if len(line[i]) < width_list[i]:
                dif = width_list[i] - len(line[i])
                if line[i] == "-":
                    line[i] = "-" * dif + line[i] 
                else:
                    line[i] = " " * dif + line[i]
        result.append("| " + " | ".join(line) + " |")
    return result


def translate_bool(string):
    """
    文字列のTrue/Falseをboolに変換する関数。
    """
    if string == "True":
        return True
    else:
        return False