students = []

def register_student():
    name = input("Enter student name: ")
    age = int(input("Enter student age: "))
    course = input("Enter course name: ")
    
    student = {"name": name, "age": age, "course": course}
    students.append(student)
    print("✅ Student registered successfully!\n")

def view_students():
    if not students:
        print("❌ No students registered yet.\n")
    else:
        print("📋 Registered Students:")
        for idx, student in enumerate(students, 1):
            print(f"{idx}. {student['name']} - Age: {student['age']} - Course: {student['course']}")
        print()

def search_student():
    search_name = input("Enter name to search: ")
    found = False
    for student in students:
        if student["name"].lower() == search_name.lower():
            print(f"🎯 Found: {student['name']} - Age: {student['age']} - Course: {student['course']}\n")
            found = True
            break0
    if not found:
        print("❌ Student not found.\n")

def main():
    while True:
        print("------ Student Registration System ------")
        print("1. Register Student")
        print("2. View Students")
        print("3. Search Student")
        print("4. Exit")
        
        choice = input("Enter your choice (1-4): ")
        
        if choice == '1':
            register_student()
        elif choice == '2':
            view_students()
        elif choice == '3':
            search_student()
        elif choice == '4':
            print("👋 Exiting the program. Goodbye!")
            break
        else:
            print("⚠️ Invalid choice. Please try again.\n")
main()            
                                                       
