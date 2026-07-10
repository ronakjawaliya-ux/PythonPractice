# tuple = collection which is ordered and unchangeable
#         used ton group together related area


#EXAMPLE-01

student = ("Ronak", "21", "male")

print(student.count("Ronak"))
print(student.index("male"))

for x in student:
    print(x)

if "Ronak" in student:
    print("Bro is here!")