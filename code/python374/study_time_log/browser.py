from browser_module import select_month


border = "- - - - - - - - - -"

def browse():

    # ファイルがなければ作成しておく
    with open("log/monthes_data.log", "a", encoding="UTF-8"):
        pass

    while True:
        print("希望する操作を選択してください")
        choice = input("1: 月あたりの学習時間を確認\n0: 閲覧を終了する\n")
        if choice == "1":
            print(border)
            select_month()
        elif choice == "0":
            print("閲覧モードを終了します")
            break
        else:
            print("無効な値が入力されました")
            print("操作をやり直してください")
            print(border)
