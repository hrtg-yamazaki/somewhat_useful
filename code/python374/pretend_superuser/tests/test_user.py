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


if __name__ == "__main__":
    unittest.main()
