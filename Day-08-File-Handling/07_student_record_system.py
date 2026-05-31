while True:

    print("\n1. Add Student")
    print("2. View Students")
    print("3. Exit")

    choice = input("Enter choice: ")

    if choice == "1":

        name = input("Enter Name: ")
        marks = input("Enter Marks: ")

        with open("students.txt", "a") as file:
            file.write(name + "," + marks + "\n")

    elif choice == "2":

        with open("students.txt", "r") as file:
            print(file.read())

    elif choice == "3":
        break

    else:
        print("Invalid Choice")
