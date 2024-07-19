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