import os
from pathlib import Path
from package.register import registration
from package.browser import browse
from package.others import other_operations


# どこから起動してもopen関数のパス指定に影響が出ないよう、ディレクトリを切り替えておく
os.chdir(Path(__file__).parent)
# print(os.getcwd())  =>  ~/study_time_log

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
