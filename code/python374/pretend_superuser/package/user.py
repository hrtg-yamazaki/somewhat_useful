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
