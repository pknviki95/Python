'''
break in Nested loop:

- If break is declared in nested loop it terminates the loop to which it is declared and executes the outer loop.

syntax:

for iteration-1 in sequence-1:
    for iteration-2 in sequence-2:
        if [condition=True]:
            break
'''


for iteration_1 in range(3):
    print("current outer loop iteration_1 value: ",iteration_1)
    for iteration_2 in range(2):
        print("current inner loop iteration_2 value: ",iteration_2)
        if iteration_1==iteration_2:
            print(f"Executing break as iteration_1 value: {iteration_1} == iteration_2 value :{iteration_2}")
            
            # break inside inner loop - terminates and exit to outer loop
            break
        
        print(f"current outer loop iteration_1 value: {iteration_1} with its current inner loop iteration_2 value: {iteration_2}")