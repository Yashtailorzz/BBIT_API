class Student:
    def __init__(self, name, student_id, assignments ={}):
        self.name = name
        self.student_id = student_id
        self.assignments = assignments

    def add_assignment(self, assignment_name, grade):
        self.assignments[assignment_name] = grade
        print(f"add assignment '{assignment_name}' with grade {grade} for {self.name}.")

    def display_grades(self):
        print(f"Grades for {self.name}:")
        if self.assignments:
            for assignment, grade in self.assignments.items():
                print(f" - {assignment}: {grade}")
        else:
            print(" No assignments yet.")


class Instructor:
    def __init__(self, name, course_name):
        self.name = name
        self.course_name = course_name
        self.students = []

    def add_student(self, student):
        self.students.append(student)
        print(f"Added student {student.name} to '{self.course_name}'.")

    def assign_grade(self, student_id, assignment_name, grade):
        student = next((s for s in self.students if s.student_id == student_id), None)
        if student:
            student.add_assignment(assignment_name, grade)
        else:
            print(f"No student found with ID {student_id}.")

    def display_students_and_grades(self):
        print(f"Course: {self.course_name}")
        for student in self.students:
            print(f"Student: {student.name} (ID: {student.student_id})")
            student.display_grades()


# Interactive Code
def main():
    instructor = Instructor("Yash Tailor", "Api")
    print(f"Welcome, {instructor.name}! Managing course: {instructor.course_name}")

    while True:
        print("\nOptions:")
        print("1. Add a student")
        print("2. Assign a grade")
        print("3. Display all students and grades")
        print("4. Exit")

        choice = input("Choose an option: ")
        if choice == "1":
            name = input("Enter student name: ")
            student_id = input("Enter student ID: ")
            student = Student(name, student_id)
            instructor.add_student(student)
        elif choice == "2":
            student_id = input("Enter student ID: ")
            assignment_name = input("Enter assignment name: ")
            grade = input("Enter grade: ")
            instructor.assign_grade(student_id, assignment_name, grade)
        elif choice == "3":
            instructor.display_students_and_grades()
        elif choice == "4":
            print("Exiting...")
            break
        else:
            print("Invalid option. Please try again.")


if __name__ == "__main__":
    main()
