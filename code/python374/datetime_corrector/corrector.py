def fix_minutes(time):

    time_list = list(time)
    hour = int(time[6:8])
    minute = int(time[9:11])
    hour = hour + 1
    minute = minute - 60
    if hour < 10:
        time_list[6:8] = "0" + str(hour)
    else:
        time_list[6:8] = str(hour)
    if minute < 10:
        time_list[9:11] = "0" + str(minute)
    else:
        time_list[9:11] = str(minute)
    time = "".join(time_list)

    return time