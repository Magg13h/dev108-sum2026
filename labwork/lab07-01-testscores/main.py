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
    low = None
    high = None 

    for score in scores:
        score_total += score
        if low is None or score < low:
            low = score
        if high is None or score > high:
            high = score
    count = len(scores)
    average = score_total / count
    sorted_scores = sorted(scores)
    mid = count // 2
    if count % 2 == 1:
        median = sorted_scores[mid]
    else:
        median = (sorted_scores[mid - 1] + sorted_scores[mid]) / 2
                
    # format and display the result
    print()
    print("Score total:       ", score_total)
    print("Number of Score:  ", count)
    print("Average Score:     ", average)
    print("Low score:         ", low)
    print("High Score:        ", high)
    print("Median Score:      ", median)

def main():
    display_welcome()
    scores = get_scores()
    process_scores(scores)
    print("")
    print("Bye!")

# if started as the main module, call the main function
if __name__ == "__main__":
    main()
