from register import registration
from browser import browse
from others import other_operations


border = "---------------------"

print(border)
print("[[ 勉強時間を記録するプログラム ]]")

while True:
    print(border)
    choice = input("1: データを登録する\n2: データを確認する\n3: その他の操作を行う\n0: アプリケーションを終了する\n")
    if choice == "1":
        print(border)
        registration()
    elif choice == "2":
        print(border)
        browse()
    elif choice == "3":
        print(border)
        other_operations()
    elif choice == "0":
        print("アプリケーションを終了します")
        break
    else:
        print("無効な値が入力されました")
        print("操作をやり直してください")
