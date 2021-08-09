import shutil
from os import path

class move_filePath:

    def move_file():

        source_path = "/home/rajkumar/sample.py"
        destination_path = "/home/rajkumar/Desktop/linux_tasks/files"


        if path.exists(source_path):
            new_location = shutil.move(source_path, destination_path)
            print(new_location)
            return True
        else:
            return False

if __name__ == "__main__":
    s=move_filePath
    s.move_file()