'''
Program-11: Write a  program to print numbers from 1 to 20 that is divisible by 3:

'''

initial_value=1

while initial_value<=20:
    if initial_value%3==0:
        print("Current initial value that is divisible by 3: ",initial_value)
    initial_value+=1

print("Exiting while loop as it fails in condition after last execution value : ",initial_value)