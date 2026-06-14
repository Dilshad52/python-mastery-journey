class Student:

    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

    def display(self):
        print("Name:", self.name)
        print("Marks:", self.marks)


students = []

while True:

    print("\n1. Add Student")
    print("2. View Students")
    print("3. Exit")

    choice = input("Enter choice: ")

    if choice == "1":

        name = input("Enter Name: ")
        marks = input("Enter Marks: ")

        students.append(Student(name, marks))

    elif choice == "2":

        for student in students:
            student.display()

    elif choice == "3":
        break
