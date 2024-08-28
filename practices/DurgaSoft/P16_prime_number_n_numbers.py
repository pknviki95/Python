'''
Program-16: Write a  program to list of prime numbers for n:
'''

input_number=int(input("Enter the number: "))

initial_value=2
count=0

while True:
    is_prime=True
    for iteration in range(2,initial_value//2+1):
        if initial_value%iteration==0:
            is_prime=False
            #print(f"{initial_value} is Not prime")
            break
    if is_prime==True:
        print(f"{initial_value} is prime",)
        count+=1
    if count==input_number:
        break
    initial_value+=1