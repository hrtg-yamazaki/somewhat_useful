def message():

    s_1 = "簡単な方程式の解を算出します\n方程式を入力してください\n"
    s_2 = "フォーマットは以下の通りです：\n例１： 5 + 5 = x\n例２： 5 - x = 5\n例３： x × 5 = 5\n例４： x ÷ 5 = 5"
    return s_1 + s_2


def answer(a, op, b, eq, c):

    if a == "x":
        b = int(b)
        c = int(c)
        if op == "+":
            answer = c - b
        elif op == "-":
            answer = c + b
        elif op == "×":
            answer = c / b
        else:
            answer = c * b
    elif b == "x":
        a = int(a)
        c = int(c)
        if op == "+":
            answer = c - a
        elif op == "-":
            answer = c + a
        elif op == "×":
            answer = c / a
        else:
            answer = c * a
    else:
        a = int(a)
        b = int(b)
        if op == "+":
            answer = a + b
        elif op == "-":
            answer = a - b
        elif op == "×":
            answer = a * b
        else:
            answer = a / b

    return int(answer)
