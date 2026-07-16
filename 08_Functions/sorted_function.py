
# sorted() function = used with iterables



# ______________________________________________________________________
#level-01 | ft.iterables
# ______________________________________________________________________

students = ["Roger","Rocks","Kaido","Linlin","Newgate","Shiki"]

sorted_students = sorted(students)

for i in sorted_students:
    print(i)


# ______________________________________________________________________
# For sort in reverse order:
# ______________________________________________________________________

students = ["Roger","Rocks","Kaido","Linlin","Newgate","Shiki"]

sorted_students = sorted(students,reverse=True)

for i in sorted_students:
    print(i)


# ______________________________________________________________________
# Level-02 | ft.Lists
# ______________________________________________________________________

students = [("Roger","S", 53),
            ("Rocks","SS", 43),
            ("Kaido","A", 59),
            ("Linlin","A", 68),
            ("Newgate","S", 72),
            ("Shiki","S", 73)]


grade = lambda grades:grades[1]
students.sort(key=grade,reverse=True)

for i in students:
    print(i)


# ______________________________________________________________________
#for sort in reverse order:
# ______________________________________________________________________

students = [("Roger","S", 53),
            ("Rocks","SS", 43),
            ("Kaido","A", 59),
            ("Linlin","A", 68),
            ("Newgate","S", 72),
            ("Shiki","S", 73)]


grade = lambda grades:grades[1]
students.sort(key=grade,reverse=True)

for i in students:
    print(i)


# ______________________________________________________________________
# if we want to sort on basis of age:
# ______________________________________________________________________

students = [("Roger","S", 53),
            ("Rocks","SS", 43),
            ("Kaido","A", 59),
            ("Linlin","A", 68),
            ("Newgate","S", 72),
            ("Shiki","S", 73)]


age = lambda ages:ages[1]
students.sort(key=age)

for i in students:
    print(i)


# ______________________________________________________________________
# for sort in reverse order:
# ______________________________________________________________________

students = [("Roger","S", 53),
            ("Rocks","SS", 43),
            ("Kaido","A", 59),
            ("Linlin","A", 68),
            ("Newgate","S", 72),
            ("Shiki","S", 73)]


age = lambda ages:ages[2]
students.sort(key=age,reverse=True)

for i in students:
    print(i)


# ______________________________________________________________________
# Level-03 | ft.tuple_of_tuple(iterables)
# ______________________________________________________________________

students = (("Roger","S", 53),
            ("Rocks","SS", 43),
            ("Kaido","A", 59),
            ("Linlin","A", 68),
            ("Newgate","S", 72),
            ("Shiki","S", 73))


age = lambda ages:ages[2]
sorted_students = sorted(students,key=age)

for i in sorted_students:
    print(i)


# ______________________________________________________________________
# for sort in reverse order:
# ______________________________________________________________________

students = (("Roger","S", 53),
            ("Rocks","SS", 43),
            ("Kaido","A", 59),
            ("Linlin","A", 68),
            ("Newgate","S", 72),
            ("Shiki","S", 73))


age = lambda ages:ages[2]
sorted_students = sorted(students,key=age,reverse=True)

for i in sorted_students:
    print(i)


# ______________________________________________________________________

# ______________________________________________________________________