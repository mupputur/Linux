import os

class check_file:

    def filefound_or_not():

        walk = os.walk("/home/rajkumar")
        search_file = input("Enter the file name:")

        file_found = False
        for root_path, directories, files in walk:
            if search_file in files:
                print(os.path.join(root_path, search_file))
                return True

        if (not file_found):
            return False

if __name__ == "__main__":
    s=check_file
    s.filefound_or_not()