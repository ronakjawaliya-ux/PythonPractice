# walrus operator :=

# new to Python 3.8
# Assignment expression aka Walrus operator
# assigns values to variables as part of a larger expression


# Example:01
# W/O walrus op.
happy = True
print(happy)

# W walrus op.
print(happy := True)

# Example:02
# W/O walrus op.
foods = list()
while True:
    food = input("What food do you like?: ")
    if food == "quit":
        break
    foods.append(food)

#W walrus op.
food = list()
while food := input("What food do you like?: ") != "quit":
    foods.append(food)

