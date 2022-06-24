""" FAULTY CALCULATOR """
""" THIS IS A FAULTY CALCULATOR WHICH WILL CORRECTLY SOLVE ALL THE PROBLEMS EXCEPT THE FOLLOWING ONES : (45 * 3 = 555) , (56 + 9 = 77) , (56/6 = 4) """
# showing the operators
print("Please Type in the Math Operation you want to do : \n"
      "+ : for addition \n"
      "- : for subtraction \n "
      "* : for multiplication \n"
      "/ : for Division \n"
      "** : for Power \n"
      "% : for modulos")

# taking inputs
varoperator = input("What you want to do : ")
num1 = int(input("Enter your 1st Number : "))
num2 = int(input("Enter your 2nd Number : "))
# main logic
if varoperator == "+" :
    if num1 == 56 and num2 == 9 :
        print("56 + 9 = 77")
    else :
        print(num1, " + ", num2, " = ", num1 + num2)
elif varoperator == "-" :
    print(num1, " - ", num2, " = ", num1 - num2)
elif varoperator == "*" :
    if num1 == 45 and num2 == 3 :
        print("45 * 3 = 555")
    else :
        print(num1, " * ", num2, " = ", num1 * num2)
elif varoperator == "/" :
    if num1 == 56 and num2 == 6 :
        print("56 / 6 = 4")
    else :
        print(num1, " / ", num2, " = ", num1 / num2)
elif varoperator == "**" :
    print(num1, " ** ", num2, " = ", num1 ** num2)
elif varoperator == "%" :
    print(num1, " % ", num2, " = ", num1 % num2)
else :
    print("Invalid Operator use a operator shown in the starting of the program")
