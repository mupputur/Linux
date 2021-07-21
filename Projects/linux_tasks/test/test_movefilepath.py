from app_source.move_filepath import move_filePath
import unittest

class Test_code(unittest.TestCase):

    def test(self):
        self.path = move_filePath
        self.assertTrue(self.path.move_file(), "file is not moved")

if __name__ == "__main__":
    unittest.main()