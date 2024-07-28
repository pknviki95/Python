'''
### eval():

- ```eval()``` function evaluates the specified expression.
- It evaluates input function based on the argument passed.

`
            eval('expression argument')

'''
# input():

input_values=input("Enter the input_values: ")
print("Type of input_values: ",type(input_values))

# eval(input())

eval_values=eval(input("Enter the eval_values: " ))
print("Type of eval_values: ",type(eval_values))

# eval expression:

eval_exp=eval('10+20+30')
print("The value of eval_exp: ",eval_exp)