# Lambda function = function written in 1 line using lambda keyword
#                   accepts any number of arguments, but only has one expression
#                   (think of it as a shortcut)
#                   (useful if needed for a short period of time, throw-away)
#
# lambda parameters:expression

# Not Using lambda func.
def double(x):
    return x*2
print(double(5))

# Using lambda func.
double = lambda x:x * 2
print(double(5))

# for multiplying 2 values with each other:
multiply = lambda x, y: x * y
print(multiply(5,6))

# for adding 3 values with each other:
add = lambda x, y, z: x + y + z
print(add(3,4,5))

# for passing strings:
full_name = lambda first_name, last_name: first_name+" "+last_name
print(full_name("Ronak","Jawalia"))

# for checking age:
age_check = lambda age:True if age >= 18 else False
print(age_check(18))

