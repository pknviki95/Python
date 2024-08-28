'''
Nested loop:

- Nested loops in Python are loops inside other loops. 
- The inner loop runs completely each time the outer loop runs one iteration. 
- Nested loops are useful for working with multi-dimensional data structures, performing repeated actions on elements, and solving complex problems like matrix multiplication.

syntax:


for iteration-1 in sequence-1:
    for iteration-2 in sequence-2:
        statement

'''

for iteration in range(3):
    print("outer loop value:",iteration)
    for iter in range(2):
            print(f"Inner loop for outer loop value {iteration}: ",iter)
