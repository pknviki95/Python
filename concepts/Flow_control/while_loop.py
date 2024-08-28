'''
while loop:

- while loop we can execute a set of statements as long as a condition is ```true```.

syntax:

while [condition=True]:
    statement
'''

initial_value=0

while initial_value<=10:
    print(" current value Inside while loop: ",initial_value)
    
    # Incrementing the initial value
    initial_value+=1
print("Exiting while loop as it fails in condition after last execution value : ",initial_value)