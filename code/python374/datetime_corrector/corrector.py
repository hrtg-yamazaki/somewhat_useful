
def fix_length(target, item, time_list):
    if target == "minute":
        i = 9
    elif target == "hour":
        i = 6

    if item < 10:
        time_list[i:(i + 2)] = "0" + str(item)
    else:
        time_list[i:(i + 2)] = str(item)

    return time_list


def fix_minutes(time):

    time_list = list(time)
    hour = int(time[6:8])
    minute = int(time[9:11])
    hour = hour + 1
    minute = minute - 60

    time_list = fix_length("hour", hour, time_list)
    time_list = fix_length("minute", minute, time_list)

    time = "".join(time_list)

    return time
