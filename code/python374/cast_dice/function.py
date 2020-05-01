from random import randint
from time import sleep


def print_dice(dice):

    print("\n_ " + str(dice[1]) + " _ _")
    print(str(dice[2]) + " " + str(dice[0]) + " " + str(dice[3]) + " " + str(dice[5]))
    print("_ " + str(dice[4]) + " _ _\n")


def select_power(power):

    if power == "0":
        N = randint(1, 3)
        print("弱く弾きました")
    elif power == "1":
        N = randint(4, 66)
        print("強く弾きました")
    else:
        N = randint(1, 66)
        print("適当に弾きました")

    return N


def please_wait():

    sleep(1)
    print("\n(転がっています....)")
    sleep(3)


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


def stop_motion(direction, dice):

    N = 1
    for t in range(3):
        t = (t + 1) * 0.8
        sleep(t)
        print("---")
        the_die_is_cast(N, direction, dice)
        print_dice(dice)

    sleep(3)
    print("...どうやら止まったようです。")
