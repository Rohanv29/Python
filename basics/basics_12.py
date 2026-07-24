python_quiz = {
    "Who developed Python?": "Guido van Rossum",
    "In which year was Python first released?": "1991",
    "Which keyword is used to define a function?": "def",
    "Which keyword is used to create a class?": "class",
    "Which data type stores True or False?": "bool",
    "Which function takes input from the user?": "input",
    "Which function displays output?": "print",
    "Which symbol is used for comments in Python?": "#",
    "Which operator is used for exponentiation?": "**",
    "Which keyword is used to import a module?": "import"
}
score = 0

for question, answer in python_quiz.items():
    user = input(question + " ")
    if user.lower() == answer.lower():
        print("Correct!\n")
        score += 1
    else:
        print("Wrong! Correct answer is:", answer, "\n")

print("Your Score:", score, "/", len(python_quiz))