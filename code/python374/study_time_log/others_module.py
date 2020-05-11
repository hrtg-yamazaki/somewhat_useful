import os
import shutil

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
    pass
