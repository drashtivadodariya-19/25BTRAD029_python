while True:
    print("\n1. Add Student")
    print("2. Display Students")
    print("3. Search Student")
    print("4. Exit")

    choice = int(input("Enter choice: "))

    if choice == 1:
        name = input("Enter name: ")
        marks = input("Enter marks: ")

        with open("students.txt", "a") as file:
            file.write(name + "," + marks + "\n")

        print("Student added successfully!")

    elif choice == 2:
        with open("students.txt", "r") as file:
            print(file.read())

    elif choice == 3:
        name = input("Enter name to search: ")

        with open("students.txt", "r") as file:
            found = False

            for line in file:
                if line.startswith(name + ","):
                    print(line)
                    found = True

            if not found:
                print("Student not found.")

    elif choice == 4:
        break

    else:
        print("Invalid choice!")
