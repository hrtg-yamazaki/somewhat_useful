from calculator import message, answer

border = "--------------------"

while True:
    print(border)
    print(message())
    print(border)
    input_line = input().split(" ")
    
    if len(input_line) == 5:
        a = input_line[0]
        op = input_line[1]
        b = input_line[2]
        eq = input_line[3]
        c = input_line[4]

        if op == "+" or "-" or "×" or "÷":
            if eq == "=":
                x = answer(a, op, b, eq, c)
                print("x の値は " + str(x) + " です")
                choice = input("プログラムを終了しますか？(y/n)\n")
                if choice == "y":
                    print("終了します")
                    break
                else:
                    print("もう一度起動します")
            else:
                print("無効なフォーマットで入力されました\n最初からやり直してください")
        else:
          print("無効な演算子が入力されました\n最初からやり直してください")
    else:
      print("無効なフォーマットで入力されました\n最初からやり直してください")
