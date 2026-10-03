
# Student Management System
# Used to manage student names and grades

student_grades = {}


# Add student
def add_student(name, grade):
    student_grades[name] = grade
    print(f"Added {name} with grade {grade}")


# Update student
def update_student(name, grade):
    if name in student_grades:
        student_grades[name] = grade
        print(f"{name}'s grade has been updated to {grade}")
    else:
        print(f"{name} is not found!")


# Delete student
def delete_student(name):
    if name in student_grades:
        del student_grades[name]
        print(f"Deleted {name} and their grade")
    else:
        print(f"{name} is not found!")


# Display all students
def display_all_student():
    if student_grades:
        print("\nStudent Grades:")
        
        for name, grade in student_grades.items():
            print(f"{name} : {grade}")
    else:
        print("No students found!")

def search_student(name):
    if name in student_grades:
        print(f"{name} yes this student is in our school")
    else:
        print("student name not found")

# Main program
def main():
    while True:
        print("\nStudent Grades Management System")
        print("1. Add student")
        print("2. Update student")
        print("3. Delete student")
        print("4. View students")
        print("5. search student")
        print("6. Exit")

        choice = int(input("Enter your choice = "))

        if choice == 1:
            name = input("Enter the student name = ")
            grade = int(input("Enter the grade = "))
            add_student(name, grade)

        elif choice == 2:
            name = input("Enter the student name = ")
            grade = int(input("Enter the new grade = "))
            update_student(name, grade)

        elif choice == 3:
            name = input("Enter the student name = ")
            delete_student(name)

        elif choice == 4:
            display_all_student()

        elif choice == 5:
            name = input("Enter student name = ")
            search_student(name)

        elif choice == 6:
            print("Closing the program...")
            break

        else:
            print("Invalid choice!")

# we can add more feature to this code so till now this is the code

main()