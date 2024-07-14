'''
Program-02: Write a  program to find a max value using nested ternary operator with two user input :

    Get two user input value
    If both numbers are equal print "Both Numbers are equal" 
    If first number is lesser than second number print "first number is lesser than second number"
    If first number is greater than second number print "first number is greater than second number"

'''

value_1=int(input("Enter value 1: "))
value_2=int(input("Enter value 2: "))

print("Both Numbers are equal") if value_1==value_2 else print("first number is lesser than second number") if value_1<value_2 else print("first number is greater than second number")