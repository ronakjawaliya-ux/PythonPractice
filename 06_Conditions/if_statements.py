#if statement = a block of code that will execute if it's conditions is true.

age = int(input("What is your age?: "))

if age == 100:
    print("You area century old: ")

elif age >= 18:
    print("You are an adult")

elif age < 0:
    print("You haven't been born yet: ")

else:
    print("You are a child: ")
