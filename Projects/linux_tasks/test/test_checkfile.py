from app_source.check_file import check_file
import unittest

class Test_code(unittest.TestCase):

    def test(self):
        self.path = check_file
        self.assertTrue(self.path.filefound_or_not(), "file is not avialable")

if __name__ == "__main__":
    unittest.main()

