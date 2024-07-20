## Durgasoft programs:

#### Program-01: [ternary_operator_min_value.py](https://github.com/pknviki95/Python/tree/main/practices/DurgaSoft/ternary_operator_min_value.py) - Write a  program to find a min value using ternary operator with two user input :

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

#### Program-02: [ternary_nested_max.py](https://github.com/pknviki95/Python/tree/main/practices/DurgaSoft/ternary_nested_max.py) - Write a  program to find a max value using nested ternary operator with two user input :
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

#### Program-03: [input_user_sum.py](https://github.com/pknviki95/Python/tree/main/practices/DurgaSoft/ternary_operator_min_value.py) - Write a  program to get two user input and print sum of two inputs:

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

#### Program-04: [user_input_employee_data.py](https://github.com/pknviki95/Python/tree/main/practices/DurgaSoft/user_input_employee_data.py) - Write a  program to get employee data as user input and print the data:

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