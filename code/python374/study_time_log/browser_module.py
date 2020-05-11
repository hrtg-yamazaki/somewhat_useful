from datetime import datetime


border = "- - - - -"


def print_time(study_time, beginning):

    # 分単位で与えられた入力を表示用フォーマットに変換
    hour = study_time // 60
    if hour != 0:
        minutes = study_time % (hour * 60)
    else:
        minutes = study_time
        
    print(beginning, hour, " h ", minutes, " m ", sep="")


def monthly_data(month):
    
    print("[ ", month, " のデータ ]", sep="")

    # 日別のデータを表示した上で、日別の学習時間をリストに格納
    study_time_list = []
    with open("log/" + month + ".log", "r", encoding="UTF-8") as f:
        for row in f:
            line = row.rstrip().split(" , ")
            beginning = " " + line[0] + "日 : " # 表示文の冒頭
            print_time(int(line[1]), beginning)
            study_time_list.append(int(line[1]))

    # 月の総学習時間を表示
    total = sum(study_time_list)
    beginning = " [ " + month + " ] 学習時間の合計 : " # 表示文の冒頭
    print_time(total, beginning)


def select_month():
    
    print("データを閲覧したい月を選択してください")

    # 記録がある月をリストに格納
    months_list = []
    with open("log/months_data.log", "r", encoding="UTF-8") as f:
        for row in f:
            month = row.rstrip()
            months_list.append(month)

    # 選択出来る月を表示し、インデックス番号をリストに格納
    index_list = []
    for i in range(len(months_list)):
        line = months_list[i].split("_")
        i = i + 1
        print(i, ": ", line[0], "年 ", line[1], "月", sep="")
        index_list.append(str(i))

    # 月の選択
    if len(index_list) >= 1:
        choice = input("0: 閲覧モードのはじめに戻る\n")
        print(border)
        if choice in index_list:
            selected_month = months_list[int(choice) - 1]
            monthly_data(selected_month)
            print(border)
        elif choice == "0":
            print("１つ前の操作に戻ります")
            print(border)
        else:
            print("無効な値が入力されました")
            print("操作をやり直してください")
    else:
        print("( 登録されているデータはありませんでした )")
        print("１つ前の操作に戻ります")
        print(border)


def total_data():

    # 記録がある月をリストに格納
    months_list = []
    with open("log/months_data.log", "r", encoding="UTF-8") as f:
        for row in f:
            month = row.rstrip()
            months_list.append(month)

    # 記録がある月とそれぞれの累計実績を、辞書に格納
    months_dict = {}
    for month in months_list:
        time_list = [] # 実績計算用のリスト
        with open("log/" + month + ".log", "r", encoding="UTF-8") as f:
            for row in f:
                line = row.rstrip().split(" , ")
                time = int(line[1])
                time_list.append(time)
        monthly_dict = {month: sum(time_list)}
        months_dict.update(monthly_dict)

    # それぞれの月の実績を一覧表示
    for month, time in months_dict.items():
        line = month.split("_")
        beginning = " " + line[0] + "年" + line[1] + "月: "
        print_time(time, beginning)

    # 総学習時間を表示
    total = sum(months_dict.values())
    beginning = "あなたの累計学習時間： "
    print(border + "\n")
    print_time(total, beginning)
    print("\nこれからも頑張っていきましょう！\n\n" + border)
