import random, json
score = 0

question1 = json.loads(open('questions/question1.json').read())
question2 = json.loads(open('questions/question2.json').read())
question3 = json.loads(open('questions/question3.json').read())
question4 = json.loads(open('questions/question4.json').read())
question5 = json.loads(open('questions/question5.json').read())
answer1 = json.loads(open('answers/answer1.json').read())
answer2 = json.loads(open('answers/answer2.json').read())
answer3 = json.loads(open('answers/answer3.json').read())
answer4 = json.loads(open('answers/answer4.json').read())
answer5 = json.loads(open('answers/answer5.json').read())

def askQuestion5():
    global score, answer5
    if question5 == " ":
        print("No question 5 was found")
        quit()
    answer = input(question1 + "\n")
    if answer == answer5:
        print("Correct!\n")
        score += 1
        score = str(score)
        print("You got " + score + "/5 correct!")
    else:
        print("Incorrect!\n")
        score = str(score)
        print("You got " + score + "/5 correct!")

def askQuestion4():
    global score, answer4
    if question4 == " ":
        print("No question 4 was found")
        quit()
    answer = input(question4 + "\n")
    if answer == answer4:
        print("Correct!\n")
        score += 1
        askQuestion5()
    else:
        print("Incorrect!\n")
        askQuestion5()

def askQuestion3():
    global score, answer3
    if question3 == " ":
        print("No question 3 was found")
        quit()
    answer = input(question3 + "\n")
    if answer == answer3:
        print("Correct!\n")
        score += 1
        askQuestion4()
    else:
        print("Incorrect!\n")
        askQuestion4()

def askQuestion2():
    global score, answer2
    if question2 == " ":
        print("No question 2 was found")
        quit()
    answer = input(question2 + "\n")
    if answer == answer2:
        print("Correct!\n")
        score += 1
        askQuestion3()
    else:
        print("Incorrect!\n")
        askQuestion3()

def askQuestion1():
    global score, answer1
    if question1 == " ":
        print("No question 1 was found")
        quit()
    answer = input(question1 + "\n")
    if answer == answer1:
        print("Correct!\n")
        score += 1
        askQuestion2()
    else:
        print("Incorrect!\n")
        askQuestion2()

def askReady():
    ready = input("Are you ready? (Yes/No/Change Question (C))\n")
    if ready == "Yes" or ready == "yes" or ready == "Y" or ready == "y":
        askQuestion1()
    elif ready == "No" or ready == "no" or ready == "N" or ready == "n":
        quit()
    elif ready == "C" or ready == "c":
        changeQuestion()
    else:
        print("Invalid Selecion\n")
        askReady()


def changeQuestion():
    questionNum = input("What question would you like to change?\n")
    questionNum = int(questionNum)
    if questionNum == 1:
        newQuestion1()
    elif questionNum == 2:
        newQuestion2()
    elif questionNum == 3:
        newQuestion3()
    elif questionNum == 4:
        newQuestion4()
    elif questionNum == 5:
        newQuestion5()
    else:
        print("Invalid Selection")
        changeQuestion()


def newQuestion5():
    newQuestion5 = input("What is the fifth question?\n")
    with open('questions/question5.json', 'w') as nameFile:
        json.dump(newQuestion5, nameFile)
    newAnswer5 = input("What is the answer?\n")
    with open('answers/answer5.json', 'w') as nameFile:
        json.dump(newAnswer5, nameFile)
    print("Rerun program for changes to take effect")
    quit()
    askReady()

def newQuestion4():
    newQuestion4 = input("What is the fourth question?\n")
    with open('questions/question4.json', 'w') as nameFile:
        json.dump(newQuestion4, nameFile)
    newAnswer4 = input("What is the answer?\n")
    with open('answers/answer4.json', 'w') as nameFile:
        json.dump(newAnswer4, nameFile)
    print("Rerun program for changes to take effect")
    quit()
    askReady()

def newQuestion3():
    newQuestion3 = input("What is the third question?\n")
    with open('questions/question3.json', 'w') as nameFile:
        json.dump(newQuestion3, nameFile)
    newAnswer3 = input("What is the answer?\n")
    with open('answers/answer3.json', 'w') as nameFile:
        json.dump(newAnswer3, nameFile)
    print("Rerun program for changes to take effect")
    quit()
    askReady()

def newQuestion2():
    newQuestion2 = input("What is the second question?\n")
    with open('questions/question2.json', 'w') as nameFile:
        json.dump(newQuestion2, nameFile)
    newAnswer2 = input("What is the answer?\n")
    with open('answers/answer2.json', 'w') as nameFile:
        json.dump(newAnswer2, nameFile)
    print("Rerun program for changes to take effect")
    quit()
    askReady()

def newQuestion1():
    newQuestion1 = input("What is the first question?\n")
    with open('questions/question1.json', 'w') as nameFile:
        json.dump(newQuestion1, nameFile)
    newAnswer1 = input("What is the answer?\n")
    with open('answers/answer1.json', 'w') as nameFile:
        json.dump(newAnswer1, nameFile)
    print("Rerun program for changes to take effect")
    quit()
    askReady()


askReady()