# deifne the functions needed, add, sub, mul and div
# print options to user
# get user input
# call the functions
# while loop to continue the program until the user wants to exit

#define addition method
def add(a, b):
    answer = a + b
    print(str(a)+ " + " + str(b) + " = " + str(answer) + "\n")

#define subtraction method
def sub(a, b):
    answer = a - b
    print(str(a) + " - " + str(b) + " = " + str(answer) + "\n")

#define multiplication method
def mul(a, b):
    answer = a * b
    print(str(a) + " * " + str(b) + " = " + str(answer) + "\n")

#define division method
def div(a, b):
    answer = a / b
    print(str(a) + " / " + str(b) + " = " + str(answer) + "\n")

# set while loop so program does not end after one interation, requires user exit action (option e)
while True:

#print user input option
    print("A. Addition")
    print("B. Subtraction")
    print("C. Multiplication")
    print("D. Division")
    print("E. Exit")

#get input from user, assign to variable "choice"
    choice = input("Input your choice of operator:")

#use user input (choice) to call relevant function (+ - * /)
    if choice == "a" or choice == "A":
        print("Addition selected")
        a = int(input("Input First Number: "))
        b = int(input("Input Second Number: "))
        add(a, b)

    elif choice == "b" or choice == "B":
        print("Subtraction selected")
        a = int(input("Input First Number: "))
        b = int(input("Input Second Number: "))
        sub(a, b)

    elif choice == "c" or choice == "C":
        print("Multiplication selected")
        a = int(input("Input First Number: "))
        b = int(input("Input Second Number: "))
        mul(a, b)

    elif choice == "d" or choice == "D":
        print("Division selected")
        a = int(input("Input First Number: "))
        b = int(input("Input Second Number: "))
        div(a, b)

    elif choice == "e" or choice == "E":
        print("Program Exited")
        quit()



