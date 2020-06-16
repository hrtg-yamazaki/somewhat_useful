import re


USERNAME_REGEX = r"^[a-zA-Z0-9-_]{4,30}$"
EMAIL_REGEX = r"^[a-zA-Z0-9-_.]{1,30}@[a-zA-Z0-9.]{1,20}.[a-zA-Z0-9]{2,10}$"
PASSWORD_REGEX = r"^[a-zA-Z0-9]{8,128}$"
COMMON_WORDS_REGEX = r".+[(test|password|user|abcd|1234)].+"


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
    # Validatorを汎用クラス化できないか考える => 出来そうならここをUserValidator(Validator)に
    """
    バリデーションメソッドをまとめて管理するためのクラス。
    フォーマット確認用の正規表現は、ファイル冒頭でまとめて定義。
    REGEXにマッチすればそのまま返し、マッチしなければもう一度入力を促しつつ再帰。
    """
    def validate_username(self, username):
        """
        User.usernameのバリデーション。
        """
        if not bool(re.match(USERNAME_REGEX, username)):
            if len(username) < 4:
                message = "This username is too short. 4 characters min."
            elif len(username) > 30:
                message = "This username is too long. 30 characters max."
            else:
                message = "Enter a valid username."
            print(message)
            username = self.validate_username(input("Username: "))
        return username

    def validate_email(self, email):
        """
        User.emailのバリデーション。
        """
        if not bool(re.match(EMAIL_REGEX, email)):
            message = "Enter a valid email address."
            print(message)
            email = self.validate_email(input("Email address: "))
        return email

    def validate_password(self, password):
        """
        User.passwordのバリデーション。
        """
        # 確認用パスワードの入力と一致確認、不一致なら再帰
        if not self.confirm_password(password):
            password = self.validate_password(input("Password: "))
        # 正規表現によるバリデーション
        if not bool(re.match(PASSWORD_REGEX, password)):
            if bool(re.search(COMMON_WORDS_REGEX, password)):
                message = "This password is too common."
            elif len(password) < 8:
                message = "This password is too short. 4 characters min."
            elif len(password) > 128:
                message = "This password is too long. 128 characters max."
            else:
                message = "Enter a valid password."
            print(message)
            password = self.validate_password(input("Password: "))
        return password

    def confirm_password(self, password):
        """
        確認用パスワードの入力を促し、最初の入力と一致するか確認する関数
        """
        password_conf = input("Password (again): ")
        if password != password_conf:
            print("Your passwords didn\'t match.")
            return False
        return True
