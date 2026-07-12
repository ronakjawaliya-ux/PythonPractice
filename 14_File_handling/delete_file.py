import os

#Simple: #FileDelete:
os.remove("test3.txt")


#Advanced: #FileDelete:
import os

path = "test3.txt"

try:
    os.remove(path)
except FileNotFoundError:
    print("File was not found")



#FolderDelete
import os

path = "Empty02"

try:
    os.remove(path)
except FileNotFoundError:
    print("File was not found")
except PermissionError:
    print("Permission denied for deleting file")
else:
    print(path+" was deleted!")



#FolderHavingFles
import shutil

path = "Empty02"

try:
    shutil.rmtree(path)
except FileNotFoundError:
    print("File was not found")
except PermissionError:
    print("Permission denied for deleting file")
else:
    print(path+" was deleted!")



#FolderNotHavingFles:
import os

path = "Empty02"

try:
    os.rmdir(path)
except FileNotFoundError:
    print("File was not found")
except PermissionError:
    print("Permission denied for deleting file")
else:
    print(path+" was deleted!")