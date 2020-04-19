from function import calculate, setting_rate

print("税率の変更に伴う支払額の増減分を算出します")

a, b = setting_rate()

calculate(a, b)

while True:
    print("--------------------")
    print("希望する操作を選択して下さい")
    choice = input("1: 商品価格を再入力し結果を出力する\n2: 税率の設定を変更する\n0: アプリケーションを終了する\n")
    if choice == "1":
        calculate(a, b)
    elif choice == "2":
        a, b = setting_rate()
    elif choice == "0":
        print("アプリケーションを終了します")
        break
    else:
        print("無効な値が入力されました\n最初からやり直して下さい")
