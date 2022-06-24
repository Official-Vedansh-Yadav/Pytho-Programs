""" Pattern Printing """
# This programm print stars in ascending order if user inputs true and print stars in descending order if user inputs false

# This variable contain the Number of Rows You want to print
n = int(input("Enter the Number of Rows You Want : \n"))

# This variable will take a number 1 or 0 and converts it into true or false
bol = bool(int(input("Enter 1 for True or 0 for False : \n")))

if (bol == True):
    zero = 1
    while (zero <= n):
        print(zero * "*")
        zero = zero + 1
elif (bol == False):
    while (n >= 1):
        print(n * "*")
        n = n - 1
