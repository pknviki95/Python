'''
Initialization of variable:

- If you are trying to perform any operations for a variable without initializing throws error - ```Name error``` 

'''

list_numbers=eval(input("Enter the list of numbers: "))

'''
commenting empty global variable initialization 
To understand the non-initialization - Name error
'''
# sum_value=0

for numbers in list_numbers:

    # Arithmetic and Assign operator to perform sum
    # Without Initialization it throws error - Name error
    
    sum_value+=numbers

print(sum_value)