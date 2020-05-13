import os
import shutil
from datetime import datetime
from .browser_module import print_time
from .register import registration


border = " * * * * *"


def reset_logs():

    # 全ログデータのリセット
    print("記録された全てのデータをリセットします\n本当によろしいですか？")
    choice = input("よろしければ「yes」と入力してください")
    if choice == "yes":
        shutil.rmtree('log/') # ディレクトリごとファイルを削除
        os.makedirs('log/', exist_ok=True) # 同名ディレクトリをもう一度作成
        with open("log/.keep", "a", encoding="UTF-8"):
            pass # .keepファイルだけ作っておく
        print("リセットが完了しました")
    else:
        print("リセット操作をキャンセルしました")


def fix_today_data():

    now = datetime.now()
    str_now = now.strftime("%Y/%m/%d")
    this_month =  now.strftime("%Y_%m")
    today = now.strftime("%d")

    # 当月用のファイルがなければ、作成しておく
    with open("log/" + this_month + ".log", "a", encoding="UTF-8") as f:
        pass

    # 当月のログの内容を全て読み込み、文字列を一行ずつリストに格納
    row_list = []
    with open("log/" + this_month + ".log", "r", encoding="UTF-8") as f:
        for row in f:
            row_list.append(row)
        
        # 今日の登録の有無を確認(最終行が代入されたままのrowを利用する)
        last_day = row.rstrip().split(" , ")[0]
        if last_day == today:
            # 登録があれば、最終行を削除し、新たな入力を受け取って、最終行に追加
            del row_list[-1]
            study_time = input("今日はどれくらい勉強しましたか？分単位で半角数字で入力してください\n")
            row_list.append(today + " , " + study_time + "\n")
            # ログ全文を書き込み直し、上書き保存
            with open("log/" + this_month + ".log", "w", encoding="UTF-8") as f:
                f.write("".join(row_list))
            # 編集結果の表示
            print(border)
            print("本日のデータを編集しました")
            beginning = str_now + " : "
            print_time(int(study_time), beginning)
        else:
            print("本日はまだ登録がありません")
            registration() # 新規登録操作へ誘導
