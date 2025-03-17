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