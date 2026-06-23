class Student:

    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

    def __str__(self):
        return f"{self.name},{self.marks}"


def add_student():

    name = input("Enter Name: ")

    try:
        marks = float(input("Enter Marks: "))

        with open("students.txt", "a") as file:
            file.write(f"{name},{marks}\n")

        print("Student Added Successfully")

    except ValueError:
        print("Invalid Marks")


def view_students():

    try:

        with open("students.txt", "r") as file:

            data = file.readlines()

            if not data:
                print("No Records Found")

            for student in data:
                print(student.strip())

    except FileNotFoundError:
        print("No Student File Found")


def search_student():

    name = input("Enter Name to Search: ")

    found = False

    try:

        with open("students.txt", "r") as file:

            for line in file:

                if line.lower().startswith(name.lower()):

                    print("Found:", line.strip())

                    found = True

        if not found:
            print("Student Not Found")

    except FileNotFoundError:
        print("File Not Found")


def delete_student():

    name = input("Enter Name to Delete: ")

    try:

        with open("students.txt", "r") as file:
            data = file.readlines()

        with open("students.txt", "w") as file:

            deleted = False

            for line in data:

                if not line.lower().startswith(name.lower()):
                    file.write(line)

                else:
                    deleted = True

        if deleted:
            print("Student Deleted")

        else:
            print("Student Not Found")

    except FileNotFoundError:
        print("File Not Found")


while True:

    print("\n===== STUDENT MANAGEMENT =====")

    print("1. Add Student")
    print("2. View Students")
    print("3. Search Student")
    print("4. Delete Student")
    print("5. Exit")

    choice = input("Enter Choice: ")

    if choice == "1":
        add_student()

    elif choice == "2":
        view_students()

    elif choice == "3":
        search_student()

    elif choice == "4":
        delete_student()

    elif choice == "5":
        print("Thank You")
        break

    else:
        print("Invalid Choice")
