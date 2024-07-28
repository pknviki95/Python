# Functions:

## Built-in Functions:

### dir():

- The ```dir()``` function returns list of all properties and methods of the specified object, without the values.

- This function will return all the properties and methods, even built-in properties which are default for all object.

```python
                dir(object)
```

#### [dir_function.py](https://github.com/pknviki95/Python/tree/main/concepts/functions/scripts/dir_function.py) - To get the list of methods and attributes from object using dir() function:

```python
import math

# dir() function returns list of attributes and other methods related to that objects

print("Attributes of math module using dir() function: ",dir(math))
```
#### output:

```python
Attributes of math module using dir() function:  ['__doc__', '__loader__', '__name__', '__package__', '__spec__', 'acos', 'acosh', 'asin', 'asinh', 'atan', 'atan2', 'atanh', 'ceil', 'comb', 'copysign', 'cos', 'cosh', 'degrees', 'dist', 'e', 'erf', 'erfc', 'exp', 'expm1', 'fabs', 'factorial', 'floor', 'fmod', 'frexp', 'fsum', 'gamma', 'gcd', 'hypot', 'inf', 'isclose', 'isfinite', 'isinf', 'isnan', 'isqrt', 'lcm', 'ldexp', 'lgamma', 'log', 'log10', 'log1p', 'log2', 'modf', 'nan', 'nextafter', 'perm', 'pi', 'pow', 'prod', 'radians', 'remainder', 'sin', 'sinh', 'sqrt', 'tan', 'tanh', 'tau', 'trunc', 'ulp']
```

### eval():

- ```eval()``` function evaluates the specified expression.
- It evaluates input function based on the argument passed.

```python
            eval('expression argument')
```

#### [eval_function.py](https://github.com/pknviki95/Python/tree/main/concepts/functions/scripts/eval_function.py) - function evaluates the specified expression using eval() function:

```python
# input():

input_values=input("Enter the input_values: ")
print("Type of input_values: ",type(input_values))

# eval(input())

eval_values=eval(input("Enter the eval_values: " ))
print("Type of eval_values: ",type(eval_values))

# eval expression:

eval_exp=eval('10+20+30')
print("The value of eval_exp: ",eval_exp)

```

#### input:

```python
Enter the input_values: 12
Enter the eval_values: 12
```

#### output:

```python
Type of input_values:  <class 'str'>
Type of eval_values:  <class 'int'>

The value of eval_exp:  60
```