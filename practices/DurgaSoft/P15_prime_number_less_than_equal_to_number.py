'''
Program-15:Write a  program to check if the given number less than equal to number is prime or not:
'''

input_number=int(input("Enter the number: "))

initial_value=2

while initial_value<=input_number:
    is_prime=True
    for iteration in range(2,initial_value//2+1):
        if initial_value%iteration==0:
            is_prime=False
            break
    if is_prime==True:
        print("Prime numbers: ",initial_value)
    initial_value=initial_value+1