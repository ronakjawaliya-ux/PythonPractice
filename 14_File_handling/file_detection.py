import os

path = "C:\\Users\\ronak\\OneDrive\\Desktop\\Empty"

if os.path.exists(path):
    print("That path does exists!")
    if os.path.isfile(path):
        print("That is a file!")
    elif os.path.isdir(path):
        print("That is a directory")
else:
    print("That path does NOT exists!")