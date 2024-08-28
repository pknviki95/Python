'''
#### Program-10: Write a  program to print sum of numbers in list sequence:
'''

list_numbers=eval(input("Enter the list of numbers: "))

# empty global variable initialization

sum_value=0

for numbers in list_numbers:

    # Arithmetic and Assign operator to perform sum
    # sum_value= 0+[list values]
    sum_value+=numbers

print("sum of list values: ",sum_value)