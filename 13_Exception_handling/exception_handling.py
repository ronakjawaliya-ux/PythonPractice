# exception = events detected during execution that interrupt the flow of a program



#SimpleExceptionHandling:

try:
    numerator = int(input("Enter a number to divide: "))
    denominator =int(input("Enter a number to divide by: "))
    result = numerator / denominator
    print(result)
except Exception:
    print("Invalid input:(")


#AdvancedExceptionHandling:
#resultBeforeExceptionHandling:

try:
    numerator = int(input("Enter a number to divide: "))
    denominator =int(input("Enter a number to divide by: "))
    result = numerator / denominator
    print(result)

except ZeroDivisionError as e:
    print(e)
    print("Invalid! can't divide by zero")
except ValueError as e:
    print(e)
    print("Invalid! enter only numbers")
except TypeError as e:
    print(e)
    print("Invalid! enter only integers")
except Exception as e:
    print(e)



#AdvancedExceptionHandling:
#resultAfterExceptionHandling:

try:
    numerator = int(input("Enter a number to divide: "))
    denominator =int(input("Enter a number to divide by: "))
    result = numerator / denominator

except ZeroDivisionError as e:
    print(e)
    print("Invalid! can't divide by zero")
except ValueError as e:
    print(e)
    print("Invalid! enter only numbers")
except TypeError as e:
    print(e)
    print("Invalid! enter only integers")
except Exception as e:
    print(e)
else:
    print(result)