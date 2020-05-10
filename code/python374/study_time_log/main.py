from datetime import datetime
from register import registration
from browser import browse


border = "---------------------"

print(border)
print("[[ 勉強時間を記録するプログラム ]]")

while True:
    print(border)
    choice = input("1: データを登録する\n2: データを確認する\n0: アプリケーションを終了する\n")
    if choice == "1":
        print("データを登録する")
        print(border)
        registration()
    elif choice == "2":
        print("データを閲覧する")
        print(border)
        browse()
    elif choice == "0":
        print("アプリケーションを終了します")
        break
    else:
        print("無効な値が入力されました")
        print("操作をやり直してください")
