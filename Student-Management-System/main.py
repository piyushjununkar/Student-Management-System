from student_manager import add_student, list_students, find_student, update_student, delete_student

def menu():
    print("\n===== STUDENT MANAGEMENT SYSTEM =====")
    print("1. Add Student")
    print("2. View Students")
    print("3. Search Student")
    print("4. Update Student")
    print("5. Delete Student")
    print("6. Exit")

def main():
    while True:
        menu()
        choice = input("Enter choice (1-6): ").strip()

        if choice == "1":
            student = {
                "id": input("Student ID: ").strip(),
                "name": input("Name: ").strip(),
                "age": input("Age: ").strip(),
                "course": input("Course: ").strip(),
                "email": input("Email: ").strip()
            }
            try:
                student["age"] = int(student["age"])
                if student["age"] <= 0:
                    raise ValueError
            except ValueError:
                print("Age must be a positive whole number.")
                continue
            print(add_student(student))

        elif choice == "2":
            students = list_students()
            if not students:
                print("No student records found.")
            for student in students:
                print(student)

        elif choice == "3":
            student = find_student(input("Enter student ID: ").strip())
            print(student if student else "Student not found.")

        elif choice == "4":
            student_id = input("Enter student ID to update: ").strip()
            current = find_student(student_id)
            if not current:
                print("Student not found.")
                continue
            print("Press Enter to keep the current value.")
            updated = {
                "name": input(f"Name [{current['name']}]: ").strip() or current["name"],
                "age": input(f"Age [{current['age']}]: ").strip() or str(current["age"]),
                "course": input(f"Course [{current['course']}]: ").strip() or current["course"],
                "email": input(f"Email [{current['email']}]: ").strip() or current["email"]
            }
            try:
                updated["age"] = int(updated["age"])
                if updated["age"] <= 0:
                    raise ValueError
            except ValueError:
                print("Invalid age. Update cancelled.")
                continue
            print(update_student(student_id, updated))

        elif choice == "5":
            student_id = input("Enter student ID to delete: ").strip()
            confirm = input("Confirm deletion? (y/n): ").strip().lower()
            print(delete_student(student_id) if confirm == "y" else "Deletion cancelled.")

        elif choice == "6":
            print("Thank you for using the Student Management System.")
            break
        else:
            print("Invalid choice. Try again.")

if __name__ == "__main__":
    main()
