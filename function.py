students = []

# enter_student = input("Do you want to enter a student name? Y/N")
# yes = "Y"

def get_student_titlecase():
    student_titlecase = []
    for student in students:
        student_titlecase.append(student["name"].title()) #, student["student_id"].title()
    return student_titlecase


def print_student_titlecase():
    student_titlecase = get_student_titlecase()
    print(student_titlecase)


def add_student(name, student_id=1232):
    student = {"name": name, "student_id": student_id}
    students.append(student)


def save_file(student):
    try:
        f = open("student.txt", "a")
        f.write(student + '\n')
        f.close()
    except Exception:
        print("Could not save file")


def read_file():
    try:
        f = open("student.txt", "r")
        for student in f.readlines():
        # for student in read_students(f):
            add_student(student)
        f.close()
    except Exception:
        print("Could not read file")

#
# def read_students(f):
#     for line in f:
#         yield line


read_file()
print_student_titlecase()

# if enter_student == "y" or enter_student == "Y":
student_name = input("Enter a students name: ")
student_id = input("Enter the student id: ")

add_student(student_name) #, student_id)
save_file(student_name)

# else:
#     print("You have exited the programme. Thank You")
