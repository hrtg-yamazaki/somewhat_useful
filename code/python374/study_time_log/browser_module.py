from datetime import datetime


border = "- - - - -"

def monthly_data(month):
    
    print("[ ", month, " のデータ ]", sep="")

    study_time_list = []
    with open("log/" + month + ".log", "r", encoding="UTF-8") as f:
        for row in f:
            line = row.rstrip().split(" , ")
            hour = int(line[1]) // 60
            if hour != 0:
                minutes = int(line[1]) % (hour * 60)
            else:
                minutes = int(line[1])
            print(" ", line[0], "日 ： ", hour, " h ", minutes, " m ", sep="")
            study_time_list.append(int(line[1]))

    total = sum(study_time_list)
    hour = total // 60
    if hour != 0:
        minutes = total % (hour * 60)
    else:
        minutes = total
    print("学習時間の合計は ", hour, " h ", minutes, " m です", sep="")


def select_month():
    
    print("データを閲覧したい月を選択してください")

    # 記録がある月をリストに格納
    monthes_list = []
    with open("log/monthes_data.log", "r") as f:
        for row in f:
            month = row.rstrip()
            monthes_list.append(month)

    # 選択出来る月を表示し、インデックス番号をリストに格納
    index_list = []
    for i in range(len(monthes_list)):
        line = monthes_list[i].split("_")
        i = i + 1
        print(i, ": ", line[0], "年 ", line[1], "月", sep="")
        index_list.append(str(i))

    # 月の選択
    choice = input("0: 閲覧モードのはじめに戻る\n")
    print(border)
    if choice in index_list:
        selected_month = monthes_list[int(choice) - 1]
        monthly_data(selected_month)
    elif choice == "0":
        print("１つ前の操作に戻ります")
    else:
        print("無効な値が入力されました")
        print("操作をやり直してください")
