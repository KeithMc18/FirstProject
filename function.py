students = []


def get_student_titlecase():
    student_titlecase = []
    for student in students:
        student_titlecase = student.title()
    return student_titlecase

def print_student_titlecase():
    student_titlecase = []
    for student in students:
        student_titlecase = student.title()
    print(student_titlecase)


def add_student(name):
    students.append(name)

student_list = get_student_titlecase()
