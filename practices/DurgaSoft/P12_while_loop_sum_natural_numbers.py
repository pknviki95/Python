'''
Program-12:Write a  program to return sum of n natural numbers

sum of n natural number formula:
         n(n+1)/2
'''

input_numbers=int(input("Enter the number: "))

sum_value=0
incremental_value=1
while incremental_value<=input_numbers:
    sum_value+=incremental_value
    incremental_value+=1
print("Sum of n value: ",sum_value)