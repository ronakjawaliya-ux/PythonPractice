
with open("test.txt") as file:
    print(file.read())

#AfterOpeningAnyFile

with open("test.txt") as file:
    print(file.read())

print(file.closed)     #ThiswillAutomaticallyCloseTheFile:


#IfErrorOccurs:
#ForHandlingAnyException:

try:
    with open("test.tx") as file:    #IfFilePathIsWrong
        print(file.read())
except FileNotFoundError:
    print("File not found:")

