from functions import question, bonus_question, get_valid_input

print()

def main():
    """
    Runs a multiplication math test with 5 questions, keeps track of the score, and offers a bonus divison question
    if the user scores 5/5.

    """

    score = 0

    for i in range(5):
        num_1, num_2, answer = question()
        print(f"Question {i + 1}/5: {num_1} × x = {answer}")
        user_input = get_valid_input("What is the value of x?: ")

        if user_input == num_2:
            print("Well done!")
            score += 1
        else:
            print(f"Wrong, sorry. The correct value of x is {num_2}.")
        print()  

    print(f"Your final score is: {score}/5!")
    print()
    if score == 5:  # If user scores 5/5, run the rest of this code
        user_input2 = get_valid_input("Well done for getting 5/5! Enter 1 for a bonus question and any other number to exit!")
        if user_input2 == 1:
            num_1, num_2, answer = bonus_question()
            print(f"{num_1} / y = {answer}")
            user_input = get_valid_input("What is the value of y?: ")

            if float(user_input) == float(num_2): # Float to handle any decimal places.
                print("Well Done! you scored 5/5! and you got the bonus question correct!")
            else:
                print(f"Unlucky!... the correct answer was {num_2}!")
                exit()
        else:
            exit()
        


if __name__ == "__main__":
    main()