import random, json
score = 0

question1 = json.loads(open('question1.json').read())
question2 = json.loads(open('question2.json').read())
question3 = json.loads(open('question3.json').read())
question4 = json.loads(open('question4.json').read())
question5 = json.loads(open('question5.json').read())
answer1 = json.loads(open(answers/answer1.json).read())
answer2 = json.loads(open(answers/answer2.json).read())
answer3 = json.loads(open(answers/answer3.json).read())
answer4 = json.loads(open(answers/answer4.json).read())
answer5 = json.loads(open(answers/answer5.json).read())

def askQuestion1():
    global score, answer1
    print(question1)
    answer = input("What is the answer?\n")
    if answer == answer1:
        print("Correct!\n")
        score += 1
    else:
        print("Incorrect!\n")

def askReady():
    ready = input("Are you ready? (Yes/No/Change Question (C)\n")
    if ready == "Yes":
        askQuestion1()
    elif ready == "No":
        quit()
    elif ready == "C":
        changeQuestion()
    else:
        print("Invalid Selecion\n")
        askReady()


def changeQuestion():
    questionNum = input("What question would you like to change?\n")
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
    with open('questions/question5.json') as nameFile:
        json.dump(newQuestion5, nameFile)
    newAnswer5 = input("What is the answer?\n")
    with open('answers/answer5.json') as nameFile:
        json.dump(newAnswer5, nameFile)
    questionCheck()

def newQuestion4():
    newQuestion4 = input("What is the fourth question?\n")
    with open('questions/question4.json') as nameFile:
        json.dump(newQuestion4, nameFile)
    newAnswer4 = input("What is the answer?\n")
    with open('answers/answer4.json') as nameFile:
        json.dump(newAnswer4, nameFile)
    questionCheck()

def newQuestion3():
    newQuestion3 = input("What is the third question?\n")
    with open('questions/question3.json') as nameFile:
        json.dump(newQuestion3, nameFile)
    newAnswer3 = input("What is the answer?\n")
    with open('answers/answer3.json') as nameFile:
        json.dump(newAnswer3, nameFile)
    questionCheck()

def newQuestion2():
    newQuestion2 = input("What is the second question?\n")
    with open('questions/question2.json') as nameFile:
        json.dump(newQuestion2, nameFile)
    newAnswer2 = input("What is the answer?\n")
    with open('answers/answer2.json') as nameFile:
        json.dump(newAnswer2, nameFile)
    questionCheck()

def newQuestion1():
    newQuestion1 = input("What is the first question?\n")
    with open('questions/question1.json') as nameFile:
        json.dump(newQuestion1, nameFile)
    newAnswer1 = input("What is the answer?\n")
    with open('answers/answer1.json') as nameFile:
        json.dump(newAnswer1, nameFile)
    questionCheck()

def questionCheck():
    global question1
    if question1 == "":
        newQuestion1()
    elif question2 == "":
        newQuestion2()
    elif question3 == "":
        newQuestion3()
    elif question4 == "":
        newQuestion4()
    elif question5 == "":
        newQuestion5()
    elif question1 != "" and question2 != "" and question3 != "" and question4 != "" and question5 != "":


