from simulator import border, regist_columns, regist_records, adjust_width, make_border, generate_table


print(border)
print("DBのテーブルを作成します")
print(border)

c_list = []
regist_columns(c_list)

print(border)

width = len(c_list)
print(str(width - 1) + "種類のカラム名が登録されました")
print("続いて、レコードを登録します")

line_list = []
length_list = []
regist_records(c_list, width, line_list, length_list)

height = len(line_list)

column_width = []
adjust_width(width, height, length_list, column_width, c_list)

border_list = []
make_border(width, column_width, border_list)

generate_table(c_list, border_list, line_list, width, column_width)
