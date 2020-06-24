import os
import sys
from pathlib import Path
import tempfile
import csv

# "~/pretend_superuser"をsys.pathに追加
project_path = Path(__file__).parent.parent
sys.path.append(str(project_path))


import unittest
from package.user import Users, User
from package.validator import Validator
from package.general import str_now


class TestUsers(unittest.TestCase):

    def test_users(self):
        """
        Users.__init__()のテスト。
        """
        expected = []
        users = Users()
        actual = users.users
        self.assertEqual(expected, actual)

    def test_latest_user(self):
        """
        Users.latest_user()のテスト。
        """
        users = Users()
        user1 = User(
            "test1", "test@test.com", "techtech", str_now()
        )
        user2 = User(
            "test2", "test2@test.com", "techtech", str_now()
        )
        users.users = [user1, user2]
        expected = user2
        actual = users.latest_user()
        self.assertEqual(expected, actual)

    def test_read_users(self):
        """
        Users.read_users()のテスト。
        読み込み時にUserインスタンスを再生成する以上、
        インスタンスのままassertEqualできないため、
        User.data()で変換した内容と比較。
        """
        user1 = User(
            "test1", "test@test.com", "techtech", str_now()
        )
        user2 = User(
            "test2", "test2@test.com", "techtech", str_now()
        )
        expected = [user1.data(), user2.data()]

        with tempfile.NamedTemporaryFile(mode="w") as f:
            row1 = ",".join(map(str, user1.data()))
            row2 = ",".join(map(str, user2.data()))
            f.write(row1 + "\n" + row2 + "\n")
            f.flush()
            users = Users()
            actual = [user.data() for user in users.read_users(f.name)]
        self.assertEqual(expected, actual)


class TestUser(unittest.TestCase):

    def test_data(self):
        """
        User.data()のユニットテスト。
        """
        expected = [
            "255", "testuser", "test@test.com", "techtech",
            "2020/06/21_14:30:00", "True"
        ]
        user = User(
            "testuser", "test@test.com", "techtech",
            "2020/06/21_14:30:00", u_id = 255, superuser="True"
        )
        actual = user.data()
        self.assertEqual(expected, actual)
    
    def test_superuser_is_false_without_input(self):
        """
        superuser属性の指定をせずインスタンスを作成した時、
        superuser属性がFalseになっているかどうかのテスト。
        """
        user = User(
            "testuser", "test@test.com", "techtech", str_now()
        )
        self.assertFalse(user.superuser)

    def test_info(self):
        """
        User.infoのテスト。
        """
        expected = {
            "id": 255, "username": "testuser",
            "email":  "test@test.com"
        }
        user = User(
            "testuser", "test@test.com", "techtech",
            str_now(), u_id = 255
        )
        actual = user.info()
        self.assertEqual(expected, actual)

    def test_create_user(self):
        """
        create_userのテスト。
        """
        user = User.new_user(
            "testuser", "test@test.com", "techtech",
            str_now(), u_id = 255
        )
        with tempfile.TemporaryDirectory() as d:
            path = os.path.join(d + "temp.csv")
            user.create_user(path)
            with open(path, "r", encoding="utf-8") as f:
                for row in f:
                    self.assertIn("testuser", row)


class TestValidator(unittest.TestCase):

    def test_username_is_valid(self):
        """
        Validator.username_is_valid()に
        適切な値が渡された場合Trueを返すかどうか。
        """
        v = Validator()
        username = "testuser"
        self.assertTrue(v.username_is_valid(username))

    def test_username_is_invalid(self):
        """
        Validator.username_is_valid()のテスト。
        正規表現で指定したフォーマットに合わない値が渡された場合、
        Falseを返すかどうか。
        """
        v = Validator()
        # too short
        username = "tes"
        self.assertFalse(v.username_is_valid(username))
        # too long
        username = "1234567890123456789012345678901"
        self.assertFalse(v.username_is_valid(username))
        # unspecified characters
        username = "テストユーザー"
        self.assertFalse(v.username_is_valid(username))

    def test_username_error_with_too_short_username(self):
        """
        validator.username_error()のテスト。
        3文字以下の場合に適切なメッセージを返すかどうか。
        """
        v = Validator()
        username = "tes"
        expected = "This username is too short. 4 characters min."
        actual = v.username_error(username)
        self.assertEqual(expected, actual)

    def test_username_error_with_too_long_username(self):
        """
        validator.username_error()のテスト。
        31文字以上の場合に適切なメッセージを返すかどうか。
        """
        v = Validator()
        username = "1234567890123456789012345678901"
        expected = "This username is too long. 30 characters max."
        actual = v.username_error(username)
        self.assertEqual(expected, actual)

    def test_username_error_with_unspecified_characters(self):
        """
        Validator.username_error()のユニットテスト。
        [a-zA-Z0-9-_]以外の文字が渡された場合に
        適切なメッセージを返すかどうか。
        """
        v = Validator()
        username = "テストユーザー"
        expected = "Enter a valid username."
        actual = v.username_error(username)
        self.assertEqual(expected, actual)

    def test_email_is_valid(self):
        """
        Validator.email_is_valid()に
        適切な値が渡された場合Trueを返すかどうか。
        """
        v = Validator()
        email = "test@test.com"
        self.assertTrue(v.email_is_valid(email))

    def test_email_is_invalid(self):
        """
        Validator.email_is_valid()のテスト。
        正規表現で指定したフォーマットに合わない値が渡された場合、
        Falseを返すかどうか。
        """
        v = Validator()
        email = "testemailaddress"
        self.assertFalse(v.email_is_valid(email))
        email = "テスト@テスト.com"
        self.assertFalse(v.email_is_valid(email))

    def test_email_error_without_atmark(self):
        """
        validator.email_error()のテスト。
        @がない場合に適切なメッセージを返すかどうか。
        """
        v = Validator()
        email = "testemailaddress"
        expected = "Enter a valid email address."
        actual = v.email_error(email)
        self.assertEqual(expected, actual)

    def test_email_error_with_unspecified_characters(self):
        """
        validator.email_error()のテスト。
        指定外の文字が入っている場合に適切なメッセージを返すかどうか。
        """
        v = Validator()
        email = "テスト@テスト.com"
        expected = "Enter a valid email address."
        actual = v.email_error(email)
        self.assertEqual(expected, actual)

    def test_password_is_valid(self):
        """
        Validator.password_is_valid()に
        適切な値が渡された場合Trueを返すかどうか。
        """
        v = Validator()
        password = "techtech"
        password_conf = "techtech"
        self.assertTrue(v.password_is_valid(password, password_conf))
    
    def test_password_is_invalid(self):
        """
        Validator.password_is_valid()のテスト。
        正規表現で指定したフォーマットに合わない値が渡された場合、
        Falseを返すかどうか。
        """
        v = Validator()
        # too_short
        password = "techtec"
        password_conf = "techtec"
        self.assertFalse(v.password_is_valid(password, password_conf))
        # too_long
        password = "techtechtecht" * 10
        password_conf = "techtechtecht" * 10
        self.assertFalse(v.password_is_valid(password, password_conf))
        # too_common
        password = "12345678"
        password_conf = "12345678"
        self.assertFalse(v.password_is_valid(password, password_conf))
        # with unspecified characters
        password = "テストパスワード"
        password_conf = "テストパスワード"
        self.assertFalse(v.password_is_valid(password, password_conf))
        # pw != pw_conf
        password = "techtech"
        password_conf = "tetetech"
        self.assertFalse(v.password_is_valid(password, password_conf))

    def test_not_match_error(self):
        """
        validator.not_match_error()のテスト。
        @以上の場合に適切なメッセージを返すかどうか。
        """
        v = Validator()
        expected = "Your password didn\'t match."
        actual = v.not_match_error()
        self.assertEqual(expected, actual)

    def test_password_error_with_too_short(self):
        """
        validator.password_error()のテスト。
        7文字以下の場合に適切なメッセージを返すかどうか。
        """
        v = Validator()
        password = "techtec"
        expected = "This password is too short. 8 characters min."
        actual = v.password_error(password)
        self.assertEqual(expected, actual)

    def test_password_error_with_too_long(self):
        """
        validator.password_error()のテスト。
        128文字以上の場合に適切なメッセージを返すかどうか。
        """
        v = Validator()
        password = "techtechtech" * 10 + "techtecht"
        expected = "This password is too long. 128 characters max."
        actual = v.password_error(password)
        self.assertEqual(expected, actual)

    def test_password_error_with_common_words(self):
        """
        validator.password_error()のテスト。
        禁止語句を含む場合に適切なメッセージを返すかどうか。
        """
        v = Validator()
        password = "12345678"
        expected = "This password is too common."
        actual = v.password_error(password)
        self.assertEqual(expected, actual)

    def test_password_error_with_unspecified_characters(self):
        """
        validator.password_error()のテスト。
        指定外の文字を含む場合に適切なメッセージを返すかどうか。
        """
        v = Validator()
        password = "テストパスワード"
        expected = "Enter a valid password."
        actual = v.password_error(password)
        self.assertEqual(expected, actual)


if __name__ == "__main__":
    unittest.main()
