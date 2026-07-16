print("Fun Math Quiz")
print()
    # first make sure they want to play
ans = input("Would you like to take the quiz? Enter y/n ")
if ans.lower() == "y":
    print("Okay, let's get started!")
    # initialize a counter to track correct answers
    counter = 0
    # math quiz questions go here
    #Q1
    q1 = int(input("Math question 1: What is 5 x 5?"))
    if q1 == 25:
        print("Great job! You got it correct!")
        counter += 1
    else:
        print("Sorry, that is incorrect. The answer was 25.")
    #Q2
    q2 = int(input("Math question 2: What is 100 / 4?"))
    if q2 == 20:
        print("Great job! You got it correct!")
        counter += 1
    else:
        print("Sorry, that is incorrect. The answer was 20.")
    #Q3
    q3 = int(input("Math question 3: What is 20 + 20?"))
    if q3 == 40:
        print("Great job! You got it correct!")
        counter += 1
    else:
        print("Sorry, that is incorrect. The answer was 40.")
    #Q4
    q4 = int(input("Math question 4: What is 200 - 100?"))
    if q4 == 100:
        print("Great job! You got it correct!")
        counter += 1
    else:
        print("Sorry, that is incorrect. The answer was 100.")
    #Q5
    q5 = int(input("Math question 5: What is 10 x 10?"))
    if q5 == 100:
        print("Great job! You got it correct!")
        counter += 1
    else:
        print("Sorry, that is incorrect. The answer was 100.")
    print("Your score is:", counter)
    print("Thanks for playing!")

elif ans.lower() == "n":
    print("Sorry, Maybe next time")
else:
    print("Invalid enrty. Please restart.")