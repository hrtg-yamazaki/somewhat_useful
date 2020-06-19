from datetime import datetime


def str_now():
    """
    現在時刻を表示用フォーマットの文字列に変換して返す関数
    """
    return datetime.now().strftime("%Y/%m/%d_%H:%M:%S")
