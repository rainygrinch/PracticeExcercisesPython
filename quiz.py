# a dictionary that stores questions and answers
# include variable to track the score of the player
# loop through dictionary using the key values pairs
# display each question to the user and allow them to answer
# tell the user if they are right or wrong
# show final result when quiz is completed



# set dictionary of questions and answer
quiz = {
    "question1": {
        "question": "What is the capital of France?",
        "answer": "Paris"
    },
    "question2": {
        "question": "What is the Capital of Germany?",
        "answer": "Berlin"
    },
    "question3": {
        "question": "What is the cpaital of Italy",
        "answer": "Rome"
    },
    "question4": {
        "question": "What is the capital of England?",
        "answer": "London"
    },
    "question5": {
        "question": "What is the Capital of Luxembourg?",
        "answer": "Luxembourg"
    },
    "question6": {
        "question": "What is the Capital of Wales",
        "answer": "Cardiff"
    },
}

# set score to 0
score = 0

# for loop to cycle through questions and request user input
for key, value in quiz.items():
    print(value["question"])
    answer = input("Answer?")

# check if answer is correct, change all to lower to counter case sensitive errors
    if answer.lower() == value["answer"].lower():
        print("Correct")
        score = score + 1
        print("Your score is: " + str(score))
        print("")
        print("")

# if answer incorrect, display corect answer
    else:
        print("Wrong answer!")
        print("The correct answer is: " + str(value["answer"]))
        print("Your score is: " + str(score))
        print("")
        print("")


# print final score and % correct
print("Your final score is " + str(score) + " out of 6 questions correctly")
print("Your percentage is " + str(int(score/7 * 100)) + "%")