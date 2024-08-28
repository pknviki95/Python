# Flow control:

- Control flow is the order in which individual statements, instructions, or function calls are executed or evaluated. 
- The control flow of a Python program is regulated by ```conditional statements```, ```loops```, and ```function calls```.
- ```Switch statement```,```do-while```,```goto``` concepts is not available in python.

### Types of flow control:

- **Conditional statements.**
- **Iterative statements.**
- **Transfer statements.**

### Indentation in python:

- Python indentation refers to adding white space before a statement to a particular block of code. 
- (i.e) All the statements with the same space to the left, belong to the same code block.

```python
if [condition]:
    statement-1
    statement-2
print(statement-3)
```
- In above expression ```statement-1```,```statement-2``` is referred to indented statements (i.e) the blocks of code is basically inside conditional statements.
- ```Statement-3``` is not inside the block of code as it is not indented; So it is outside the block of code. 

#### [indentation.py](https://github.com/pknviki95/Python/tree/main/concepts/Flow_control/indentation.py) - Indentation block for executing block of code.

```python
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
```
#### input:
```python
Enter X value: 10
Enter Y value: 20
```
#### output:
```python
X is greater than y - Indented block
Inside Second conditional statement
Wrong statement- Not Indented block
```
- If the indentation inside the conditional statement after ```(:)-colon``` is not declared it throws ```Indentation error```.

#### [indentation_error.py](https://github.com/pknviki95/Python/tree/main/concepts/Flow_control/indentation_error.py) - Indentation block for executing block of code ; If not declared properly throws error - Indentation error.

```python
x=int(input("Enter X value: "))
y=int(input("Enter Y value: "))

if x>y:
    
# Indentation error

print("X is greater than y - Indented block")
```
#### error:

```python
  File "/home/pknviki95/Learning/Python/concepts/Flow_control/indentation_error.py", line 13
    print("X is greater than y - Indented block")
    ^
IndentationError: expected an indented block after 'if' statement on line 10
```
### Conditional statements:

- Conditional Statements are statements in Python that provide a choice for the control flow based on a condition. 
- It means that the control flow of the Python program will be decided based on the outcome of the condition.

### Types of conditional statements:

- **If conditional statements.**
- **If else conditional statements.**
- **Nested if conditional statements.**
- **If elif else conditional statements.**
- **Ternary Expression conditional statements.**

### If conditional statements:

- ```If conditional statement``` to control the flow of execution of program based on the condition passed in if statement.
- The execution of statements takes place if the condition in if statements is ```True```. 

#### syntax:
```python
if [condition]:
    statements
```    
#### [if_conditional_statement.py](https://github.com/pknviki95/Python/tree/main/concepts/Flow_control/if_conditional_statement.py) - If statements to control the flow of execution of program.

```python
input_value=input("Enter the input: ")

if input_value=='viki':
    print(f"Hello {input_value}")

print("How are you!!!")
```
#### if condition satisfies - Executes block of code:

#### input:
```python
Enter the input: viki
```
#### output:

```python
Hello viki
How are you!!!
```
#### if condition not satisfied - Neglects block of code:

#### input:
```python
Enter the input: guru  
```
#### output:  
```python
How are you!!!
```

### If else conditional statements:

- ```If else conditional statement``` to control the flow of execution of program based on the condition passed in if else statement.
- The execution of statements takes place if the condition in if statements is ```True```. 
- It executes the else statement if the condition in if statements is ```False``` . 

#### syntax:
```python
if [condition]:
    statements
else:
    statements
```   

#### [if_else_conditional_statement.py](https://github.com/pknviki95/Python/tree/main/concepts/Flow_control/if_else_conditional_statement.py) - If else statements to control the flow of execution of program.

```python
name=input("Enter the name: ")

if name=='viki':
    print(f"Hello {name};How are you!!!")
else:
    print("Who are you!!!")
```

#### if condition satisfies - Executes if statement block of code:

#### input:

```python
Enter the name: viki
```
#### output:

```python
Hello viki;How are you!!!
```
#### if condition not satisfied - Executes else statement block of code:

#### input:

```python
Enter the name: guru
```
#### output:

```python
Who are you!!!
```

### If elif else conditional statements:

- ```If elif else conditional statement``` to control the flow of execution of program based on the condition passed in if elif else statement.
- The execution of statements takes place if the condition in if statements is ```True```. 
- It executes the elif statement if the condition in if statements is ```False``` . 
- It executes the else statement if the condition in if and elif statements is ```False``` .

#### syntax:
```python
if [condition]:
    statements
elif [condition]:
    statements
else:
    statements
```   

#### [if_elif_else_statement.py](https://github.com/pknviki95/Python/tree/main/concepts/Flow_control/if_elif_else_statement.py) - If elif else statements to control the flow of execution of program.

```python
input_value=input("Enter the value: ")

if input_value=='viki':
    print(f"Hi {input_value};How are you!!!")
elif input_value=='karthi':
    print(f"Hi {input_value};How are you!!!")
else:
    print(f"Hi {input_value};Who are you!!!")
```

#### if condition satisfies - Executes if statement block of code:

#### input:
```python
Enter the value: viki
```
#### output:
```python
Hi viki;How are you!!!
```

#### if condition not satisfied - Executes elif statement block of code:
#### input:
```python
Enter the value: karthi
```
#### output:
```python
Hi karthi;How are you!!!
```

#### if condition and elif condition not satisfied - Executes else statement block of code:

#### input:
```python
Enter the value: raja
```
#### output:
```python
Hi raja;Who are you!!!
```

### Iterative statements:

- In Python, iterative statements allow us to execute a block of code repeatedly as long as the condition is True. 
- We also call it a loop statements.

### Types of Iterative statements:

- **for loop**
- **while loop**

### for loop:

- ```for``` loop is used for iterating over a sequence.
- Iterating sequences  such as a list, a tuple, a dictionary, a set, or a string.
- The execution of iteration takes place based on the number of elements in sequence.

#### syntax:

```python
for iteration in sequence:
    statement
```

#### [for_loop.py](https://github.com/pknviki95/Python/tree/main/concepts/Flow_control/for_loop.py) - Iterating element of sequence using for loop:


#### String iteration:

```python
string_variable='ramnad'

for iter in string_variable:
    print("string_variable elements: ",iter)
```
#### output:
```python
string_variable elements:  r
string_variable elements:  a
string_variable elements:  m
string_variable elements:  n
string_variable elements:  a
string_variable elements:  d
```
#### List iteration:

```python
list_variable=[1,2,3,'viki',{1:'viki'}]

for iter in list_variable:
    print("list_variable elements: ",iter)
```
#### output:
```python
list_variable elements:  1
list_variable elements:  2
list_variable elements:  3
list_variable elements:  viki
```
#### Tuple iteration:

```python
tuple_variable=(1,2,3,'viki')

for iter in tuple_variable:
    print("tuple_variable elements: ",iter)
```
#### output:
```python
tuple_variable elements:  1
tuple_variable elements:  2
tuple_variable elements:  3
tuple_variable elements:  viki
```
#### Set iteration:

```python
set_variable={1,2,3,'viki'}

for iter in set_variable:
    print("set_variable elements: ",iter)
```
#### output:
```python
set_variable elements:  1
set_variable elements:  2
set_variable elements:  3
set_variable elements:  viki
```
#### Dictionary iteration:

```python
dict_variable={1:'viki',2:'raja',3:'bengaluru'}

for iter_key,iter_values in dict_variable.items():
    print("dict_variable key element: " ,iter_key)
    print("dict_variable value element: " ,iter_values)
```
#### output:
```python
dict_variable key element:  1
dict_variable value element:  viki
dict_variable key element:  2
dict_variable value element:  raja
dict_variable key element:  3
dict_variable value element:  bengaluru
```
#### Range iteration:

```python
range_variable=4
for iter in range(0,range_variable):
    print("range_variable elements: ",iter)
```

#### output:
```python
range_variable elements:  0
range_variable elements:  1
range_variable elements:  2
range_variable elements:  3
```

### while loop:

- ```while loop``` we can execute a set of statements as long as a condition is ```true```.

#### syntax:

```python
while [condition=True]:
    statement
```

#### [while_loop.py](https://github.com/pknviki95/Python/tree/main/concepts/Flow_control/while_loop.py) - Executing the statement as long as the condition is True in while loop:


```python
initial_value=0

while initial_value<=10:
    print(" current value Inside while loop: ",initial_value)
    
    # Incrementing the initial value
    initial_value+=1
print("Exiting while loop as it fails in condition after last execution value : ",initial_value)
```

#### output:

```python
 current value Inside while loop:  0
 current value Inside while loop:  1
 current value Inside while loop:  2
 current value Inside while loop:  3
 current value Inside while loop:  4
 current value Inside while loop:  5
 current value Inside while loop:  6
 current value Inside while loop:  7
 current value Inside while loop:  8
 current value Inside while loop:  9
 current value Inside while loop:  10
Exiting while loop as it fails in condition after last execution value :  11
```

#### Explanation:

- ```while initial_value<=10:``` -  This line starts a while loop that will continue to execute as long as the condition ```initial_value <= 10``` remains ```true```. 
- This means the loop will run when initial_value is ```0, 1, 2, ..., up to 10```.

- ```initial_value+=1``` - Incrementing initial_value by ```1``` using the ```+= operator```. 
- This is essential for eventually making the condition of the while loop ```(initial_value <= 10) false```, allowing the loop to terminate.
- once initial_value becomes ```11```, the loop has exited as the condition is false in while loop and shows the final value of initial_value.

### Infinite loop:

- Infinite loop is something that is executed infinitely as the condition is always ```True```.
- Infinite loop Execution can be terminated by ```Keyboard Interrupt``` (i.e)```CTLR+C```.
- Infinite loop can be terminated or exited using ```break``` statement.

#### syntax:

```python
while True:
    statement
```
#### [infinite_loop.py](https://github.com/pknviki95/Python/tree/main/concepts/Flow_control/infinite_loop.py) - Executing the statement as the condition is True always in Infinite loop:

```python
initial_value=1

# condition is always True - Infinite loop

while True:
    print("Hello!")
```

#### output:

```python
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!

^C

Traceback (most recent call last):
  File "/home/pknviki95/Learning/Python/concepts/Flow_control/infinite_loop.py", line 12, in <module>
    print("Hello!")
KeyboardInterrupt
```

### Nested loop:

- Nested loops in Python are loops inside other loops. 
- The inner loop runs completely each time the outer loop runs one iteration. 
- Nested loops are useful for working with multi-dimensional data structures, performing repeated actions on elements, and solving complex problems like matrix multiplication.

#### syntax:

```python
for iteration-1 in sequence-1:
    for iteration-2 in sequence-2:
        statement
```
#### [Nested_loop.py](https://github.com/pknviki95/Python/tree/main/concepts/Flow_control/Nested_loop.py) - Implementing nested loop:


```python
for iteration in range(3):
    print("outer loop value:",iteration)
    for iter in range(2):
            print(f"Inner loop for outer loop value {iteration}: ",iter)
```

#### output:

```python
outer loop value: 0
Inner loop for outer loop value 0:  0
Inner loop for outer loop value 0:  1
outer loop value: 1
Inner loop for outer loop value 1:  0
Inner loop for outer loop value 1:  1
outer loop value: 2
Inner loop for outer loop value 2:  0
Inner loop for outer loop value 2:  1
```

#### Explanation:

**Outer Loop (```for iteration in range(3)```):**

- The outer loop runs ```3``` times, with iteration taking values ```0```,```1```, and ```2```.
- Each time the outer loop runs, it prints the current value of iteration.

**Inner Loop (```for iter in range(2)```):**

- The inner loop runs ```2``` times for each iteration of the ```outer loop```, with iter - taking values 0 and 1.
- During each iteration of the inner loop, it prints the current value of iter along with the current value of the outer loop's iteration.

### Transfer statements:
- Transfer statements alter the way a logic gets executed. These statements are often used in loops for and while.

### Types of Transfer statements:
- **break statement**
- **continue statement**


### break statement:

- ```break``` statement in Python is used to exit a loop prematurely when a specific condition is met. 
- It can be used within both ```for``` and ```while``` loops. 
- When break is encountered, the loop stops immediately, and the program continues with the next statement following the loop.

#### syntax:

#### for loop:


```python
for iteration in sequence:
    if [condition=True]:
        break
```
#### while loop:
```python
while [condition=True]:
    if [condition=True]:
        break
```
    
#### [break_transfer_statement.py](https://github.com/pknviki95/Python/tree/main/concepts/Flow_control/break_transfer_statement.py) - Exiting from loop using ```break``` statement when specific condition is met:

#### for loop:

```python
for iteration in range(10):
    print("current iteration value inside while loop: ",iteration)

    if iteration==7:
        print(f"Iteration value: {iteration} met with condition inside for loop ; Execute break statement as defined below")
        
        # break - to exit the loop
        break

print(f"Executed break as iteration value is : {iteration}; Exited the for loop") 
```
#### output:
```python
current iteration value inside while loop:  0
current iteration value inside while loop:  1
current iteration value inside while loop:  2
current iteration value inside while loop:  3
current iteration value inside while loop:  4
current iteration value inside while loop:  5
current iteration value inside while loop:  6
current iteration value inside while loop:  7
Iteration value: 7 met with condition inside for loop ; Execute break statement as defined below
Executed break as iteration value is : 7; Exited the for loop
```
#### while loop:

```python
initial_value=0

while initial_value<=10:
    print("current initial value inside while loop: ",initial_value)
    if initial_value==7:
        print(f"initial value: {initial_value} met with condition inside while loop ; Execute break statement as defined below")

        # break - to exit the loop
        break
    
    initial_value+=1
print(f"Executed break as initial value is : {initial_value}; Exited the while loop") 
```
#### output:
```python
current initial value inside while loop:  0
current initial value inside while loop:  1
current initial value inside while loop:  2
current initial value inside while loop:  3
current initial value inside while loop:  4
current initial value inside while loop:  5
current initial value inside while loop:  6
current initial value inside while loop:  7
initial value: 7 met with condition inside while loop ; Execute break statement as defined below
Executed break as initial value is : 7; Exited the while loop
```

#### NOTE:
- ```break statement``` should be used within both ```for``` and ```while``` loops. 
- If break statements are used outside the loop it throws ```Syntax error```

#### [break_syntax_error.py](https://github.com/pknviki95/Python/tree/main/concepts/Flow_control/break_syntax_error.py) -  ```break``` statement should be declared within loop if not it throws error - ```Syntax error```:


```python
if value<2:

    # break outside the loop throws error - Syntax error
    break

print("Executed print as break is not declared inside loop")
```

#### error:
```python
  File "/home/pknviki95/Learning/Python/concepts/Flow_control/break_syntax_error.py", line 9
    break
    ^^^^^
SyntaxError: 'break' outside loop
```
### break in Nested loop:

- If break is declared in nested loop it terminates the loop to which it is declared and executes the outer loop.

#### syntax:

```python
for iteration-1 in sequence-1:
    for iteration-2 in sequence-2:
        if [condition=True]:
            break 
```
#### [break_nested_loop.py](https://github.com/pknviki95/Python/tree/main/concepts/Flow_control/break_nested_loop.py) -  ```break``` statement in nested loop it terminates from inner loop to outer loop:

```python
for iteration_1 in range(3):
    print("current outer loop iteration_1 value: ",iteration_1)
    for iteration_2 in range(2):
        print("current inner loop iteration_2 value: ",iteration_2)
        if iteration_1==iteration_2:
            print(f"Executing break as iteration_1 value: {iteration_1} == iteration_2 value :{iteration_2}")
            
            # break inside inner loop - terminates and exit to outer loop
            break
        
        print(f"current outer loop iteration_1 value: {iteration_1} with its current inner loop iteration_2 value: {iteration_2}")
```
#### output:
```python
current outer loop iteration_1 value:  0
current inner loop iteration_2 value:  0
Executing break as iteration_1 value: 0 == iteration_2 value :0
current outer loop iteration_1 value:  1
current inner loop iteration_2 value:  0
current outer loop iteration_1 value: 1 with its current inner loop iteration_2 value: 0
current inner loop iteration_2 value:  1
Executing break as iteration_1 value: 1 == iteration_2 value :1
current outer loop iteration_1 value:  2
current inner loop iteration_2 value:  0
current outer loop iteration_1 value: 2 with its current inner loop iteration_2 value: 0
current inner loop iteration_2 value:  1
current outer loop iteration_1 value: 2 with its current inner loop iteration_2 value: 1
```
### continue statement:
- ```continue``` statement terminates execution of the statements in the current iteration of the current or labeled loop. 
- And it continues execution of the loop with the next iteration.

#### syntax:

#### for loop:

```python
for iteration in sequence:
    if [condition=True]:
       continue
```
#### while loop:

```python
while [condition=True]:
    if [condition=True]:
       continue
```

#### [continue_transfer_statement.py](https://github.com/pknviki95/Python/tree/main/concepts/Flow_control/continue_transfer_statement.py) -  ```continue``` statement executes by terminating the current iteration and executes the next iteration:


#### for loop:

```python
for iteration in range(10):
    if iteration%2==0:
        print("Executing continue statement inside iteration as it satisfies above condition: ",iteration)
        
        # continue statement - To exit current iteration
        continue

    print("Executed outside iteration as condition is not met for continue statement: ",iteration)
```

#### output:
```python
Executing continue statement inside iteration as it satisfies above condition:  0
Executed outside iteration as condition is not met for continue statement:  1
Executing continue statement inside iteration as it satisfies above condition:  2
Executed outside iteration as condition is not met for continue statement:  3
Executing continue statement inside iteration as it satisfies above condition:  4
Executed outside iteration as condition is not met for continue statement:  5
Executing continue statement inside iteration as it satisfies above condition:  6
Executed outside iteration as condition is not met for continue statement:  7
Executing continue statement inside iteration as it satisfies above condition:  8
Executed outside iteration as condition is not met for continue statement:  9
```

#### while loop:

```python
value=0

while value<10:
    
    value+=1
    
    if value%2==0:
        print("Executing continue statement inside iteration as it satisfies above condition: ",value)
        
        # continue statement - To exit current iteration
        continue
        
    print("Executed outside iteration as condition is not met for continue statement: ",value)
```
#### output:
```python
Executed outside iteration as condition is not met for continue statement:  1
Executing continue statement inside iteration as it satisfies above condition:  2
Executed outside iteration as condition is not met for continue statement:  3
Executing continue statement inside iteration as it satisfies above condition:  4
Executed outside iteration as condition is not met for continue statement:  5
Executing continue statement inside iteration as it satisfies above condition:  6
Executed outside iteration as condition is not met for continue statement:  7
Executing continue statement inside iteration as it satisfies above condition:  8
Executed outside iteration as condition is not met for continue statement:  9
Executing continue statement inside iteration as it satisfies above condition:  10
```
#### NOTE:
- ```continue statement``` should be used within both ```for``` and ```while``` loops. 
- If continue statements are used outside the loop it throws ```Syntax error```

#### [continue_syntax_error.py](https://github.com/pknviki95/Python/tree/main/concepts/Flow_control/continue_syntax_error.py) -  ```continue``` statement should be declared within loop if not it throws error - ```Syntax error```:

```python
value=0
if value<2:

    # continue outside the loop throws error - Syntax error
    continue

print("outside iteration")
```
#### error:

```python
  File "/home/pknviki95/Learning/Python/concepts/Flow_control/continue_syntax_error.py", line 10
    continue
    ^^^^^^^^
SyntaxError: 'continue' not properly in loop
```
### continue in Nested loop:

- If continue is declared in nested loop it terminates the current iteration of loop to which it is declared and executes the next iteration loop.

#### syntax:

```python
for iteration-1 in sequence-1:
    for iteration-2 in sequence-2:
        if [condition=True]:
            continue 
```
#### [continue_nested_loop.py](https://github.com/pknviki95/Python/tree/main/concepts/Flow_control/continue_nested_loop.py) -  ```continue``` statement in nested loop it terminates current iteration of inner loop and executes next iteration:

```python
for iteration_1 in range(3):
    print("current outer loop iteration_1 value: ",iteration_1)
    for iteration_2 in range(2):
        print("current inner loop iteration_2 value: ",iteration_2)
        if iteration_1==iteration_2:
            print(f"Executing continue as iteration_1 value: {iteration_1} == iteration_2 value :{iteration_2}")
            
            # continue inside inner loop - terminates current iteration of inner loop and executes next iteration
            continue
        
        print(f"current outer loop iteration_1 value: {iteration_1} with its current inner loop iteration_2 value: {iteration_2}")
```
#### output:
```python
current outer loop iteration_1 value:  0
current inner loop iteration_2 value:  0
Executing continue as iteration_1 value: 0 == iteration_2 value :0
current inner loop iteration_2 value:  1
current outer loop iteration_1 value: 0 with its current inner loop iteration_2 value: 1
current outer loop iteration_1 value:  1
current inner loop iteration_2 value:  0
current outer loop iteration_1 value: 1 with its current inner loop iteration_2 value: 0
current inner loop iteration_2 value:  1
Executing continue as iteration_1 value: 1 == iteration_2 value :1
current outer loop iteration_1 value:  2
current inner loop iteration_2 value:  0
current outer loop iteration_1 value: 2 with its current inner loop iteration_2 value: 0
current inner loop iteration_2 value:  1
current outer loop iteration_1 value: 2 with its current inner loop iteration_2 value: 1
```
### Difference between break and continue in python  
|Feature|break|continue|
|:--|:--|:--|
|```Purpose```|It is used for the termination of all the remaining iterations of the loop.|It is used for the termination of the only current iteration of the loop.|
|```Effect```|It stops the continuation of the loop.|It stops the execution of the current iteration.|
|```Usage Scenario```|When you want to stop the loop based on a condition.|When you want to skip specific iterations but continue looping.|

### loops with else with break statement:

- The else block just after for/while is executed only when the loop is ```NOT``` terminated by a break statement. 

|break|Process| else part executed|
|:--|:--|:--|
|```if [condition=True]:```<br>```break```|- The execution of loop is terminated <br> - else part is not executed|:x:|
|```if [condition=False]```<br>```break```| - The execution of loop is terminated <br> - else part is executed|:heavy_check_mark:|

#### [loops_with_else_break.py](https://github.com/pknviki95/Python/tree/main/concepts/Flow_control/loops_with_else_break.py) -  ```break``` statement with loop if condition met it terminates loop neglecting else execution/executes if condition not met for break in loop:


#### for loop with break statement condition True:

#### syntax:

```python
for iteration in sequence:
        if [condition=True]:
            break
else:
    # else part is not executed as condition for break is True
    statement 
```

```python
list_values_break_True=[2,3,60,90,500,550,250]
for iteration in list_values_break_True:
    print("current iteration value: ",iteration)
    if iteration>500:
        print(f"Current iteration value: {iteration} met condition and executes break statement")
        print("Neglects the else part as break condition =True")
        break
else:
    
    # else part is not executed as condition for break is True

    print(f"else part executed as break is not executed with iteration value: {iteration} as break condition =False")

```
#### output:
```python
current iteration value:  2
current iteration value:  3
current iteration value:  60
current iteration value:  90
current iteration value:  500
current iteration value:  550
Current iteration value: 550 met condition and executes break statement
Neglects the else part as break condition =True
```

#### for loop with break statement condition False:

#### syntax:

```python
for iteration in sequence:
        if [condition=False]:
            break
else:
    # else part is executed as condition for break is False
    statement 
```

```python
list_values_break_False=[2,3,60,90,500,250]
for iteration in list_values_break_False:
    print("current iteration value: ",iteration)
    if iteration>500:
        print(f"Current iteration value: {iteration} met condition and executes break statement")
        print("Neglects the else part as break condition =True")
        break
else:

    # else part is executed as condition for break is False

    print(f"else part executed as break is not executed with iteration value: {iteration} as break condition =False")
```

#### output:
```python
current iteration value:  2
current iteration value:  3
current iteration value:  60
current iteration value:  90
current iteration value:  500
current iteration value:  250
else part executed as break is not executed with iteration value: 250 as break condition =False
```

### pass statement:

- The ```pass``` statement in Python is a null operation. 
- It is a statement that does ```nothing``` when executed. 
- It is typically used as a ```placeholder``` in situations where a statement is syntactically required, but no action is desired. 
- In case the code is incomplete and will be implemented later.

#### syntax:

#### Function:

```python
def my_function():
    pass  # Placeholder for future implementation
```
#### class:

```python
class MyClass:
    pass  # Placeholder for future class definition
```

#### Iterative statement:

```python
for variable in sequence:
    pass  # Loop does nothing
```

#### conditional statement:

```python
if condition:
    # Perform some action
    statement
else:
    pass  # No action required if condition is false
```
#### [pass_statement.py](https://github.com/pknviki95/Python/tree/main/concepts/Flow_control/pass_statement.py) -  ```pass``` statement acts as placeholder for the given execution which helps code to be syntactically correct:

#### conditional statement:

```python
value=int(input("Enter the value: "))

if value<=20:
    print(f"{value} is less than 20")
else:
    pass
```
#### input
```python
Enter the value: 20
```
#### output without pass:

```python
20 is less than 20
```
#### input:

```python
Enter the value: 30
```
#### output with pass:

```python
# Empty
```
#### Iterative statement:

```python
for iterative in range(10):
    pass  # Loop does nothing
```
#### output with pass:

```python
# Empty
```

### del statement:

- ```del``` statement is used to delete variables and objects.

#### syntax:
```python
del variable
```
#### [del_statement.py](https://github.com/pknviki95/Python/tree/main/concepts/Flow_control/del_statement.py) -  ```del``` statement is used to delete variables and objects:

```python
value=10

print("Before del statement: ",value)

# del [variable] - deletes the variable

del value

print("After del statement: ",value)
```
#### output before del:

```python
Before del statement:  10
```
#### output after del - throws Name error:

```python
Traceback (most recent call last):
  File "/home/pknviki95/Learning/Python/concepts/Flow_control/del_statement.py", line 19, in <module>
    print("After del statement: ",value)
NameError: name 'value' is not defined. Did you mean: 'False'?
```
#### [del_immutable_type_error.py](https://github.com/pknviki95/Python/tree/main/concepts/Flow_control/del_immutable_type_error.py) -  ```del``` statement if used to delete elements of sequence for immutable objects it throws error - Type error:

#### Mutable objects supports index deletion as it is Mutable:

```python
list_variable=['viki',2,5,7]

# deleting mutable objects element using indexing 

del list_variable[1]
print("list_variable: ",list_variable)
```

#### output:
```python
list_variable:  ['viki', 5, 7]
```

#### Immutable objects does supports index deletion as it is immutable:

```python
string_variable='viki'

# deleting Immutable objects element using indexing 
# throws error - Type error 

del string_variable[1]
print("string_variable: ",string_variable)
```
#### error:
```python
Traceback (most recent call last):
  File "/home/pknviki95/Learning/Python/concepts/Flow_control/del_immutable_type_error.py", line 22, in <module>
    del string_variable[1]
TypeError: 'str' object doesn't support item deletion
```