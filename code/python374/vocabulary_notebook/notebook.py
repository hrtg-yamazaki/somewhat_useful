border = "--------------------"

class Notebook:

    def __init__(self):

        self.word_dict = {}


    def regist(self):

        word = input("登録したい単語、文字列を入力してください\n")
        mean = input("入力した単語の意味、説明を入力してください\n")
        self.word_dict.update({word: mean})
        print("新たに [ " + word + " ] が登録されました")


    def search(self):

        dicts = {}
        keyword = input("キーワードを入力してください\n")
        for key in self.word_dict:
            if keyword in key:
                d = {key: self.word_dict[key]}
                dicts.update(d)

        print(border)
        print("【検索結果一覧】")
        for key in dicts:
            print("・" + key + "\n意味： " + dicts[key])
