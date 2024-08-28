'''
continue statement:

- continue statement terminates execution of the statements in the current iteration of the current or labeled loop. 
- And it continues execution of the loop with the next iteration.

syntax:

for loop:

for iteration in sequence:
    if [condition=True]:
       continue

while loop:

while [condition=True]:
    if [condition=True]:
       continue

'''
for iteration in range(10):
    if iteration%2==0:
        print("Executing continue statement inside iteration as it satisfies above condition: ",iteration)
        
        # continue statement - To exit current iteration
        continue

    print("Executed outside iteration as condition is not met for continue statement: ",iteration)

#### while loop:

value=0

while value<10:
    
    value+=1
    
    if value%2==0:
        print("Executing continue statement inside iteration as it satisfies above condition: ",value)
        
        # continue statement - To exit current iteration
        continue
        
    print("Executed outside iteration as condition is not met for continue statement: ",value)