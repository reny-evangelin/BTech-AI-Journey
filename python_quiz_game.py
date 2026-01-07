# Python Quiz Game

questions = ("Which process do plants use to make their own food using sunlight?: ",
             "Which planet is known as the Red Planet?: ",
             "What is the name of the imaginary line that divides the Earth into Northern and Southern Hemispheres?: ",
             "Which is the longest river in the world?: ",
             "How many bones are there in an adult human body?: ")

options = (("A. Respiration","B. Photosynthesis","C. Evaporation","D. Digestion"),
           ("A. Venus","B. Jupiter","C. Mars","D. Saturn"),
           ("A. Prime Meridian","B. Tropic of Cancer","C. Equator","D. Arctic Circle"),
           ("A. Amazon River","B. Nile River","C. Yangtze River","D. Mississippi River"),
           ("A. 105","B. 300","C. 206","D. 215"))

answers = ("B", "C", "C", "B", "C")
guesses = []
question_num = 0
scores = 0

for question in questions:
    print("------------------")
    print(question)
    for option in options[question_num]:
        print(option)
     
    guess = input("Enter the Correct Answer (A/B/C/D): ").upper()
    guesses.append(guess)
    if guess == answers[question_num]:
        scores += 1
        print("CORRECT")
    else:
        print("INCORRECT")
        print(f"{answers[question_num]} is the correct answer")
    question_num += 1

print("-----------------------")
print("         RESULT        ")
print("-----------------------")

print("Answers: ", end="")
for answer in answers:
    print(answer, end=" ")
print()

print("Guesses: ", end="")
for guess in guesses:
    print(guess, end=" ")
print()

scores = (scores / len(questions)) * 100

print("------------------------------")
print(f"Your total score is {scores}%")
