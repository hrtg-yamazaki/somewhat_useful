print("税率の変更に伴う支払額の増減分を算出します")

a = int(input("変更前の税率を入力してください\n"))
b = int(input("変更後の税率を入力してください\n"))
price = int(input("商品の価格を入力して下さい\n"))

from function import calculate
calculate(a, b, price)

while True:
    print("--------------------")
    print("希望する操作を選択して下さい")
    choice = input("1: 商品価格を再入力し結果を出力する\n0: アプリケーションを終了する\n")
    if choice == "1":
        price = int(input("商品の価格を入力して下さい"))
        calculate(a, b, price)
    elif choice == "0":
        print("アプリケーションを終了します")
        break
    else:
        print("無効な値が入力されました\n最初からやり直して下さい")
