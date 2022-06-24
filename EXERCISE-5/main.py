""" Health Management System """
# Programm Creation Steps :)
# 3 Clients - Vanshika, Nishant and Rohan
# Total 6 Files
# Write a Function that take input as Client Name
# One More Function to retrative exercise or food for the client
def getdatetime():
    import datetime
    return datetime.datetime.now()

client = input("Enter your Name : ")
task = input( f"Welcome {client.capitalize()} Which task you want to access [i.e. Food or Exercise] : ")
print(f"You Entered in the {task.capitalize()} Task")

""" Logic for Opening the File of the Correct User """
# Opening Files for Client : 1
if (client.lower() == "vanshika"):
    if (task.lower() == "food"):
        filepointer = open("Exercises\\Exercise-5\\food.vanshika.txt", "r+")

    elif (task.lower() == "exercise"):
        filepointer = open("Exercises\\Exercise-5\\exercise.vanshika.txt", "r+")

# Opening Files for Client : 2
elif (client.lower() == "nishant"):
    if (task.lower() == "food"):
        filepointer = open("Exercises\\Exercise-5\\food.nishant.txt", "r+")

    elif (task.lower() == "exercise"):
        filepointer = open("Exercises\\Exercise-5\\exercise.nishant.txt", "r+")
        
# Opening Files for Client : 3
elif (client.lower() == "rohan"):
    if (task.lower() == "food"):
        filepointer = open("Exercises\\Exercise-5\\food.rohan.txt", "r+")

    elif (task.lower() == "exercise"):
        filepointer = open("Exercises\\Exercise-5\\exercise.rohan.txt", "r+")

# If Client Name is Wrong
else :
    print("Enter a Valid Client Name")
    exit()

""" Functions to Read or Update Data in the Files"""
def readdata():
    print(filepointer.read())

""" Function to Update Data in the File """
def updatedata(data):
    content = f"[{str(getdatetime())}] - {data}\n"
    read = filepointer.read()
    charactersadded = filepointer.write(content)
    if(charactersadded > 0):
        print("Data Submitted Successfuly")
    else :
        print("Something Went Wrong")


""" Logic for calling the function according to the user input """
mode = input("You want to Log or Retrative : ")

if(mode.lower() == "retrative"):
    readdata()
elif(mode.lower() == "log"):
    if (task.lower() == "food"):
        foodeaten = input("What you eated : ")
        data = f"{client.capitalize()} Eaten {foodeaten.capitalize()}"
    elif (task.lower() == "exercise"):
        exerciseperformed = input("Which Exercise you performed : ")
        data = f"{client.capitalize()} did {exerciseperformed.capitalize()}"

    updatedata(data)
else :
    print("Enter a Lock or Retrative only")
    exit()

filepointer.close()
