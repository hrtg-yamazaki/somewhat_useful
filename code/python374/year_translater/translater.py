class Translater:

    def __init__(self):

        from datetime import datetime
        now = datetime.now().year
        self.era = {"taisho":1912, "showa":1926, "heisei":1989, "reiwa": 2019, "now":now}
        self.era_name = ["明治以前", "大正", "昭和", "平成", "令和"]


    def year_to_jp_era(self):

        year = int(input("西暦年を半角数字で入力してください(例：1990)\n"))
        era = self.era

        if year < era["taisho"]:
            print(str(year) + " 年は、明治以前のため変換未対応です")
        elif year < era["showa"]:
            jp_year = (year + 1) - era["taisho"]
            print(str(year) + " 年は、大正 " + str(jp_year) + " 年です")
        elif year == era["showa"]:
            print(str(year) + " 年は、大正 15 年として始まり、12/25 に昭和に改元しました")
        elif year < era["heisei"]:
            jp_year = (year + 1) - era["showa"]
            print(str(year) + " 年は、昭和 " + str(jp_year) + " 年です")
        elif year == era["heisei"]:
            print(str(year) + " 年は、昭和 64 年として始まり、1/8 に平成に改元しました")
        elif year < era["reiwa"]:
            jp_year = (year + 1) - era["heisei"]
            print(str(year) + " 年は、平成 " + str(jp_year) + " 年です")
        elif year == era["reiwa"]:
            print(str(year) + " 年は、平成 31 年として始まり、5/1 に令和に改元しました")
        elif year <= era["now"]:
            jp_year = (year + 1) - era["reiwa"]
            print(str(year) + " 年は、令和 " + str(jp_year) + " 年です")
        else:
            jp_year = (year + 1) - era["reiwa"]
            print("令和が続いている場合、" + str(year) + "年は、令和 " + str(jp_year) + " 年です")


    def jp_era_to_year(self):

        def result(era_name, jp_year, year):
            return era_name + str(jp_year) + "年は、西暦 " + str(year) + " 年です"

        print("元号を半角数字で選択してください")
        selected_era = int(input("0:明治以前, 1:大正, 2:昭和, 3:平成, 4:令和\n"))
        era_name = self.era_name

        if era_name[selected_era] == "明治以前":
            print("明治以前は変換未対応です")
            return ""

        jp_year = int(input((era_name[selected_era] + "の何年か、数字を入力してください\n")))
        
        if era_name[selected_era] == era_name[1]:
            year = 1912 + (jp_year - 1)
            print(result(era_name[selected_era], jp_year, year))
        elif era_name[selected_era] == era_name[2]:
            year = 1926 + (jp_year - 1)
            print(result(era_name[selected_era], jp_year, year))
        elif era_name[selected_era] == era_name[3]:
            year = 1989 + (jp_year - 1)
            print(result(era_name[selected_era], jp_year, year))
        elif era_name[selected_era] == era_name[4]:
            year = 2019 + (jp_year - 1)
            print(result(era_name[selected_era], jp_year, year))
        else:
            print("無効な値が入力されました")
            self.jp_era_to_year()
