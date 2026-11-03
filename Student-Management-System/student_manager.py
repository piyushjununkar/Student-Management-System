import json
from pathlib import Path

DATA_FILE = Path(__file__).parent / "students.json"

def load_students():
    if not DATA_FILE.exists():
        return []
    try:
        with DATA_FILE.open("r", encoding="utf-8") as file:
            data = json.load(file)
            return data if isinstance(data, list) else []
    except (json.JSONDecodeError, OSError):
        print("Warning: Could not read students.json.")
        return []

def save_students(students):
    with DATA_FILE.open("w", encoding="utf-8") as file:
        json.dump(students, file, indent=4)

def add_student(student):
    students = load_students()
    if any(s["id"].casefold() == student["id"].casefold() for s in students):
        return "Student ID already exists."
    students.append(student)
    save_students(students)
    return "Student added successfully."

def list_students():
    return load_students()

def find_student(student_id):
    for student in load_students():
        if student["id"].casefold() == student_id.casefold():
            return student
    return None

def update_student(student_id, details):
    students = load_students()
    for student in students:
        if student["id"].casefold() == student_id.casefold():
            student.update(details)
            save_students(students)
            return "Student updated successfully."
    return "Student not found."

def delete_student(student_id):
    students = load_students()
    remaining = [s for s in students if s["id"].casefold() != student_id.casefold()]
    if len(remaining) == len(students):
        return "Student not found."
    save_students(remaining)
    return "Student deleted successfully."
