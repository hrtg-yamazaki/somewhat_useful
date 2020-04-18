def calculate(a, b, price):
    p_a = int(price * (1 + a / 100))
    p_b = int(price * (1 + b / 100))
    result = p_b - p_a
    print(str(a) + "% の場合、税込価格は " + str(p_a) + " です")
    print(str(b) + "% の場合、税込価格は " + str(p_b) + " です")
    print("よって、差額は " + str(result) + " 円です")
