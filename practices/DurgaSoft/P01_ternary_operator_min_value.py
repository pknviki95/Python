'''
Program - 01 - Write a  program to find a min value using ternary operator with two user input

### Syntax:
            [True value] if [condition] else [false value]

'''

value_1=int(input("Enter value 1: "))
value_2=int(input("Enter value 2: "))

# [True value] if [condition] else [false value]

min_value =  value_1 if value_1<value_2  else value_2

print("The minimum value: ",min_value)