try:
    import math_function as m

    userName = input('Please enter your user name: ')

    userScore = int(m.getUserScore(userName))

    if userScore == -1:
        newUser = True
        userScore = 0
    else:
        newUser = False

    userChoice = ''   # ✅ always defined

    while userChoice != '-1':
        userScore += m.generateQuestion()
        print("Current Score =", userScore)

        userChoice = input('Press Enter to continue or -1 to exit: ')

    m.updateUserPoints(newUser, userName, str(userScore))

except Exception as e:
    print('An unexpected error occurred. Program will be exited')
    print("Error:", e)   # ✅ VERY IMPORTANT for debugging
