import os

class MissingFolderError(Exception):
    pass

def scan_demo():

    path = input("Enter folder path: ")

    try:

        if not os.path.exists(path):
            raise FileNotFoundError("Folder does not exist!")

        for root, dirs, files in os.walk(path):

            print("\nFolder:", root)

            for file in files:
                print("File:", file)

            if not dirs and not files:
                raise MissingFolderError("Empty Folder Found")

    except FileNotFoundError as e:
        print(e)

    except MissingFolderError as e:
        print(e)

    except Exception as e:
        print("Unexpected Error:", e)