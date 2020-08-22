import random, json

question1 = json.loads(open('question1.json').read())
question2 = json.loads(open('question2.json').read())
question3 = json.loads(open('question3.json').read())
question4 = json.loads(open('question4.json').read())
question5 = json.loads(open('question5.json').read())

def newQuestion5():
    newQuestion5 = input("What is the first question?\n")
    with open('question5.json') as nameFile:
        json.dump(newQuestion5, nameFile)
    questionCheck()

def newQuestion4():
    newQuestion4 = input("What is the first question?\n")
    with open('question4.json') as nameFile:
        json.dump(newQuestion4, nameFile)
    questionCheck()

def newQuestion3():
    newQuestion3 = input("What is the first question?\n")
    with open('question3.json') as nameFile:
        json.dump(newQuestion3, nameFile)
    questionCheck()

def newQuestion2():
    newQuestion2 = input("What is the first question?\n")
    with open('question2.json') as nameFile:
        json.dump(newQuestion2, nameFile)
    questionCheck()

def newQuestion1():
    newQuestion1 = input("What is the first question?\n")
    with open('question1.json') as nameFile:
        json.dump(newQuestion1, nameFile)
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

