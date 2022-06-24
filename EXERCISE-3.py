""" Number Guessing Game """
""" GAME RULES """
# Limited Guesses : 5

defaultNum = 18
attempts = 1
print("----------- Number Guessing Game -----------")
while (attempts <= 5): 
    userinput = int(input("Guess the Number : "))
    if (userinput == defaultNum) :
        print("You won !!! in ", attempts, "Guesses")
        break
    elif (userinput > defaultNum) :
        print("Your Number is Greater than the default Number")
        print("Number of Guesses Left : ", 5 - attempts)
        attempts+=1
        continue
    elif (userinput < defaultNum) :
        print("Your Number is lesser than the default Number")
        print("Number of Guesses Left : ", 5 - attempts)
        attempts+=1
        continue

if(attempts > 5) :
    print("Game Over : Your Guesses are Finished")
