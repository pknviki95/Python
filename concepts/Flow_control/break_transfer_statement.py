'''
break statement:

- break statement in Python is used to exit a loop prematurely when a specific condition is met. 
- It can be used within both for and while loops. 
- When break is encountered, the loop stops immediately, and the program continues with the next statement following the loop.

syntax:

for loop:

for iteration in sequence:
    if [condition=True]:
        break

while loop:

while [condition=True]:
    if [condition=True]:
        break

'''

#### for loop:

for iteration in range(10):
    print("current iteration value inside while loop: ",iteration)

    if iteration==7:
        print(f"Iteration value: {iteration} met with condition inside for loop ; Execute break statement as defined below")
        break
print(f"Executed break as iteration value is : {iteration}; Exited the for loop") 

#### while loop:

initial_value=0

while initial_value<=10:
    print("current initial value inside while loop: ",initial_value)
    if initial_value==7:
        print(f"initial value: {initial_value} met with condition inside while loop ; Execute break statement as defined below")
        break
    initial_value+=1
print(f"Executed break as initial value is : {initial_value}; Exited the while loop") 