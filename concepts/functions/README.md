# Functions:

## Built-in Functions:

### dir():

- The dir() function returns list of all properties and methods of the specified object, without the values.

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

