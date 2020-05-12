from others_module import reset_logs, fix_today_data


border = " * * * * *"


def other_operations():

    print("[[ その他の操作 ]]\n" + border)
    while True:
        print("希望する操作を選択してください")
        choice = input("1: データをリセットする\n2: 本日のデータを修正する\n0: 最初の画面に戻る\n")
        if choice == "1":
            reset_logs()
            print(border)
        elif choice == "2":
            fix_today_data()
            print(border)
        elif choice == "0":
            print("最初の画面に戻ります")
            break
        else:
            print("無効な値が入力されました")
            print("操作をやり直してください")
            print(border)
