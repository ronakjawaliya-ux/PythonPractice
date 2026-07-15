# ---------------------------
def new_game():

    guesses = []
    correct_guesses = 0
    question_num = 1

    for key in questions:
        print("--------------------------")
        print(key)
        for i in options[question_num-1]:
            print(i)

        guess = input("Enter your guess(A, B): ")
        guess = guess.upper()
        guesses.append(guess)

        correct_guesses += check_answer(questions.get(key), guess)
        question_num += 1

    return correct_guesses, guesses

# ---------------------------
def check_answer(answer, guess):

    if answer == guess:
        print("CORRECT!")
        return 1
    else:
        print("WRONG!")
        return 0
# ---------------------------
def display_score(correct_guesses, guesses):
    print("---------------------------")
    print("RESULTS")
    print("---------------------------")

    print("Answers: ", end="")
    for i in questions:
        print(questions.get(i), end=" ")
    print()

    print("Guesses: ", end="")
    for i in guesses:
        print(i, end=" ")
    print()

    score = int((correct_guesses/len(questions))*100)
    print("Your score is: "+str(score)+"%")


# ---------------------------
def play_game():

    response = input("Do you want to play again? (YES or NO): ")
    response = response.upper()

    if response == "YES":
        return True
    else:
        return False
# ---------------------------


questions = {
    'What is the capital of India?': "A",
    'Who was the first PM of India?': "B",
    'Who is the worst PM of India?': "B"
}

options =[["A. New Delhi","B. Mumbai"],
          ["A. Rajendra Prasad","B. Jawaharlal Nehru"],
          ["A. None","B. Narendra Modi"]]

correct_score, final_guesses = new_game()
display_score(correct_score, final_guesses)

while play_game():
    correct_score, final_guesses = new_game()
    display_score(correct_score, final_guesses)

print("GAME OVER!")



