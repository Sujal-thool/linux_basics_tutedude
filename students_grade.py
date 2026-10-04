students = {
    "Rahul": 85,
    "Amit": 92,
    "Priya": 78
}

while True:
    print("\n--- Student Grade System ---")
    print("1. Add Student")
    print("2. Update Grade")
    print("3. Print All Grades")
    print("4. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        name = input("Enter student name: ")
        grade = int(input("Enter grade: "))

        if name in students:
            print("Student already exists.")
        else:
            students[name] = grade
            print("Student added successfully.")

    elif choice == "2":
        name = input("Enter student name: ")

        if name in students:
            grade = int(input("Enter new grade: "))
            students[name] = grade
            print("Grade updated successfully.")
        else:
            print("Student not found.")

    elif choice == "3":
        print("\n--- All Student Grades ---")

        for name, grade in students.items():
            print(name, ":", grade)

    elif choice == "4":
        print("Program ended.")
        break

    else:
        print("Invalid choice.")


        '''PS C:\Users\hp\OneDrive\Desktop\tutedude\Python_and_Bash_sujal> py students_grade.py

--- Student Grade System ---
1. Add Student
2. Update Grade
3. Print All Grades
4. Exit
Enter your choice: 1
Enter student name: nayan
Enter grade: 99
Student added successfully.

--- Student Grade System ---
1. Add Student
2. Update Grade
3. Print All Grades
4. Exit
Enter your choice: 2
Enter student name: nayan
Enter new grade: 100
Grade updated successfully.

--- Student Grade System ---
1. Add Student
2. Update Grade
3. Print All Grades
4. Exit
Enter your choice: 3

--- All Student Grades ---
Rahul : 85
Amit : 92
Priya : 78
nayan : 100

--- Student Grade System ---
1. Add Student
2. Update Grade
3. Print All Grades
4. Exit
Enter your choice: 4
Program ended.
PS C:\Users\hp\OneDrive\Desktop\tutedude\Python_and_Bash_sujal> '''