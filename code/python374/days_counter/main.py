print("１つめの入力からみて、２つめの日付が何日後なのかを判定します")

print("１つめの日付は・・・")
y = int(input("何年？"))
m = int(input("何月？"))
d = int(input("何日？"))
first = "１つめの入力： " + str(y) + " / " + str(m) + " / " + str(d)
print(first)

print("２つめの日付は・・・？")
y_2 = int(input("何年？"))
m_2 = int(input("何月？"))
d_2 = int(input("何日？"))
second = "２つめの入力： " + str(y_2) + " / " + str(m_2) + " / " + str(d_2)
print(second)

count = 0
while (y != y_2) or (m != m_2) or (d != d_2):
    d = d + 1
    if m == 1 or m == 3 or m == 5 or m == 7 or m == 8 or m == 10 or m == 12:
        if d > 31:
            m = m + 1
            d = d - 31
            if m > 12:
                y = y + 1
                m = m - 12
    elif m == 4 or m == 6 or m == 9 or m == 11:
        if d > 30:
            m = m + 1
            d = d - 30
    elif (m == 2) and ((y % 4) == 0) and (((y % 100) != 0) or (y % 400 == 0)):
      if d > 29:
          m = m + 1
          d = d - 29
    else:
        if d > 28:
            m = m + 1
            d = d - 28
    count = count + 1

print(first + "から数えて" + second + " は " + str(count) + " 日後です")
