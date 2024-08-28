## Durgasoft programs:

#### Program-01: [P01_ternary_operator_min_value.py](https://github.com/pknviki95/Python/tree/main/practices/DurgaSoft/P01_ternary_operator_min_value.py) - Write a  program to find a min value using ternary operator with two user input :

```python
value_1=int(input("Enter value 1: "))
value_2=int(input("Enter value 2: "))

# [True value] if [condition] else [false value]

min_value =  value_1 if value_1<value_2  else value_2

print("The minimum value: ",min_value)
```

#### input:
```python
                Enter value 1: 200
                Enter value 2: 250
```
#### output:

```python
The minimum value:  200
```

#### Program-02: [P02_ternary_nested_max.py](https://github.com/pknviki95/Python/tree/main/practices/DurgaSoft/P02_ternary_nested_max.py) - Write a  program to find a max value using nested ternary operator with two user input :
```
    Get two user input value
    If both numbers are equal print "Both Numbers are equal" 
    If first number is lesser than second number print "first number is lesser than second number"
    If first number is greater than second number print "first number is greater than second number"
```
```python
value_1=int(input("Enter value 1: "))
value_2=int(input("Enter value 2: "))

print("Both Numbers are equal") if value_1==value_2 else print("first number is lesser than second number") if value_1<value_2 else print("first number is greater than second number")
```

#### input:
```python
                Enter value 1: 80
                Enter value 2: 50
```
#### output:
```python
first number is greater than second number
```

#### Program-03: [P03_input_user_sum.py](https://github.com/pknviki95/Python/tree/main/practices/DurgaSoft/P03_input_user_sum.py) - Write a  program to get two user input and print sum of two inputs:

```python
user_input_1=int(input("Enter value 1: "))
user_input_2=int(input("Enter value 2: "))


# sum of two user input

print("Sum of user_input_1 and user_input_2 = ",user_input_1+user_input_2)
```

#### input:
```python
Enter value 1: 10
Enter value 2: 15
```
#### output:
```python
Sum of user_input_1 and user_input_2 =  25
```

#### Program-04: [P04_user_input_employee_data.py](https://github.com/pknviki95/Python/tree/main/practices/DurgaSoft/P04_user_input_employee_data.py) - Write a  program to get employee data as user input and print the data:

```python
# Employee user input:

Employee_Name=input("Enter Employee Name: ")
Employee_Age=int(input("Enter Employee Age: "))
Employee_salary=float(input("Enter Employee Salary: "))
Employee_Address=input("Enter Employee Address: ")

print("Employee Information: \n\nEmployee_Name: {} \nEmployee_Age: {} \nEmployee_Salary: {} \nEmployee_Address: {}".format(Employee_Name,Employee_Age,Employee_salary,Employee_Address))
```
#### input:
```python
Enter Employee Name: viki
Enter Employee Age: 29
Enter Employee Salary: 15000.25
Enter Employee Address: Ramnad
```
#### output:
```python
Employee Information: 

Employee_Name: viki 
Employee_Age: 29 
Employee_Salary: 15000.25 
Employee_Address: Ramnad
```

#### Program-05: [P05_sys_argv_command_line_argument_sum.py](https://github.com/pknviki95/Python/tree/main/practices/DurgaSoft/P05_sys_argv_command_line_argument_sum.py) - Write a  program to get sum of given number passed as an arguments:

```
py <script> <sum of arguments>
```

```python
import sys

print("List elements of sys.argv variable: ", sys.argv)

print("length of sys.argv: ",len(sys.argv))

sum_value=0

for index_value in sys.argv[1:]:
    sum_value+=int(index_value)
print("sum of argv values {}'s output = {}".format(sys.argv[1:],sum_value))
```

#### input:
```python
py P05_sys_argv_command_line_argument_sum.py 1 2 3 24
```

#### output:

```python
List elements of sys.argv variable:  ['P05_sys_argv_command_line_argument_sum.py', '1', '2', '3', '24']
length of sys.argv:  5
sum of argv values ['1', '2', '3', '24']'s output = 30
```
#### Explanation:

- ```sys.argv``` holds list elements ```['P05_sys_argv_command_line_argument_sum.py', '1', '2', '3', '24']```
- ```sys.argv[1:]``` Index value to start from first argument.
- ```sum_value+=int(index_value)``` :
    - ```+=``` - Addition and assign argument to sum value.
    - ```int(index_value)``` - typecast to int as list elements is string values.

#### Program-06: [P06_if_else_statement_big_small_num.py](https://github.com/pknviki95/Python/tree/main/practices/DurgaSoft/P06_if_else_statement_big_small_num.py) - Write a  program to find smallest and biggest number using if else statements:

```python
number_1=int(input("Enter the number-1: "))
number_2=int(input("Enter the number-2: "))

if number_1>number_2:
    print(f"{number_1} is the biggest Number and {number_2} is the Smallest Number")
elif number_2>number_1:
    print(f"{number_2} is the biggest Number and {number_1} is the Smallest Number")
else:
    print("Numbers are equal")
```
#### input:
```python
Enter the number-1: 10       
Enter the number-2: 20
```
#### output:
```python
20 is the biggest Number and 10 is the Smallest Number
```
#### input:
```python
Enter the number-1: 20
Enter the number-2: 10
```
#### output:
```python
20 is the biggest Number and 10 is the Smallest Number
```
#### input:
```python
Enter the number-1: 10
Enter the number-2: 10
```
#### output:
```python
Numbers are equal
```
#### Explanation:
- ```if number_1>number_2:``` - if condition satisfied it executes if statements.
- ```elif number_2>number_1:``` - if condition is not satisfied it executes elif statements.
- ```else:``` - if and elif condition is not satisfied it executes else statements.

#### Program-07: [P07_if_else_statement_range1to100.py](https://github.com/pknviki95/Python/tree/main/practices/DurgaSoft/P07_if_else_statement_range1to100.py) - Write a  program to find given number is between the range of 1 to 100:

```python
input_number=int(input("Enter the number: "))

if input_number in range(1,101):
    print(f"The number {input_number} is between 1 to 100")
else:
    print(f"The number {input_number} is outside the range of 1 to 100")
```

#### input:
```python
Enter the number: 50
```
#### output:
```python
The number 50 is between 1 to 100
```

#### input:
```python
Enter the number: 101 
```
#### output:
```python
The number 101 is outside the range of 1 to 100
```
#### Explanation:
- ```if input_number in range(1,101):``` if this condition satisfies it executes the if condition statements.
- ```in``` Membership operator checks if the numbers is present in ```range(start,end+1) function```
- It checks if the user input number is in between 1 to 100 range.

#### Program-08: [P08_for_loop_range_odd.py](https://github.com/pknviki95/Python/tree/main/practices/DurgaSoft/P08_for_loop_range_odd.py) - Write a  program to find given odd number between the range of 0 to 20:

```python
for value in range(0,21):
    
    # odd values logic
    if (value%2)!=0:
        print(value)
```
#### output:
```python
1
3
5
7
9
11
13
15
17
19
```
#### Explanation:

- ```for``` loop to iterate the elements in range function ```range(0,21)```.
- ```(value%2)!=0``` - modulo operation to get the reminder value ; if the reminder value not equal to 0 it returns ```odd value```.

#### Program-09: [P09_for_loop_10to1_descending.py](https://github.com/pknviki95/Python/tree/main/practices/DurgaSoft/P09_for_loop_10to1_descending.py) - Write a  program to print number in descending order from 10to 1:

```python
# range(start,stop,step)

for number in range(10,0,-1):
    print(number)
```
#### output:
```python
10
9
8
7
6
5
4
3
2
1
```
#### Explanation:

- ```for number in range(10, 0, -1)```: This line initiates a for loop that iterates over a sequence generated by the range function.
- ```range(start, stop, step)``` - creates a sequence of numbers starting from start, up to (but not including) stop, with a specified step.
range(10, 0, -1)
- ```10``` is the starting point of the sequence. The loop will start with number set to 10.
- ```0``` is the stopping point, but it’s not included in the sequence. The sequence will end before reaching 0, so the loop will run while number is greater than 0.
- ```-1``` is the step, meaning the sequence decreases by 1 on each iteration.
- ```print(number)```-This line prints the current value of number to the console during each iteration of the loop.

#### Program-10: [P10_for_loop_sum_of_num_list.py](https://github.com/pknviki95/Python/tree/main/practices/DurgaSoft/P10_for_loop_sum_of_num_list.py) - Write a  program to print sum of numbers in list sequence:

```python
list_numbers=eval(input("Enter the list of numbers: "))

# empty global variable initialization

sum_value=0

for numbers in list_numbers:

    # Arithmetic and Assign operator to perform sum
    # sum_value= 0+[list values]
    sum_value+=numbers

print("sum of list values: ",sum_value)
```

#### Input:

```python
Enter the list of numbers: [1,2,5,7]
```
#### output:

```python
sum of list values:  15
```
#### Explanation:

- The ```eval()``` function then evaluates this string as a Python expression. This allows users to enter a list-like input such as [1, 2, 3], which eval() interprets as a ```list of numbers```.
- The variable ```sum_value``` is initialized to ```0```. This variable will accumulate the sum of the numbers in the list.
- The ```for``` loop iterates over each element in list_numbers.
- In each iteration, the current element ```(numbers)``` is added to ```sum_value```. 
- The ```+= operator``` adds the value of numbers to the current value of sum_value and then updates sum_value with this new total.

#### Program-11: [P11_while_loop_num_1_20_divisible_3.py](https://github.com/pknviki95/Python/tree/main/practices/DurgaSoft/P11_while_loop_num_1_20_divisible_3.py) - Write a  program to print numbers from 1 to 20 that is divisible by 3:

```python
initial_value=1

while initial_value<=20:
    if initial_value%3==0:
        print("Current initial value that is divisible by 3: ",initial_value)
    initial_value+=1

print("Exiting while loop as it fails in condition after last execution value : ",initial_value)
```
#### output:
```python
Current initial value that is divisible by 3:  3
Current initial value that is divisible by 3:  6
Current initial value that is divisible by 3:  9
Current initial value that is divisible by 3:  12
Current initial value that is divisible by 3:  15
Current initial value that is divisible by 3:  18
Exiting while loop as it fails in condition after last execution value :  21
```

#### Program-12: [P12_while_loop_sum_natural_numbers.py](https://github.com/pknviki95/Python/tree/main/practices/DurgaSoft/P12_while_loop_sum_natural_numbers.py) - Write a  program to return sum of n natural numbers:


```python
input_numbers=int(input("Enter the number: "))

sum_value=0
incremental_value=1
while incremental_value<=input_numbers:
    sum_value+=incremental_value
    incremental_value+=1
print("Sum of n value: ",sum_value)
```

#### input:
```python
Enter the number: 10
```
#### output:
```python
Sum of n value:  55
```

#### Program-13: [P13_break_statement_greaterthan500.py](https://github.com/pknviki95/Python/tree/main/practices/DurgaSoft/P13_break_statement_greaterthan500.py) - Write a  program to break from loop using break statement if cart value exceeds more than 500:

```python
cart_value={'milk':28,'sugar':10,'vegetables':240,'lotion':550,'toothpaste':40}

for iteration in cart_value.values():
    print("Current iteration value: ",iteration)
    if iteration>500:
        print(f"Executing the break statement inside loop as {iteration} is greater than 500")
        break
print(f"outside the loop as {iteration} value")
```

#### output:

```python
Current iteration value:  28
Current iteration value:  10
Current iteration value:  240
Current iteration value:  550
Executing the break statement inside loop as 550 is greater than 500
outside the loop as 550 value
```

#### Explanation:

- ```dictionary``` cart_value contains items as ```keys``` and their corresponding prices as ```values```.
- The loop iterates over the values in the dictionary ```(cart_value.values())```, assigning each value to the variable iteration.
- During each iteration, the loop checks if the current value (iteration) is greater than ```500```.
- If the condition is ```true``` (i.e., iteration > 500), the ```break``` statement is executed, which immediately exits the loop.
- A message is printed indicating that the loop is being exited because the value is greater than 500.
- After the loop exits (either by completing all iterations or due to the break statement), a final print statement displays the value of iteration that caused the loop to exit.

#### Program-14: [P14_prime_number_or_not.py](https://github.com/pknviki95/Python/tree/main/practices/DurgaSoft/P14_prime_number_or_not.py) - Write a  program to check if the given number is prime or not:

```python
input_number=int(input("Enter the number: "))

is_prime=True

if input_number<=1:
    print("The number is not prime number")

else:
    for iteration in range(2,input_number):
        # prime number logic - number if divided by other number then it is not prime.
        if input_number%iteration==0:
            is_prime=False
            break
if is_prime==True:
    print("The number is prime number")
if is_prime==False:
    print("The number is not prime number")
```
#### prime number:
#### input:
```python
Enter the number: 11
```
#### output:
```python
The number is prime number
```
#### Not prime number:
#### input:
```python
Enter the number: 10
```
#### output:
```python
The number is not prime number
```
#### Program-15: [P15_prime_number_less_than_equal_to_number.py](https://github.com/pknviki95/Python/tree/main/practices/DurgaSoft/P15_prime_number_less_than_equal_to_number.py) - Write a  program to check for the given number less than equal to number is prime or not:

```python
input_number=int(input("Enter the number: "))

initial_value=2

while initial_value<=input_number:
    is_prime=True
    for iteration in range(2,initial_value//2+1):
        if initial_value%iteration==0:
            is_prime=False
            break
    if is_prime==True:
        print("Prime numbers: ",initial_value)
    initial_value=initial_value+1
```
#### input:
```python
Enter the number: 5
```
#### output:
```python
Prime numbers:  2
Prime numbers:  3
Prime numbers:  5
```
#### Program-16: [P16_prime_number_n_numbers.py](https://github.com/pknviki95/Python/tree/main/practices/DurgaSoft/P16_prime_number_n_numbers.py) - Write a  program to list of prime numbers for n:

```python
input_number=int(input("Enter the number: "))

initial_value=2
count=0

while True:
    is_prime=True
    for iteration in range(2,initial_value//2+1):
        if initial_value%iteration==0:
            is_prime=False
            #print(f"{initial_value} is Not prime")
            break
    if is_prime==True:
        print(f"{initial_value} is prime",)
        count+=1
    if count==input_number:
        break
    initial_value+=1
```
#### input:
```python
Enter the number: 5
```
#### output:
```python
2 is prime
3 is prime
5 is prime
7 is prime
11 is prime
```