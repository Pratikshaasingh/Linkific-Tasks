import os

FILE_PATH = "employees.txt"

def add_employee():
    """Appends a new employee record to the text file."""
    emp_id = input("Enter Employee ID: ").strip()
    name = input("Enter Employee Name: ").strip()
    department = input("Enter Department: ").strip()
    salary = input("Enter Salary: ").strip()

    if not emp_id or not name or not department or not salary:
        print("All fields are required.\n")
        return

    # Check for duplicate Employee ID
    if os.path.exists(FILE_PATH):
        with open(FILE_PATH, "r") as file:
            for line in file:
                parts = line.strip().split(",")
                if parts and parts[0] == emp_id:
                    print(f" Employee ID '{emp_id}' already exists.\n")
                    return

    # Write record in CSV-style format
    with open(FILE_PATH, "a") as file:
        file.write(f"{emp_id},{name},{department},{salary}\n")
    
    print(f" Record for '{name}' added successfully!\n")

def view_all_employees():
    """Reads and parses all records from the text file."""
    if not os.path.exists(FILE_PATH) or os.path.getsize(FILE_PATH) == 0:
        print("No employee records found.\n")
        return

    print("\n" + "=" * 60)
    print(f"{'ID':<8} | {'Name':<20} | {'Department':<18} | {'Salary':<10}")
    print("-" * 60)
    
    with open(FILE_PATH, "r") as file:
        for line in file:
            parts = line.strip().split(",")
            if len(parts) == 4:
                e_id, name, dept, salary = parts
                print(f"{e_id:<8} | {name:<20} | {dept:<18} | {salary:<10}")
    print("=" * 60 + "\n")

def search_employee():
    """Searches for a specific employee by ID."""
    if not os.path.exists(FILE_PATH):
        print(" No records file found.\n")
        return

    search_id = input("Enter Employee ID to search: ").strip()
    found = False

    with open(FILE_PATH, "r") as file:
        for line in file:
            parts = line.strip().split(",")
            if len(parts) == 4 and parts[0] == search_id:
                e_id, name, dept, salary = parts
                print("\n Employee Found:")
                print(f"  ID:         {e_id}\n  Name:       {name}\n  Department: {dept}\n  Salary:     {salary}\n")
                found = True
                break

    if not found:
        print(f"No employee found with ID '{search_id}'.\n")

def update_employee():
    """Updates an existing employee's details."""
    if not os.path.exists(FILE_PATH) or os.path.getsize(FILE_PATH) == 0:
        print(" No records file found.\n")
        return

    target_id = input("Enter Employee ID to update: ").strip()
    updated_records = []
    found = False

    with open(FILE_PATH, "r") as file:
        for line in file:
            parts = line.strip().split(",")
            if len(parts) == 4 and parts[0] == target_id:
                e_id, name, dept, salary = parts
                found = True
                print(f"\nCurrent Record -> Name: {name}, Dept: {dept}, Salary: ${salary}")
                new_name = input("Enter New Name (press Enter to keep current): ").strip()
                new_dept = input("Enter New Department (press Enter to keep current): ").strip()
                new_salary = input("Enter New Salary (press Enter to keep current): ").strip()

                updated_name = new_name if new_name else name
                updated_dept = new_dept if new_dept else dept
                updated_salary = new_salary if new_salary else salary

                updated_records.append(f"{e_id},{updated_name},{updated_dept},{updated_salary}\n")
            else:
                updated_records.append(line)

    if found:
        with open(FILE_PATH, "w") as file:
            file.writelines(updated_records)
        print(f" Record for Employee ID '{target_id}' updated successfully!\n")
    else:
        print(f"No employee found with ID '{target_id}'.\n")

def delete_employee():
    """Deletes an employee record by ID."""
    if not os.path.exists(FILE_PATH) or os.path.getsize(FILE_PATH) == 0:
        print(" No records file found.\n")
        return

    target_id = input("Enter Employee ID to delete: ").strip()
    updated_records = []
    found = False

    with open(FILE_PATH, "r") as file:
        for line in file:
            parts = line.strip().split(",")
            if len(parts) == 4 and parts[0] == target_id:
                e_id, name, dept, salary = parts
                found = True
                confirm = input(f" Are you sure you want to delete '{name}'? (y/N): ").strip().lower()
                if confirm != "y":
                    print("Action cancelled.\n")
                    return
            else:
                updated_records.append(line)

    if found:
        with open(FILE_PATH, "w") as file:
            file.writelines(updated_records)
        print(f"Record for Employee ID '{target_id}' deleted successfully!\n")
    else:
        print(f" No employee found with ID '{target_id}'.\n")

def main():
    while True:
        print("=== EMPLOYEE RECORD MANAGEMENT SYSTEM ===")
        print("1. Add Employee Record")
        print("2. View All Employees")
        print("3. Search Employee by ID")
        print("4. Update Employee Record")
        print("5. Delete Employee Record")
        print("6. Exit")
        
        choice = input("Select an option (1-6): ").strip()
        print()

        if choice == "1":
            add_employee()
        elif choice == "2":
            view_all_employees()
        elif choice == "3":
            search_employee()
        elif choice == "4":
            update_employee()
        elif choice == "5":
            delete_employee()
        elif choice == "6":
            print("Exiting system. Goodbye!")
            break
        else:
            print("Invalid selection. Please choose 1-6.\n")

if __name__ == "__main__":
    main()
