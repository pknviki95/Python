'''
Program-06: Write a  program to find smallest and biggest number using if else statements:

'''

number_1=int(input("Enter the number-1: "))
number_2=int(input("Enter the number-2: "))

if number_1>number_2:
    print(f"{number_1} is the biggest Number and {number_2} is the Smallest Number")
elif number_2>number_1:
    print(f"{number_2} is the biggest Number and {number_1} is the Smallest Number")
else:
    print("Numbers are equal")