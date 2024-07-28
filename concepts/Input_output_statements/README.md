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

### Command-line arguments:

- Command-line arguments are the arguments passed on the command line alongside python program.

#### sys.argv method:

- sys module with ```argv``` variable is used to perform command line arguments.

```python
                sys.argv
```
- ```sys.argv``` holds the list value of arguments passed
- Individual elements can be accessed using indexing.
- ```argv[0]``` is always pointing to the script ; so always the first index value is reserved for script in python. 
#### for example:

|**Input**|**sys.argv**|**sys.argv[0]**|**sys.argv[1]**|**sys.argv[2]**|
|:---|:---|:---|:---|:---|
|```py sys_argv_command_line_argument.py 1 2```|```['sys_argv_command_line_argument.py', '1', '2']```|```sys_argv_command_line_argument.py``` | ```1```| ```2```|

#### [sys_argv_command_line_argument.py](https://github.com/pknviki95/Python/tree/main/concepts/Input_output_statements/sys_argv_command_line_argument.py) - To pass values as arguments get command-line argument output using sys.argv:

```python
import sys

### command line arguments:

### argument values stored as list of elements in argv variable 

print("sys.argv variable values: ",sys.argv)

print("Type of sys.arg variable: ",type(sys.argv))

### Accessing individual element using indexing in argv variable.

print("sys.argv[0] variable values: ",sys.argv[0])
print("sys.argv[1] variable values: ",sys.argv[1])
print("sys.argv[2] variable values: ",sys.argv[2])
```


#### input:

```python
py sys_argv_command_line_argument.py 1 2
```

#### output:

```python
sys.argv variable values:  ['sys_argv_command_line_argument.py', '1', '2']

Type of sys.arg variable:  <class 'list'>

sys.argv[0] variable values:  sys_argv_command_line_argument.py

sys.argv[1] variable values:  1

sys.argv[2] variable values:  2
```

### Conclusions on command-line arguments:

####  Argument passed in quotes are considered as single argument: 

#### [sys_argv_command_line_arguments_quotes.py](https://github.com/pknviki95/Python/tree/main/concepts/Input_output_statements/sys_argv_command_line_arguments_quotes.py) - Argument passed in quotes are considered as single argument can be seen in argv lists:

```python
import sys

# argument passed in quotes are considered as single argument
print("The lists of sys.argv elements: ",sys.argv)
```
#### input:
```python
py sys_argv_command_line_arguments_quotes.py 1 "
Hello all"
```
#### output:
```python
The lists of sys.argv elements:  ['sys_argv_command_line_arguments_quotes.py', '1', 'Hello all']
```

####   String concatenation can be done in command-line arguments:  

- String concatenations are possible as the list elements in ```sys.argv``` is considered as ```strings```.

#### [sys_argv_command_line_arguments_str_concatenation.py](https://github.com/pknviki95/Python/tree/main/concepts/Input_output_statements/sys_argv_command_line_arguments_str_concatenation.py) - String concatenation can be done in command-line arguments:

```python
import sys

# String concatenation can be done in command-line arguments

print("The lists of sys.argv elements: ",sys.argv)

print("String concatenation of argv[1]+argv[2] : ",sys.argv[1]+sys.argv[2])
``` 
#### input:
```python
py sys_argv_command_line_arguments_str_concatenation.py hello GoodMorning!
```
#### output:
```python
String concatenation of argv[1]+argv[2] :  helloGoodMorning!
```

#### command-line arguments sys.argv value outside the index range passed throws error - Index error:

#### [sys_argv_command_line_argument_index_error.py](https://github.com/pknviki95/Python/tree/main/concepts/Input_output_statements/sys_argv_command_line_argument_index_error.py) - command-line arguments sys.argv value outside the index range passed throws error - Index error:

```python
import sys

### command line arguments:

### argument values stored as list of elements in argv variable 

print("sys.argv variable values: ",sys.argv)


### Accessing individual element using indexing in argv variable.

print("sys.argv[0] variable values: ",sys.argv[0])
print("sys.argv[1] variable values: ",sys.argv[1])
print("sys.argv[2] variable values: ",sys.argv[2])

### Accessing individual element outside index in argv variable throws error: Index error.

print("sys.argv[2] variable values: ",sys.argv[10])
```

#### input:
```python
py sys_argv_command_line_argument_index_error.py 1 2 3
```
#### output:

```python
sys.argv variable values:  ['sys_argv_command_line_argument_index_error.py', '1', '2', '3']
sys.argv[0] variable values:  sys_argv_command_line_argument_index_error.py
sys.argv[1] variable values:  1
sys.argv[2] variable values:  2
```

#### error:

```python
Traceback (most recent call last):
  File "/home/pknviki95/Learning/Python/concepts/Input_output_statements/sys_argv_command_line_argument_index_error.py", line 23, in <module>
    print("sys.argv[2] variable values: ",sys.argv[10])
IndexError: list index out of range
```

## Output statements:

### print():

- The ```print()``` function prints the specified message to the screen, or other standard output device.
- The message can be a string, or any other object, the object will be converted into a ```string``` before written to the screen

```python
            print(objects,sep='',end='\n')
```

#### [print_user.py](https://github.com/pknviki95/Python/tree/main/concepts/Input_output_statements/print_user.py) - printing the objects using print() function:

```python
input_user=input("Enter the value: ")


# print() function:

# print(objects)

print("The input is: ",input_user)

print("The type of input is: ",type(input_user))
```
#### output:
```python
Enter the value: 15
```
#### output:
```python
The input is:  15
The type of input is:  <class 'str'>
```
#### separator attribute:

- separator specifies how to separate the objects, if there is more than one. 
- By default separator  is ```' '```
- It will separate objects with ```spaces```.

```python
            print(sep='')
```
#### [print_separator.py](https://github.com/pknviki95/Python/tree/main/concepts/Input_output_statements/print_separator.py) - printing the objects using print() function with separator sep='':

```python
# Multiple objects input:

x,y,z=10,20,30

# Default separator '':

print("printing with default separator(''):",x,y,z)

# Separator can be changed using sep='<value>'

print("printing by changing default separator(','):",x,y,z,sep=',')
```
#### output:

```python
printing with default separator(''): 10 20 30
printing by changing default separator(','):,10,20,30
```

#### end attribute:

- end specifies values to print at the end. 
- By default end attribute is ```\n``` (line feed).
- print() function always has end attribute print(end='\n')
- (i.e) ```print()``` is equivalent to ```print(end='\n')```

```python
            print(end='\n')
```

#### [print_end.py](https://github.com/pknviki95/Python/tree/main/concepts/Input_output_statements/print_end.py) - printing the objects using print() function with  end='\n':

```python
# Default end '\n':

print("Hello")

# print() equivalent to print(end='\n')

print()
print("GoodMorning!!!")

# end can be changed using end='<value>'

# Empty end attribute:

print("Hello",end='')               

# end attribute ('\t'):

print("GoodMorning!!!",end='\t')
print("How are you")
```
#### output:
```python
Hello

GoodMorning!!!
HelloGoodMorning!!!     How are you
```

#### [print_sep_end.py](https://github.com/pknviki95/Python/tree/main/concepts/Input_output_statements/print_sep_end.py) - printing the objects using print() function with  combination of sep='' and end='\n':

```python
x,y,z=10,20,30

# Default separator '' and end='\n':

print("printing with default separator('') and end='\n':",x,y,z)

# Separator and end can be changed using sep='<value>' and end='<value>'

print("printing by changing default separator and end:",x,y,z,sep='$$',end='\t')
```
#### output:
```python
printing with default separator('') and end='
': 10 20 30
printing by changing default separator and end:$$10$$20$$30     pknviki95@pknviki95-Lenovo-ideapad-330:~/Learning/Python$
```

### print() with replacement operator with f-strings:

- print() with replacement operator is used to print objects with the replacement operators.

#### syntax:
```python
        print(f"{objects}")
```

#### [print_replacement_fstring.py](https://github.com/pknviki95/Python/tree/main/concepts/Input_output_statements/print_replacement_fstring.py) - printing the objects using print() function with  replacement operator:

```python
Employee_Name=input("Enter Employee Name: ")
Employee_Age=int(input("Enter Employee Age: "))

print(f"Employee Name: {Employee_Name}\nEmployee Age:{Employee_Age}")
```

#### Input:
```python
Enter Employee Name: viki
Enter Employee Age: 29
```
#### output:
```python
Employee Name: viki
Employee Age:29
```
### print() with replacement operator with format method:

- print() with replacement operator is used to print objects with the replacement operators with string format method ```"{}".format()```.
- The variable argument should be in same sequence you wanted to print.

#### syntax:
```python
        print("{}".format(variable))
```

#### [print_replacement_format.py](https://github.com/pknviki95/Python/tree/main/concepts/Input_output_statements/print_replacement_format.py) - print() with replacement operator with format method:

```python
integer_variable=29
float_variable=85.5
string_variable='viki'

# "{}".format(variable)

print("I am {}, I am {} Years old, And I weigh about {}".format(string_variable,integer_variable,float_variable))
```
#### output:
```python
I am viki, I am 29 Years old, And I weigh about 85.5
```
### print() with formatted string using % operator:

- print() function with formatted string is used to print output statements based on the type of variables.
- formatted string s are declared with ```%``` operator.

#### syntax:
```python
        print("%[formatted string]" %[variable])
```
- If you need to print with specific value after decimal point ```%.[number of decimal point value]f``` as by default float value returns with five values after decimal point.

### Various formatted string used with print():

|**Formatted String**|**Declaration types**|
|:---|:---|
|```%d```|Signed decimal variables|
|```%i```|Signed decimal variables|
|```%f```| Float variables|
|```%.[number of decimal point value]f```| Float variable with controlled decimal point value|
|```%e```| Exponential floating variables|
|```%o```|Octal variables|
|```%b```|Binary variables|
|```%s```| String variables and other object variables|


#### [print_formatted_string.py](https://github.com/pknviki95/Python/tree/main/concepts/Input_output_statements/print_formatted_string.py) - print() with formatted string using % operator:

```python
integer_variable=29
float_variable=85.5
string_variable='viki'

# %i - Integer/decimal value ; %f - Default float value ; %s - string variable

print("I am %s, I am %i Years old, And I weigh about with default float %f" %(string_variable,integer_variable,float_variable))

# %i - Integer/decimal value ; %.[number of decimal point value]f - Default float value ; %s - string variable

print("I am %s, I am %i Years old, And I weigh about without default float %.2f" %(string_variable,integer_variable,float_variable))
```

#### output:
```python
I am viki, I am 29 Years old, And I weigh about with default float 85.500000
I am viki, I am 29 Years old, And I weigh about without default float 85.50
```