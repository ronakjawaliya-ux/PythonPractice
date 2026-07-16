# sorted() function = used with iterables


students = ["Roger","Rocks","Kaido","Linlin","Newgate","Shiki"]

sorted_students = sorted(students)

for i in sorted_students:
    print(i)


# For sort in reverse order:
students = ["Roger","Rocks","Kaido","Linlin","Newgate","Shiki"]

sorted_students = sorted(students,reverse=True)

for i in sorted_students:
    print(i)

# Level-02
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


#for sort in reverse order:
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