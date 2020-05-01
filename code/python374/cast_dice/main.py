print("サイコロを転がしてみよう!")

from function import print_dice, select_power, please_wait, the_die_is_cast, stop_motion

dice = [1, 2, 3, 4, 5, 6]
direction = ["U", "L", "R", "D"]

print("現在のサイコロの状態(展開図・中心左が上向き)：")
print_dice(dice)

print("どれくらいの強さで転がしますか？")
power = input("0:弱く弾く\n1:強く弾く\n(それ以外の入力の場合は適当に弾きます)\n")

N = select_power(power)

please_wait()

the_die_is_cast(N, direction, dice)

stop_motion(direction, dice)

print("転がった結果、サイコロは以下の状態で停止しました")
print_dice(dice)
