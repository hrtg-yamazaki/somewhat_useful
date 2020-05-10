from datetime import datetime
from register import registration


print("勉強時間を記録するプログラムです")

while True:
    choice = input("1: データを登録する\n2: データを確認する\n0: アプリケーションを終了する\n")
    if choice == "1":
        print("データを登録する")
        registration()
    elif choice == "2":
        print("データを閲覧する(開発中)")
    elif choice == "0":
        print("アプリケーションを終了します")
        break
    else:
        print("無効な値が入力されました")
        print("操作をやり直してください")
