import os

FILE_PATH = "student.txt"

def add_student():
    """Appends a new student record to the text file."""
    student_id = input("Enter Student ID: ").strip()
    name = input("Enter Student Name: ").strip()
    course = input("Enter Course/Major: ").strip()
    grade = input("Enter Grade/GPA: ").strip()

    if not student_id or not name or not course or not grade:
        print("All fields are required.\n")
        return

    # Check for duplicate Student ID
    if os.path.exists(FILE_PATH):
        with open(FILE_PATH, "r") as file:
            for line in file:
                parts = line.strip().split(",")
                if parts and parts[0] == student_id:
                    print(f"Student ID '{student_id}' already exists.\n")
                    return

    # Write record 
    with open(FILE_PATH, "a") as file:
        file.write(f"{student_id},{name},{course},{grade}\n")
    
    print(f"Record for '{name}' added successfully!\n")

def view_all_students():
    """Reads and parses all student records from the text file."""
    if not os.path.exists(FILE_PATH) or os.path.getsize(FILE_PATH) == 0:
        print("No student records found.\n")
        return

    print("\n" + "=" * 60)
    print(f"{'ID':<8} | {'Name':<20} | {'Course':<18} | {'Grade/GPA':<10}")
    print("-" * 60)
    
    with open(FILE_PATH, "r") as file:
        for line in file:
            parts = line.strip().split(",")
            if len(parts) == 4:
                s_id, name, course, grade = parts
                print(f"{s_id:<8} | {name:<20} | {course:<18} | {grade:<10}")
    print("=" * 60 + "\n")

def search_student():
    """Searches for a specific student by ID."""
    if not os.path.exists(FILE_PATH):
        print("No records file found.\n")
        return

    search_id = input("Enter Student ID to search: ").strip()
    found = False

    with open(FILE_PATH, "r") as file:
        for line in file:
            parts = line.strip().split(",")
            if len(parts) == 4 and parts[0] == search_id:
                s_id, name, course, grade = parts
                print("\nStudent Found:")
                print(f"  ID:      {s_id}\n  Name:    {name}\n  Course:  {course}\n  Grade:   {grade}\n")
                found = True
                break

    if not found:
        print(f"No student found with ID '{search_id}'.\n")

def update_student():
    """Updates an existing student's details."""
    if not os.path.exists(FILE_PATH) or os.path.getsize(FILE_PATH) == 0:
        print("No records file found.\n")
        return

    target_id = input("Enter Student ID to update: ").strip()
    updated_records = []
    found = False

    with open(FILE_PATH, "r") as file:
        for line in file:
            parts = line.strip().split(",")
            if len(parts) == 4 and parts[0] == target_id:
                s_id, name, course, grade = parts
                found = True
                print(f"\nCurrent Record -> Name: {name}, Course: {course}, Grade: {grade}")
                new_name = input("Enter New Name (press Enter to keep current): ").strip()
                new_course = input("Enter New Course (press Enter to keep current): ").strip()
                new_grade = input("Enter New Grade/GPA (press Enter to keep current): ").strip()

                updated_name = new_name if new_name else name
                updated_course = new_course if new_course else course
                updated_grade = new_grade if new_grade else grade

                updated_records.append(f"{s_id},{updated_name},{updated_course},{updated_grade}\n")
            else:
                updated_records.append(line)

    if found:
        with open(FILE_PATH, "w") as file:
            file.writelines(updated_records)
        print(f"Record for Student ID '{target_id}' updated successfully!\n")
    else:
        print(f"No student found with ID '{target_id}'.\n")

def delete_student():
    """Deletes a student record by ID."""
    if not os.path.exists(FILE_PATH) or os.path.getsize(FILE_PATH) == 0:
        print("No records file found.\n")
        return

    target_id = input("Enter Student ID to delete: ").strip()
    updated_records = []
    found = False

    with open(FILE_PATH, "r") as file:
        for line in file:
            parts = line.strip().split(",")
            if len(parts) == 4 and parts[0] == target_id:
                s_id, name, course, grade = parts
                found = True
                confirm = input(f"Are you sure you want to delete '{name}'? (y/N): ").strip().lower()
                if confirm != "y":
                    print("Action cancelled.\n")
                    return
            else:
                updated_records.append(line)

    if found:
        with open(FILE_PATH, "w") as file:
            file.writelines(updated_records)
        print(f"Record for Student ID '{target_id}' deleted successfully!\n")
    else:
        print(f"No student found with ID '{target_id}'.\n")

def main():
    while True:
        print("=== STUDENT RECORD MANAGEMENT SYSTEM ===")
        print("1. Add Student Record")
        print("2. View All Students")
        print("3. Search Student by ID")
        print("4. Update Student Record")
        print("5. Delete Student Record")
        print("6. Exit")
        
        choice = input("Select an option (1-6): ").strip()
        print()

        if choice == "1":
            add_student()
        elif choice == "2":
            view_all_students()
        elif choice == "3":
            search_student()
        elif choice == "4":
            update_student()
        elif choice == "5":
            delete_student()
        elif choice == "6":
            print("Exiting system. Goodbye!")
            break
        else:
            print("Invalid selection. Please choose 1-6.\n")

if __name__ == "__main__":
    main()