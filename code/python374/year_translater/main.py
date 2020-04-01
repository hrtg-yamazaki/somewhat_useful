border = "--------------------"

print(border)
print("和暦 <=> 西暦 変換プログラム")

from translater import Translater

while True:
    print(border)
    print("操作したい項目の番号を半角数字で入力してください")
    print(border)
    choice = int(input("0: 西暦を和暦に変換する\n1: 和暦を西暦に変換する\n2: アプリケーションを終了する\n" + border + "\n"))
    if choice == 0:
        print(border)
        Translater().year_to_jp_era()
    elif choice == 1:
        print(border)
        Translater().jp_era_to_year()
    elif choice == 2:
        print(border)
        print("アプリケーションを終了します")
        break
    else:
        print("無効な値が入力されました")
        print("はじめからやり直してください")
