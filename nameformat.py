def sayHello(firstName):
    """Returns a greeting."""
    return "Hello " + firstName + "!"

def fullName(firstName,lastName):
    """Returns the full name."""
    return firstName + " " + lastName

def lastNameFirst(firstName, lastName):
    """Returns the last name first."""
    return lastName + ", " + firstName

import nameformat

firstName = input("Enter your first name: ")
lastName = input("Enter your last name: ")

choice = 0

while choice != 5:

    print("\n----MENU----")
    print("1. Say Hello")
    print("2. Full Name")
    print("3. Last Name First")
    print("4. View Documentation")
    print("5. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        print(nameformat.sayHello(firstName))

    elif choice == 2:
        print(nameformat.fullName(firstName, lastName))

    elif choice == 3:
        print(nameformat.lastNameFirst(firstName, lastName))

    elif choice == 4:
        help(nameformat.sayHello)
        help(nameformat.fullName)
        help(nameformat.lastNameFirst)

    elif choice == 5:
        print("Goodbye!")

    else:
        print("Invalid choice. Try again.")
