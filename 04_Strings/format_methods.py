# str.format() =  optional method that gives users
#                 more control when displaying output


#example_01

animal = "cow"
item = "moon"

#simple_way_to_code
print("The "+animal+" jumped over the "+item+"")

#different_format
print("The {} jumped over the {} ".format(animal,item))

#positional_argument
print("The {1} jumped over the {0} ".format(animal,item))

#keyword_argument
print("The {animal} jumped over the {item} ".format(animal="cow",item="moon"))

#another_format
text = "The {} jumped over the {} "
print(text.format(animal,item))




#example_02

name = "Ronak"

print("Hello, my name is {}".format(name))

print("Hello, my name is {:10}. Nice to meet you ".format(name))

print("Hello, my name is {:<10}. Nice to meet you ".format(name))

print("Hello, my name is {:>10}. Nice to meet you ".format(name))

print("Hello, my name is {:^10}. Nice to meet you ".format(name))



#example_03

number = 10000

print("The number pi is {:.2f}".format(number))

print("The number is {:,}".format(number))

print("The number is {:b}".format(number))

print("The number is {:o}".format(number))

print("The number is {:X}".format(number))

print("The number is {:E}".format(number))

