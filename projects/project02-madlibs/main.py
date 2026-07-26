# placeholder for Madlibs main.py file

print("Welcome to Mad Libs Game!")
print()

stories_created = 0
play_again = "y"

while play_again == "y":

    play = input("Would  you like to play? (y/n): ")

    while play != "y" and play != "n":
        play = input("Please enter y or n: ")

    if play == "n":
        print("Thanks for visiting!")
        break

    name = input("What is you name? ")
    print("Hello, ", name + "!")

    print("\nChoose a story:")
    print("1. Superhero Quest")
    print("2. Goofy Vacation")

    choice = input("Enter 1 or 2: ")

    while choice != "1" and choice != "2":
        choice = input("Invalid choice. Enter 1 or 2: ")

    print()

    # Story 1
    if choice == "1":
        hero = input("Enter a superhero name: ")
        villain = input("Enter a villain: ")
        place = input("Enter a place: ")
        animal = input("Enter an animal: ")
        color = input("Enter a color: ")
        number = input("Enter a number: ")

        print("\n---- Your Story ----")
        print(hero,"flew to", place, "to stop", villain + ".")
        print("Suddenly, a", color, animal, "appeared and helped.")
        print("Together they saved", number, "people.")
        print("Everyone cheered because", hero, "was the hero of the day!")

    # Story 2
    else:
        city = input("Enter a city: ")
        food = input("Enter a food: ")
        vehicle = input("Enter a vehicle: ")
        adjective = input("Enter an adjective: ")
        friend = input("Enter a friend's name: ")
        number = input("Enter a number: ")

        print("\n---- Your Story ----")
        print("One day", name, "went to", city, "with", friend + ".")
        print("They traveled in a", vehicle, "and ate", food + ".")
        print("The trip was", adjective, "and the laughed", number, "times.")
        print("It became the best vacation ever!")

    stories_created += 1

    print("\nStories Created", stories_created)

    play_again = input("Would you like to play again? (y/n): ")

    while play_again != "y" and play_again != "n":
        play_again = input("Please enter y or n: ")

print("\nThanks for playing!")