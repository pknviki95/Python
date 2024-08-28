'''
Program-07: Write a  program to find given number is between the range of 1 to 100:

'''

input_number=int(input("Enter the number: "))

if input_number in range(1,101):
    print(f"The number {input_number} is between 1 to 100")
else:
    print(f"The number {input_number} is outside the range of 1 to 100")