import zipfile
import os
from zipfile import ZipFile

class achiveFile:

    def zip_file():

        try:
            os.chdir("/home/rajkumar/Desktop/linux_tasks/files")
            createzip:ZipFile = zipfile.ZipFile('newfile.zip','w')
            createzip.write('sample.py', compress_type=zipfile.ZIP_DEFLATED)
            createzip.write('raj.jpg', compress_type=zipfile.ZIP_DEFLATED)
            createzip.close()
            return True

        except FileNotFoundError:
            return False

    def unzip_file():

        try:
            unzip =  ZipFile("/home/rajkumar/Desktop/linux_tasks/files/newfile.zip", 'r')
            unzip.extractall("/home/rajkumar/Desktop/linux_tasks/files/newfile")
            return True

        except FileNotFoundError:
            return False

if __name__ == "__main__":
    s=achiveFile
    s.unzip_file()
    s.zip_file()