from random import randint
from os import remove, rename

def getUserScore(userName):
    try:
        file = open('userScores.txt', 'r')
        for line in file:
            content = line.strip().split(',')
            if content[0] == userName:
                file.close()
                return content[1]

        file.close()
        return "-1"

    except IOError:
        print('\nFile userScores.txt not found. A new file will be created')
        file = open('userScores.txt', 'w')
        file.close()
        return "-1"


def updateUserPoints(newUser, userName, score):

    if newUser:
        file = open('userScores.txt', 'a')
        file.write('\n' + userName + ',' + str(score))
        file.close()

    else:
        file = open('userScores.txt', 'r')
        temp = open('userScores.tmp', 'w')

        for line in file:
            content = line.strip().split(',')
            if content[0] == userName:
                newScore = int(content[1]) + int(score)
                line = content[0] + ',' + str(newScore) + '\n'
            temp.write(line)

        file.close()
        temp.close()

        remove('userScores.txt')
        rename('userScores.tmp', 'userScores.txt')


def generateQuestion():
    operandList = [0] * 5
    operatorList = [''] * 4

    operatorDict = {1: '+', 2: '-', 3: '*', 4: '**'}

    # generate numbers
    for i in range(5):
        operandList[i] = randint(1, 9)

    # generate operators
    for i in range(4):
        operatorList[i] = operatorDict[randint(1, 4)]

    # build expression
    questionString = str(operandList[0])
    for i in range(1, 5):
        questionString += operatorList[i-1] + str(operandList[i])

    # calculate result
    result = eval(questionString)

    # display nicely
    displayString = questionString.replace('**', '^')
    print('\n' + displayString)

    # user input
    userResult = input('Answer: ')

    while True:
        try:
            if int(userResult) == result:
                print('Excellent')
                return 1
            else:
                print("Sorry, wrong answer. The correct answer is", result)
                return 0

        except:
            print('You did not enter a number. Please try again!')
            userResult = input('Answer: ')
