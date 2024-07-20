# Input and output statements:

## Input statements:

### raw_input():

- ```raw_input()``` is used to get the user input for the python program.
- raw_input() return type is always string.
- To covert the value to other object we need typecasting on user input.
- raw_input() is applicable only for python 2.X.

```python
            user_raw_input=raw_input("user_input")
```
#### [raw_input_user.py](https://github.com/pknviki95/Python/tree/main/concepts/Input_output_statements/raw_input_user.py) - To get user input using raw_input() - applicable only for python 2.X versions:

```python
#raw_input()

value=raw_input("Enter the value: ")

print("Type of raw_input user value = ",type(value))
```

#### inputs:
```python
Enter the value: 16
Enter the value: 20.5
Enter the value: True
```

#### output:

```python
Type of raw_input user value =  <class 'str'>
```

### input():

- ```input()``` is used to get the user input for the python program.
- input() return type is based on value passed for python 2.X versions.
- input() return type is always string for python 3.X versions.
- To covert the value to other object we need typecasting on user input.
- input() for python 3.X is similar to raw_input()

```python
            user_input=input("user_input")
```


#### [input_user.py](https://github.com/pknviki95/Python/tree/main/concepts/Input_output_statements/input_user.py) - To get user input using input() - applicable only for python 3.X versions: 

```python
#input()

value=input("Enter the value: ")

print("Type of input user value for python versions 3.X = ",type(value))
```
#### inputs:
```python
Enter the value: 16
Enter the value: 20.5
Enter the value: True
```

#### output:

```python
Type of input user value for python versions 3.X = <class 'str'>
```

#### Program-2: To get user input using input() - for python 2.X versions:

```python
#input()

value=input("Enter the value: ")

print("Type of input user value for python versions 2.X = ",type(value))
```

#### inputs:
```python
Enter the value: 16
Enter the value: 20.5
Enter the value: True
```

#### output:

```python
Type of input user value for python versions 2.X =  <class 'int'>
Type of input user value for python versions 2.X =  <class 'float'>
Type of input user value for python versions 2.X =  <class 'bool'>
```


