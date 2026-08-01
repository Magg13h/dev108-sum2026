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
    low = min(scores)
    high = max(scores)
    sorted_scores = sorted(scores)

    if count % 2 == 1:
        median = sorted_scores[count // 2]
    else:
        middle1 = sorted_scores[(count // 2) - 1]
        middle2 = sorted_scores[count // 2]
        median = (middle1 + middle2) / 2

    results = (score_total, count, average, low, high, median)
                
    # format and display the result
    print()
    print("Score total:       ", results[0])
    print("Number of Score:   ", results[1])
    print("Average Score:     ", results[2])
    print("Low score:         ", results[3])
    print("High Score:        ", results[4])
    print("Median Score:      ", results[5])

def main():
    display_welcome()
    scores = get_scores()
    process_scores(scores)
    print("")
    print("Bye!")

# if started as the main module, call the main function
if __name__ == "__main__":
    main()
