class Student:
    def __init__(self, name, roll_number, cgpa):
        self.name = name
        self.roll_number = roll_number
        self.cgpa = cgpa

def sort_students(student_list):
    sorted_students = sorted(student_list, key=lambda student: student.cgpa, reverse=True)
    return sorted_students

num_students = int(input("Enter the number of students: "))

students = []

for i in range(num_students):
    name = input(f"Enter the name of student {i + 1}: ")
    roll_number = input(f"Enter the roll number of student {i + 1}: ")
    cgpa = float(input(f"Enter the CGPA of student {i + 1}: "))
    student = Student(name, roll_number, cgpa)
    students.append(student)

sorted_students = sort_students(students)

print("\nStudents sorted by CGPA (descending order):")
for student in sorted_students:
    print(f"\nName: {student.name}, Roll Number: {student.roll_number}, CGPA: {student.cgpa}")
