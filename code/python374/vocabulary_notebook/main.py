
from notebook import Notebook

border = "--------------------"
note = Notebook()

while True:
    print(border)
    print("数字を入力し操作したい項目を選択して下さい")
    choice = int(input
        (border + "\n1: 単語を登録する\n2: 登録した単語をキーワードで検索する\n0: 操作を終了する\n")
    )
    if choice == 1:
        note.regist()
    elif choice == 2:
        if not note.word_dict:
            print(border)
            print("まだ登録がありません")
        else:
            print(border)
            note.search()
    elif choice == 0:
        print("プログラムを終了します")
        break
    else:
        print("無効な値が入力されました")
        print("最初からやり直してください")
