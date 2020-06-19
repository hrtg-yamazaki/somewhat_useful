import re
import csv
from datetime import datetime
from .general import USERS_CSV_PATH


USERNAME_REGEX = r"^[a-zA-Z0-9-_]{4,30}$"
EMAIL_REGEX = r"^[a-zA-Z0-9-_.]{1,30}@[a-zA-Z0-9.]{1,20}.[a-zA-Z0-9]{2,10}$"
PASSWORD_REGEX = r"^[a-zA-Z0-9]{8,128}$"
COMMON_WORDS_REGEX = r"test|password|user|abcd|12345678"


class Users:

    def __init__(self):
        self.users = []

    def latest_user(self):
        user = self.users[-1]
        return user

    def read_users(self):
        """
        user.csvファイルに記録されている全てのUserを、
        インスタンス化したのちにself.usersに格納する関数。
        """
        with open(USERS_CSV_PATH, "r", encoding="utf-8") as f:
            for row in f:
                columns = row.rstrip().split(",")
                username, email, password, created_at, superuser = (
                    columns[0], columns[1], columns[2], columns[3], columns[4]
                )
                user = User(username, email, password, created_at, superuser)
                self.users.append(user)


class User:
    
    def __init__(self, username, email, password, created_at, superuser=False):
        self.username = username
        self.email = email
        self.password = password
        self.created_at = created_at
        self.superuser = superuser

    def data(self):
        """
        書き込み用、デバッグ用にインスタンス変数のリストを返す関数。
        """
        return [self.username, self.email, self.password, self.created_at, str(self.superuser)]

    def create_user(self):
        """
        Userインスタンスをcsvファイルに書き込み、永続化するための関数。
        """
        with open(USERS_CSV_PATH, "a", encoding="utf-8") as f:
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
  