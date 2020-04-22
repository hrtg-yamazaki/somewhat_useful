
def update_timelist(target, item, time_list):

    if target == "minute":
        i = 9
    elif target == "hour":
        i = 6
    elif target == "day":
        i = 3
    elif target == "month":
        i = 0

    if item < 10:
        time_list[i:(i + 2)] = "0" + str(item)
    else:
        time_list[i:(i + 2)] = str(item)

    return time_list


def last_day_of_month(month):

    if month == (4 or 6 or 9 or 11):
        last_day = 30
    elif month == 2:
        leap = 0
        while (leap != "y") and (leap != "n"):
            print("閏年を想定していますか？")
            leap = input("(y / n)\n")
            if leap == "y":
                last_day = 29
            elif leap == "n":
                last_day = 28
            else:
                print("無効な値が入力されました\n y か n を入力して下さい")
    else:
        last_day = 31

    return last_day


def fix_minutes(time):

    time_list = list(time)
    minute = int(time[9:11])
    minute = minute - 60
    hour = int(time[6:8])
    hour = hour + 1

    time_list = update_timelist("minute", minute, time_list)
    time_list = update_timelist("hour", hour, time_list)

    time = "".join(time_list)

    return time


def fix_hour(time):

    time_list = list(time)
    hour = int(time[6:8])
    hour = hour - 24
    day = int(time[3:5])
    day = day + 1

    time_list = update_timelist("hour", hour, time_list)
    time_list = update_timelist("day", day, time_list)

    time = "".join(time_list)

    return time


def fix_day(time, last_day):

    time_list = list(time)
    day = int(time[3:5])
    day = day - last_day
    month = int(time[0:2])
    month = month + 1

    time_list = update_timelist("day", day, time_list)
    time_list = update_timelist("month", month, time_list)

    time = "".join(time_list)

    return time
