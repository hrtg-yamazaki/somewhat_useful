import os
import sys
from pathlib import Path


# "~/pretend_superuser"をsys.pathに追加
project_path = Path(__file__).parent.parent
sys.path.append(str(project_path))


import unittest
from package.user import User, Validator


class TestUser(unittest.TestCase):

    def test_data(self):
        """
        User.data()のユニットテスト。
        """
        user = User("testuser", "test@test.com", "techtech", superuser="True")
        expected = "testuser\ntest@test.com\ntechtech\nTrue"
        actual = user.data()

        self.assertEqual(expected, actual)
    
    def test_superuser_is_false_without_input(self):
        """
        superuser属性の指定をせずインスタンスを作成した時、
        superuser属性がFalseになっているかどうかのテスト。
        """
        user = User("testuser", "test@test.com", "techtech")
        
        self.assertFalse(user.superuser)


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
        @以上の場合に適切なメッセージを返すかどうか。
        """
        v = Validator()
        email = "testemailaddress"
        expected = "Enter a valid email address."
        actual = v.email_error(email)
        self.assertEqual(expected, actual)

    def test_email_error_with_unspecified_characters(self):
        """
        validator.email_error()のテスト。
        @以上の場合に適切なメッセージを返すかどうか。
        """
        v = Validator()
        email = "テスト@テスト.com"
        expected = "Enter a valid email address."
        actual = v.email_error(email)
        self.assertEqual(expected, actual)


if __name__ == "__main__":
    unittest.main()
