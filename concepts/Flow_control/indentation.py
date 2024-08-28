'''
Indentation in python:

- Python indentation refers to adding white space before a statement to a particular block of code. 
- (i.e) All the statements with the same space to the left, belong to the same code block.

if [condition]:
    statement-1
    statement-2
print(statement-3)

'''

x=int(input("Enter X value: "))
y=int(input("Enter Y value: "))

if x>y:
    
    # Inside indentation scope

    print("X is greater than y - Indented block")
    print("Inside first conditional statement")
if x<y:
    
    # Inside indentation scope

    print("X is greater than y - Indented block")
    print("Inside Second conditional statement")

# Outside indentation scope

print("Wrong statement- Not Indented block")