
students = ["saif", "rupa", "efaz", "muntaha", "lamiya"]


marks = {
    "saif": 75,
    "rupa": 35,
    "efaz": 80,
    "muntaha": 45,
    "lamiya": 30
}



passed = 0
failed = 0

for name, mark in marks.items():

    if mark >= 40:
        print("Student Name:", name, "— Marks:", mark, "— Pass")
        passed = passed + 1

    else:
        print("Student Name:", name, "— Marks:", mark, "— Fail")
        failed = failed + 1



wanted = input("Enter student name: ")

if wanted in students:
    print("Student Found")
else:
    print("Student Not Found")



total = len(students)

print("Total Students:", total)


print("Passed Students:", passed)
print("Failed Students:", failed)


