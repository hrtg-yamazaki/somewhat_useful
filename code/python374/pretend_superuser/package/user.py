import re
import csv
from datetime import datetime
from .general import USERS_CSV_PATH, next_id, length_check


USERNAME_REGEX = r"^[a-zA-Z0-9-_]{4,30}$"
EMAIL_REGEX = r"^[a-zA-Z0-9-_.]{1,30}@[a-zA-Z0-9.]{1,20}.[a-zA-Z0-9]{2,10}$"
PASSWORD_REGEX = r"^[a-zA-Z0-9]{8,128}$"
COMMON_WORDS_REGEX = r"test|password|user|abcd|12345678"


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
        output = []  # 表示用データのリスト

        header = User.column_list
        output.append(header)
        column_width_list = [ len(header[i]) for i in range(len(header)) ]
        borders = [ "-" for _ in range(len(header)) ]  # カラムの数だけボーダーを用意
        output.append(borders)
        for user in self.users:
            data = user.data()
            output.append(data)
            # カラム別最大長の確認と更新
            for i in range(4):
                column_width_list[i] = length_check(column_width_list[i], len(data[i]))
        # created_atとsuperuserは固定長
        column_width_list[4] = 19
        column_width_list[5] = 9
        output.append(borders)

        result = []
        for line in output:
            for i in range(len(line)):
                if len(line[i]) < column_width_list[i]:
                    dif = column_width_list[i] - len(line[i])
                    if line[i] == "-":
                        line[i] = "-" * dif + line[i] 
                    else:
                        line[i] = " " * dif + line[i]
            result.append("| " + " | ".join(line) + " |\n")

        return result

class User:

    column_list = ["id", "username", "email", "password", "created_at", "superuser"]

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



class Validator():
    # Validatorを汎用クラス化できないか考える => 出来そうならここをUserValidator(Validator)に
    """
    バリデーションメソッドをまとめて管理するためのクラス。
    フォーマット確認用の正規表現は、ファイル冒頭でまとめて定義。
    REGEXにマッチすればそのまま返し、マッチしなければもう一度入力を促しつつ再帰。
    """
    def username_is_valid(self, username):
        """
        User.usernameのバリデーション。
        """
        if not bool(re.match(USERNAME_REGEX, username)):
            print(self.username_error(username))
            return False
        return True
    
    def username_error(self, username):
        """
        User.usernameのバリデーションメッセージを返す関数。
        """
        if len(username) < 4:
            message = "This username is too short. 4 characters min."
        elif len(username) > 30:
            message = "This username is too long. 30 characters max."
        else:
            message = "Enter a valid username."
        return message

    def email_is_valid(self, email):
        """
        User.emailのバリデーション。
        """
        if not bool(re.match(EMAIL_REGEX, email)):
            print(self.email_error(email))
            return False
        return True

    def email_error(self, email):
        """
        User.emailのバリデーションメッセージを返す関数。
        """
        message = "Enter a valid email address."
        return message

    def password_is_valid(self, password, password_conf):
        """
        User.passwordのバリデーション。
        """
        # 確認用パスワードの入力と一致確認
        if password != password_conf:
            print(self.not_match_error())
            return False
        # 正規表現によるバリデーション
        if not bool(re.match(PASSWORD_REGEX, password)) or\
                bool(re.search(COMMON_WORDS_REGEX, password)):
            print(self.password_error(password))
            return False
        return True

    def not_match_error(self):
        """
        passwordとpassword_confの不一致時のエラーメッセージを返す関数
        """
        message = "Your password didn\'t match."
        return message

    def password_error(self, password):
        """
        User.passwordのバリデーションメッセージを返す関数
        """
        if len(password) < 8:
            message = "This password is too short. 8 characters min."
        elif len(password) > 128:
            message = "This password is too long. 128 characters max."
        elif bool(re.search(COMMON_WORDS_REGEX, password)):
            message = "This password is too common."
        else:
            message = "Enter a valid password."
        return message
  