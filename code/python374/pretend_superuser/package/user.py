import re


USERNAME_REGEX = r"^[a-zA-Z0-9-_]{4,30}$"


class User:
    
    def __init__(self, username, email, password, superuser=False):
        self.username = username
        self.email = email
        self.password = password
        self.superuser = superuser

    def print_data(self):
        """
        デバッグ用にインスタンス変数を一覧表示する関数
        """
        print(self.username, self.email, self.password, self.superuser, sep="\n")


class Validator():
    """
    バリデーションメソッドをまとめて管理するためのクラス。
    フォーマット確認用の正規表現は、ファイル冒頭でまとめて定義。
    REGEXにマッチすればそのまま返し、マッチしなければもう一度入力を促しつつ再帰。
    """

    def validate_username(self, username):
        """
        usernameのバリデーション
        """
        if not bool(re.match(USERNAME_REGEX, username)):
            if len(username) < 4:
                message = "This username is too short. 4 characters min."
            elif len(username) > 30:
                message = "This username is too long. 30 characters max."
            else:
                message = "Enter a valid username."
            print(message)
            username = self.validate_username(input("Username:"))
        return username
