""" GAME : Snake Water Gun """

import random

# Essential Variables
botWin = 0
userWin = 0
index = 0

# Function to show result 
def showresult(botMove, userMove):
    global botWin
    global userWin
    if(botMove == userMove):
        return f"Bot Move : {botMove} and User Move : {userMove} \nGame Result : !!! MATCH TIE !!!"
    elif(botMove == "Snake" and userMove == "Water"):
        botWin += 1
        return f"Bot Move : {botMove} and User Move : {userMove} \nGame Result : !!! BOT WINS !!!"
    elif(botMove == "Water" and userMove == "Snake"):
        userWin += 1
        return f"Bot Move : {botMove} and User Move : {userMove} \nGame Result : !!! User WINS !!!"
    elif(botMove == "Gun" and userMove == "Water"):
        userWin += 1
        return f"Bot Move : {botMove} and User Move : {userMove} \nGame Result : !!! USER WINS !!!"
    elif(botMove == "Water" and userMove == "Gun"):
        botWin += 1
        return f"Bot Move : {botMove} and User Move : {userMove} \nGame Result : !!! BOT WINS !!!"
    elif(botMove == "Gun" and userMove == "Snake"):
        botWin += 1
        return f"Bot Move : {botMove} and User Move : {userMove} \nGame Result : !!! BOT WINS !!!"
    elif(botMove == "Snake" and userMove == "Gun"):
        userWin += 1
        return f"Bot Move : {botMove} and User Move : {userMove} \nGame Result : !!! USER WINS !!!"
    
# Looping the Game 10 Times
while(index < 10):
    print("------------ GAME : Snake Water Gun ------------") # Game Startup text

    moves_possible = ["Snake","Water","Gun"]
    move_computer = random.choice(moves_possible)
    user_input = input("Please Enter your move and write Snake, Water or Gun : ")
    move_user = user_input.capitalize()

    print(showresult(move_computer, move_user))
    index += 1

print(f"GAME RESULTS : BotWins : {botWin} times | | UserWins : {userWin} times")