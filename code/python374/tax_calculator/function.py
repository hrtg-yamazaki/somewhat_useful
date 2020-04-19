
def calculate(a, b):
    price = int(input("商品の価格を入力して下さい\n"))
    p_a = int(price * (1 + a / 100))
    p_b = int(price * (1 + b / 100))
    result = p_b - p_a
    print(str(a) + "% の場合、税込価格は " + str(p_a) + " です")
    print(str(b) + "% の場合、税込価格は " + str(p_b) + " です")
    print("よって、差額は " + str(result) + " 円です")


def setting_rate():
    a = int(input("増税前の税率を入力してください\n"))
    b = int(input("増税後の税率を入力してください\n"))

    return a, b