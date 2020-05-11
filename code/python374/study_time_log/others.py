import os
import shutil


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


def other_operations():

    print("[[ その他の操作 ]]" + border)
    while True:
        print("希望する操作を選択してください")
        choice = input("1: データをリセットする\n0: 最初の画面に戻る\n")
        if choice == "1":
            reset_logs()
            print(border)
        elif choice == "0":
            print("最初の画面に戻ります")
            break
        else:
            print("無効な値が入力されました")
            print("操作をやり直してください")
            print(border)