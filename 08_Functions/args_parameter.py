#  *args = parameter will pack all arguments into a tuple
#         useful so that a function can accept a varying amount of arguments


#  ---example_01---
def add(*args):
    sum = 0
    for arg in args:
        sum += arg
    return sum
print(add(1,2,3,4))
