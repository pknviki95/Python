# Math module - math():

- Python has a set of built-in math functions, including an extensive math module, that allows you to perform mathematical tasks on numbers.

#### [math_dir.py](https://github.com/pknviki95/Python/tree/main/concepts/Modules/math/math_dir.py) - To get the list of methods and attributes from math module using dir() function:

```python
import math

# methods of math module

print("Attributes of math module using dir() function: ",dir(math))
```
#### output:

```python
Attributes of math module using dir() function:  ['__doc__', '__loader__', '__name__', '__package__', '__spec__', 'acos', 'acosh', 'asin', 'asinh', 'atan', 'atan2', 'atanh', 'ceil', 'comb', 'copysign', 'cos', 'cosh', 'degrees', 'dist', 'e', 'erf', 'erfc', 'exp', 'expm1', 'fabs', 'factorial', 'floor', 'fmod', 'frexp', 'fsum', 'gamma', 'gcd', 'hypot', 'inf', 'isclose', 'isfinite', 'isinf', 'isnan', 'isqrt', 'lcm', 'ldexp', 'lgamma', 'log', 'log10', 'log1p', 'log2', 'modf', 'nan', 'nextafter', 'perm', 'pi', 'pow', 'prod', 'radians', 'remainder', 'sin', 'sinh', 'sqrt', 'tan', 'tanh', 'tau', 'trunc', 'ulp']
```

### Methods of math Module:

- **math.sqrt(value)**
- **math.ceil(value)**
- **math.pow(value,power_value)**
- **math.exp(value)**

### variables of math Module:
- **math.pi**
- **math.e**

#### math.sqrt(value):

- ```sqrt(value)``` is used to perform square root for the value.

#### [math_sqrt.py](https://github.com/pknviki95/Python/tree/main/concepts/Modules/math/math_sqrt.py) - To perform square root for the value using sqrt(value):

```python
import math

#from math import *

value=14.5

# math.sqrt(value)

print("Sqrt of value = ",math.sqrt(value))
```
#### output:

```python
Sqrt of value =  3.8078865529319543
```
#### math.ceil(value):

- ```ceil(value)``` is used to get the nearest return value for a given values.

#### [math_ceil.py](https://github.com/pknviki95/Python/tree/main/concepts/Modules/math/math_ceil.py) - To get the nearest return value for a given values using ceil(value):

```python
import math

#from math import *

value=14.5

# math.ceil(value)

print("ceil of value = ",math.ceil(value))
```

#### output:
```python
ceil of value =  15
```
#### math.pow(value,power_value):

- ```pow(value,power_value)``` is used to get the power of values by passing power value to argument.

#### [math_pow.py](https://github.com/pknviki95/Python/tree/main/concepts/Modules/math/math_pow.py) - To get the power of values by passing power value to argument using pow(value,power_value):

```python
import math

#from math import *

value=14.5

#math.pow(value,power_value)

print("power of value = ",math.pow(value,2))
```
#### output:
```python
power of value =  210.25
```
#### math.e:

- ```e``` math module variable holds the equivalent value of ```e=2.718281828459045```.
- By using this variable various mathematical operation related to ```e``` can be performed.

#### [math_e.py](https://github.com/pknviki95/Python/tree/main/concepts/Modules/math/math_e.py) - various mathematical operation related to ```e```:

```python
import math

#from math import *

# e value (Euler number) = 2.718281828459045...

print("Euler value using math.e= ",math.e)
```
#### output:

```python
Euler value using math.e=  2.718281828459045
```

#### math.exp(value):

- ```exp(value)``` returns the **e<sup>(value)</sup>** 
- e is Euler number whose value is ```2.718281828459045```

#### [math_exp.py](https://github.com/pknviki95/Python/tree/main/concepts/Modules/math/math_exp.py) - To get power of e with value passed using exp(value):

```python
import math

#from math import *

value=14.5

# e value (Euler number) = 2.718281828459045...

print("Euler value using math.e= ",math.e)

# math.exp(value) = e^value 
# 2.718281828459045...^14.5 

print("Exponential of value using math.exp(value)= ",math.exp(value))
```
#### output:
```python
Euler value using math.e=  2.718281828459045
Exponential of value using math.exp(value)=  1982759.2635375687
```
#### math.pi:

- ```pi``` math module variable holds the equivalent value of ```pi=3.141592653589793```.
- By using this variable various mathematical operation related to ```pi``` can be performed.

#### [math_pi.py](https://github.com/pknviki95/Python/tree/main/concepts/Modules/math/math_pi.py) - various mathematical operation related to ```pi```.

```python
import math

#from math import *

value=14.5

# math.pi= 3.141592653589793

print("value of pi = ",math.pi)
```
#### output:
```python
value of pi =  3.141592653589793
```