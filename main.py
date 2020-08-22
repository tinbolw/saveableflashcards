import random, json

question1 = json.loads(open('question1.json').read())
question2 = json.loads(open('question2.json').read())
question3 = json.loads(open('question3.json').read())
question4 = json.loads(open('question4.json').read())
question5 = json.loads(open('question5.json').read())

def askQuestion():


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


