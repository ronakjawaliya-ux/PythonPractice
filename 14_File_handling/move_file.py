import os
from dataclasses import replace


#MovingAFile:
source = "test2.txt"
destination = "C:\\Users\\ronak\\OneDrive\\test2.txt"


try:
    if os.path.exists(destination):
        print("Already exists")
    else:
        os.replace(source,destination)
        print(source+" wa moved to "+destination)
except FileNotFoundError:
    print("File not found")



#MovingAFolder:
source = "FolderPY"
destination = "C:\\Users\\ronak\\OneDrive\\FolderPY"


try:
    if os.path.exists(destination):
        print("Already exists")
    else:
        os.replace(source,destination)
        print(source+" wa moved to "+destination)
except FileNotFoundError:
    print("File not found")


