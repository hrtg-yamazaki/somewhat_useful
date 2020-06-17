import os
from pathlib import Path


# ディレクトリをプロジェクト"pretend_superuser"に切り替え
project_path = Path(__file__).parent.parent
os.chdir(project_path)


import unittest
from package.user import User


class TestSet(unittest.TestCase):

    def test_equal(self):
        ex = "a"
        ac = "b"

        self.assertEqual(ex, ac)


if __name__ == "__main__":
    unittest.main()
