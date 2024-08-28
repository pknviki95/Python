'''
Program-14:Write a  program to check if the given number is prime or not:
'''

input_number=int(input("Enter the number: "))

is_prime=True

if input_number<=1:
    print("The number is not prime number")

else:
    for iteration in range(2,input_number):
        # prime number logic - number if divided by other number then it is not prime.
        if input_number%iteration==0:
            is_prime=False
            break
if is_prime==True:
    print("The number is prime number")
if is_prime==False:
    print("The number is not prime number")