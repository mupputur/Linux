from app_source.achive_file import achiveFile
import unittest

class Test_code(unittest.TestCase):

    def test1(self):
        self.path = achiveFile
        self.assertTrue(self.path.zip_file(), "file is unable to zip")

    def test2(self):
        self.path = achiveFile
        self.assertTrue(self.path.unzip_file(), "file is unable to unzip")

if __name__== "__main__":
    unittest.main()