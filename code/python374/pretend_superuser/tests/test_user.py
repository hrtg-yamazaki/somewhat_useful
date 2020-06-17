import os
import sys
from pathlib import Path


# "~/pretend_superuser"をsys.pathに追加
project_path = Path(__file__).parent.parent
sys.path.append(str(project_path))


import unittest
from package.user import User


class TestUser(unittest.TestCase):

    def test_print_data(self):
        user = User("testuser", "test@test.com", "techtech", superuser="True")
        expected = "testuser\ntest@test.com\ntechtech\nTrue"
        actual = user.data()

        self.assertEqual(expected, actual)
    
    def test_superuser_is_false_without_input(self):
        user = User("testuser", "test@test.com", "techtech")
        
        self.assertFalse(user.superuser)


if __name__ == "__main__":
    unittest.main()