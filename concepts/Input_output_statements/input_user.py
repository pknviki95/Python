'''
- ```input()``` is used to get the user input for the python program.
- input() return type is based on value passed for python 2.X versions.
- input() return type is always string for python 3.X versions.
- To covert the value to other object we need typecasting on user input.

            user_input=input("user_input")
'''


#input()

value=input("Enter the value: ")

print("Type of input user value for python versions 3.X = ",type(value))

print("Type of input user value for python versions 2.X = ",type(value))