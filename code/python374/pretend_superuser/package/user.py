import os
import csv
from datetime import datetime
from .general import USERS_CSV_PATH, next_id, length_check, adjust_width


class Users:

    def __init__(self):
        self.users = []

    def latest_user(self):
        """
        userクラスの最新のインスタンスを返す関数
        """
        user = self.users[-1]
        return user

    def read_users(self, path):
        """
        user.csvファイルに記録されている全てのUserを、
        インスタンス化したのちにself.usersに格納する関数。
        """
        with open(path, "r", encoding="utf-8") as f:
            next(f) # headerを読み飛ばす
            for row in f:
                columns = row.rstrip().split(",")
                u_id, username, email, password, created_at, superuser = (
                    int(columns[0]), columns[1], columns[2],
                    columns[3], columns[4], columns[5]
                )
                user = User(
                    username, email, password, created_at,
                    u_id=u_id, superuser=superuser
                )
                self.users.append(user)
        return self.users

    def show_all_users(self):
        """
        self.usersを表示用フォーマットに変換して出力する関数。
        """
        # 表示するデータをピックアップし、列ごとのリストに格納
        row_list = self.make_row_list()
        # カラム別最大長の確認と更新
        header = User.field_names
        column_width_list = [ len(header[i]) for i in range(len(header)) ]
        for user in self.users:
            data = user.data()
            for i in range(len(header)):
                column_width_list[i] = length_check(column_width_list[i], len(data[i]))
        # 最大長に合わせて横幅を調整し、文字列化したものを返り値に
        output_list = adjust_width(row_list, column_width_list)
        output_str = "\n".join(output_list)
        return output_str

    def make_row_list(self):
        """
        表示する内容をピックアップし、
        カラム名とボーダーラインを含むリストを返す関数。
        """
        row_list = []
        # 見出し(カラム名)
        row_list.append(User.field_names)
        # カラムの数だけボーダーを用意
        borders = [ "-" for _ in range(len(User.field_names)) ]
        row_list.append(borders)
        # ユーザーのデータを入れる
        for user in self.users:
            row_list.append(user.data())
        # 末尾のボーダーも追加
        row_list.append(borders)
        return row_list

    @staticmethod
    def set_users_csv():
        """
        users.csvファイルがなければ作成しておくための関数。
        """
        target = USERS_CSV_PATH
        with open(target, "a", encoding="utf-8") as f:
            if os.path.getsize(target) == 0:  # headerがなければ書き込み
                f.write(",".join(User.field_names) + "\n")


class User:

    field_names = ["id", "username", "email", "password", "created_at", "superuser"]

    def __init__(
            self, username, email, password, created_at,
            superuser=False, u_id=next_id(USERS_CSV_PATH)
        ):
        self.id = u_id
        self.username = username
        self.email = email
        self.password = password
        self.created_at = created_at
        self.superuser = superuser

    def data(self):
        """
        書き込み用、デバッグ用にインスタンス変数のリストを返す関数。
        """
        return [
            str(self.id), self.username, self.email, self.password,
            self.created_at, str(self.superuser)
        ]

    def info(self):
        """
        出力用に、インスタンス変数の辞書を返す関数。
        """
        field_name = ["id", "username", "email"]
        field_value = [self.id, self.username, self.email]
        info = dict(zip(field_name, field_value))
        return info

    def create_user(self, path):
        """
        Userインスタンスをcsvファイルに書き込み、永続化するための関数。
        """
        with open(path, "a", encoding="utf-8") as f:
            writer = csv.writer(f)
            writer.writerow(self.data())

    @staticmethod
    def new_user(*args, **kwargs):
        """
        Userクラスのインスタンスを作成する関数。
        """
        # セキュリティ？的に問題なければ*args, **kwargsのまま飛ばしたい
        # 他の方法で、「呼び出し元依存の superuser T/F 設定」ができるならあとで修正
        user = User(*args, **kwargs)
        return user
