from datetime import datetime


def registration():

    now = datetime.now()
    str_now = now.strftime("%Y/%m/%d")
    this_month = now.strftime("%Y_%m")
    today = now.strftime("%d")

    # ファイルがなければ作成しておく
    with open("log/monthes_data.log", "a", encoding="UTF-8") as f:
        pass
    with open("log/" + this_month + ".log", "a", encoding="UTF-8") as f:
        pass

    # 当月の登録があるかどうかの確認
    registed_month = False
    with open("log/monthes_data.log", "r") as f:
        for row in f:
            month = row.rstrip()
            if this_month == month:
                registed_month = True

    # 当月のデータがなければ、登録する(このデータは閲覧時に選択肢として利用する)
    if registed_month == False:
        with open("log/monthes_data.log", "a", encoding="UTF-8") as f:
            f.write(this_month + "\n")

    # 当日のデータがあるかどうか確認
    registed_today = False
    with open("log/" + this_month + ".log", "r") as f:
        for row in f:
            line = row.rstrip().split(" , ")
            if line[0] == today:
              registed_today = True
              study_minutes = line[1]

    # 勉強時間の記録(月ごとにログを管理)
    if registed_today == False:
        study_minutes = input("今日は何時間勉強しましたか？分単位で半角数字で入力してください\n")
        with open("log/" + this_month + ".log", "a", encoding="UTF-8") as f:
            f.write(today + " , " + study_minutes + "\n")
        print("登録が完了しました")
    else:
        print("本日の登録は終了しています")

    # 登録内容の表示
    hour = int(study_minutes) // 60
    if hour != 0:
        minutes = int(study_minutes) % (hour * 60)
    else:
        minutes = int(study_minutes)
    print("( ", str_now, " の学習時間： ", hour, " h ", minutes, " m )", sep="")