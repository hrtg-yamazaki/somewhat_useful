
border = "--------------------"


def regist_columns(c_list):

    print("登録したいカラム名を入力してください")
    print("(入力なしのままEnterキーを押すことで、登録を終了することができます)")
    index = 0
    c_list.append("id")
    while True:
        index = index + 1
        column = input("(" + str(index) + ") ")
        if len(column) != 0:
            c_list.append(column)
        else:
            break


def regist_records(c_list, width, line_list, length_list):

    index = 0
    choice = "1"
    while True:
        index = index + 1
        if choice == "1":
            print(border)
            print("レコードの登録(" + str(index) + ")")
            line = []
            line_length = []
            line.append(str(index))
            line_length.append(len(str(index)))
            for i in range(1, width):
                c = c_list[i]
                value = input(c + "： ")
                line.append(value)
                line_length.append(len(value))
            line_list.append(line)
            length_list.append(line_length)
            # 次も登録を継続するかどうかの確認
            print(border)
            choice = input("1:レコードを登録を継続する\n0:登録を終了しテーブルを表示する\n")
        else:
            break


def adjust_width(width, height, length_list, column_width, c_list):

    for k in range(width):
        column_list = []
        for l in range(height):
            count = length_list[l][k]
            column_list.append(count)
        column_width.append(max(column_list))

    for i in range(width):
        if len(c_list[i]) < column_width[i]:
            space = " " * (column_width[i] - len(c_list[i]))
            c_list[i] = c_list[i] + space
        else:
            column_width[i] = len(c_list[i])


def make_border(width, column_width, border_list):

    for i in range(width):
        border = ("-" * (column_width[i] + 2))
        border_list.append(border)


def generate_table(c_list, border_list, line_list, width, column_width):

    print(border)
    print("入力されたデータを元に作成されたテーブルを表示します\n")
    print("| " + " | ".join(c_list) + " |")
    print("|" + "|".join(border_list) + "|")

    for l in line_list:
        for i in range(width):
            if len(l[i]) != column_width[i]:
                space = " " * (column_width[i] - len(l[i]))
                l[i] = l[i] + space
                
        print("| " + " | ".join(l) + " |")

    print("|" + "|".join(border_list) + "|")
    print("")
