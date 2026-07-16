#This is how you assign a function to variable:

def hello():
    print("hello")

#1
print(hello)
hi = hello
print(hi)

#2
hi = hello
hello()
hi()

#3
say = print
say("Whoa! I can't believe you! :0")