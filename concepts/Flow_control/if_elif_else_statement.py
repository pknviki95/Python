'''
If elif else conditional statements:

- If elif else conditional statement to control the flow of execution of program based on the condition passed in if elif else statement.
- The execution of statements takes place if the condition in if statements is True. 
- It executes the elif statement if the condition in if statements is False . 
- It executes the else statement if the condition in if and elif statements is False.

if [condition]:
    statements
elif [condition]:
    statements
else:
    statements

'''

input_value=input("Enter the value: ")

if input_value=='viki':
    print(f"Hi {input_value};How are you!!!")
elif input_value=='karthi':
    print(f"Hi {input_value};How are you!!!")
else:
    print(f"Hi {input_value};Who are you!!!")