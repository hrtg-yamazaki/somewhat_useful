from random import randint


def print_dice(dice):

    print("_ " + str(dice[1]) + " _ _")
    print(str(dice[2]) + " " + str(dice[0]) + " " + str(dice[3]) + " " + str(dice[5]))
    print("_ " + str(dice[4]) + " _ _")


def select_power(power):

    if power == "0":
        N = randint(1, 3)
    elif power == "1":
        N = randint(4, 66)
    else:
        N = randint(1, 66)

    return N


def the_die_is_cast(N, direction, dice):

    for _ in range(N):
        num = randint(0, 3)
        dir = direction[num]
        if dir == "U":
            temp = dice[0]
            dice[0] = dice[4]
            dice[4] = dice[5]
            dice[5] = dice[1]
            dice[1] = temp
        elif dir == "L":
            temp = dice[0]
            dice[0] = dice[3]
            dice[3] = dice[5]
            dice[5] = dice[2]
            dice[2] = temp
        elif dir == "R":
            temp = dice[0]
            dice[0] = dice[2]
            dice[2] = dice[5]
            dice[5] = dice[3]
            dice[3] = temp
        else:
            temp = dice[0]
            dice[0] = dice[1]
            dice[1] = dice[5]
            dice[5] = dice[4]
            dice[4] = temp

