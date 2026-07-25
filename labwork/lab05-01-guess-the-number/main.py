# starting Guess the Number program from our textbook

import random


def display_title():
    print("Guess the number!")
    print()

def get_name():
    player_name = input("What is your name? ")
    print("Hello", player_name)
    print()

def play_game(wins):
    level = input("What game level would you like to play? E for Easy, M for Medium, or H for Hard")

    if level.lower() == "e":
        max_number = 10
        tries = 5
    elif level.lower() == "m":
        max_number = 100
        tries = 8
    elif level.lower() == "h":
        max_number = 1000
        tries = 10
    else:
        print("Sorry. Invalid input. Please try again")

        
    number = random.randint(1, max_number)
    print(f"I'm thinking of a number from 1 to {max_number}\n")
    count = 1

    while count <= tries:
        guess = int(input("Your guess: "))
        if guess < number:
            print("Too low.")
            count += 1
        elif guess > number:
            print("Too high.")
            count += 1
        elif guess == number:
            print("You guessed it in " + str(count) + " tries.\n")
            wins += 1
            print("You have won ", wins, "games")
            return wins
    else:
        print("Sorry. You ran out of guesses. The number was", number)

def main():
    display_title()
    get_name()
    wins = 0
    again = "y"
    while again.lower() == "y":
        wins = play_game(wins)
        again = input("Would you like to play again? (y/n): ")
        print()
    print("Bye!")

# if started as the main module, call the main function
if __name__ == "__main__":
    main()
