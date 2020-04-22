from corrector import fix_minutes, fix_hour

print("存在しない超過した数値を繰り上げ、時刻を修正します")

print("全て2桁の半角数字で入力して下さい\n(例：1月の場合 => 01)")
MM = input("月を入力して下さい\n")
dd = input("日を入力して下さい\n")
hh = input("時を入力して下さい\n")
mm = input("分を入力して下さい\n")

time = MM + "/" + dd + " " + hh + ":" + mm

time_list = list(time)
month = int(time[0:2])
day = int(time[3:5])
hour = int(time[6:8])
minute = int(time[9:11])

if (minute >= 60) or (hour >= 24):

    if minute >= 60:
        time = fix_minutes(time)

    hour = int(time[6:8])
    if hour >= 24:
        time = fix_hour(time)

    print(time)
    print("時刻を修正しました")
else:
    print(time)
    print("入力された時刻に修正点はありません")
