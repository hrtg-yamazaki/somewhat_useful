from calculator import message, answer

print(message())

input_line = input().split(" ")
a = input_line[0]
op = input_line[1]
b = input_line[2]
eq = input_line[3]
c = input_line[4]

x = answer(a, op, b, eq, c)

print("x の値は " + str(x) + " です")
