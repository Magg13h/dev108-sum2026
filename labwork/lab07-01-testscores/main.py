# Starting file for Exercise 6.1 in our textbook

def display_welcome():
    print("The Test Scores program")
    print("Enter 'x' to exit")
    print("")

def get_scores():
    scores = []

    while True:
        score = input("Enter test score: ")

        if score == "x":
            return scores

        score = int(score)

        if score >= 0 and score <= 100:
            scores.append(score)
        else:
            print("Test score must be from 0 through 100. " +
                      "Score discarded. Try again.")

def process_scores(scores):
    # calculate average score
    score_total = 0

    for score in scores:
        score_total += score

    count = len(scores)

    average = score_total / count
                
    # format and display the result
    print()
    print("Score total:       ", score_total)
    print("Number of Score:  ", count)
    print("Average Score:     ", average)

def main():
    display_welcome()
    scores = get_scores()
    process_scores(scores)
    print("")
    print("Bye!")

# if started as the main module, call the main function
if __name__ == "__main__":
    main()
