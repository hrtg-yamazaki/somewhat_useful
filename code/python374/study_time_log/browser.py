from browser_module import select_month, total_data


border = "- - - - - - - - - -"


def browse():

    # ファイルがなければ作成しておく
    with open("log/months_data.log", "a", encoding="UTF-8"):
        pass

    while True:
        print("希望する操作を選択してください")
        choice = input("1: 月ごとの学習時間を確認\n2: 累計学習時間を確認\n0: 閲覧を終了する\n")
        if choice == "1":
            print(border)
            select_month()
        elif choice == "2":
            print(border)
            total_data()
        elif choice == "0":
            print("閲覧モードを終了します")
            break
        else:
            print("無効な値が入力されました")
            print("操作をやり直してください")
            print(border)
