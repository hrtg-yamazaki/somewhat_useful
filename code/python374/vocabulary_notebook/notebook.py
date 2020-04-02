class Notebook:

    def __init__(self):
        self.str_list = []

    def regist(self):
        string = input("任意の文字列を入力してください\n")
        self.str_list.append(string)
        print("新たに [" + string + "] が登録されました")

    def search(self):
        searched = []
        keyword = input("キーワードを入力してください\n")
        for string in self.str_list:
            if keyword in string:
                searched.append(string)
        print(keyword + " を含む文字列は以下の通りです\n" + "\n".join(searched))
