# Python Operators:

- Operators are used to perform operations on variables and values.

## Types of operators:

- Based on types of operation it is divided into different types.
            
    - **Arithmetic operator**
    - **Relational operator**
    - **Equality operator**
    - **Logical operator**
    - **Bitwise operator**
    - **Assignment operator**
    - **Ternary operator**
    - **Identity operator**
    - **Membership operator**


<details>            
 <summary> Arithmetic operator:</summary>

## Arithmetic operator:

- Arithmetic operators are used to perform arithmetic operations such as addition,Subtraction,Multiplication,Division,Modulo,Floor division,Exponential

    - **Arithmetic addition (+)**
    - **Arithmetic Subtraction(-)**
    - **Arithmetic Multiplication(*)**
    - **Arithmetic Division(/)**
    - **Arithmetic Modulo(%)**
    - **Arithmetic Floor division(//)**
    - **Arithmetic Exponential(i<sup>\*\*n</sup>).** 

#### [Arithmetic_operator.py](https://github.com/pknviki95/Python/tree/main/concepts/operators/scripts/Arithmetic_operator.py) - Arithmetic operation for given values:

#### Addition:

- Addition operator (+) is used for performing addition of values
  
```python
x=10
y=5

### Addition:

addition=x+y
print("Addition of x and y: ",addition)
```
#### output:

```python
Addition of x and y:  15
```

#### Subtraction:

- Subtraction operator (-) is used for performing Subtraction of values.
                
```python
x=10
y=5

### Subtraction:

Subtraction=x-y
print("Subtraction of x and y: ",Subtraction)
```
#### output:
```python
Subtraction of x and y:  5
```

#### Multiplication:

- Multiplication operator (*) is used for performing Multiplication of values.

```python
x=10
y=5

# Multiplication

Multiplication=x*y
print("Multiplication of x and y: ",Multiplication)
```
#### output:
```python
Multiplication of x and y:  50
```

#### Modulo:

- Modulo operator (%) is used for performing Modulo operation of values to return its reminder value
                
```python
x=10
y=5

# Modulo

Modulo=x%y
print("Modulo of x and y: ",Modulo)
```
#### output:
```python
Modulo of x and y:  0
```

#### Division:

- Division operator (/) is used for performing Division of values.
- Division always return Float type.
                
```python
x=10
y=5

# Division

Division=x/y
print("Division of x and y: ",Division)
```
#### output:
```python
Division of x and y:  2.0
```

#### Floor Division:

- Floor Division operator (//) is used for performing Floor Division of values.
- Floor Division return integer value/decimal values based on input.
- (i.e) If both are integer then it return Integer value; if any one float then it return float value

```python
x=10
y=5

# Floordivision

Floordivision=x//y

print("Floordivision of x and y: ",Floordivision)
```
#### output:
```python
Floordivision of x and y:  2
```

#### Exponential or power:

- Exponential return power value of the value passed $(i**^n)$
                
```python

x=10

# Exponential - i**n

Exponential=x**2

print("Exponential of x: ",Exponential)
```
#### output:
```python
Exponential of x:  100
```

#### [Arithmetic_zerodivision_error.py](https://github.com/pknviki95/Python/tree/main/concepts/operators/scripts/Arithmetic_zerodivision_error.py) - Division,floor division,Modulo operation with zero throws error - Zero division error:

- Division,floor division,Modulo operation performed with zero throws - Zerodivision error

```python
# Division:

# operation performed with zero throws Zerodivision error

x=2/0
print("Division of x: ",x)

# floor division:

x=2//0
print("floorDivision of x: ",x)

# Modulo

x=2%0
print("Modulo of x: ",x)
```

#### error:

```python
Traceback (most recent call last):
File "/home/pknviki95/Learning/Python/concepts/operators/scripts/Arithmetic_zerodivision_error.py", line 9, in <module>
    x=2/0
ZeroDivisionError: division by zero
```

</details>

<details>            
 <summary>Relational operator:</summary>

## Relational operator:

- Relational Operators in python helps to find the relation between values and return boolean result; some of the relational operations are greater than(>),greater than or equal to (>=), lesser than (<), less than or equal to(<=)

    - **Relational greater than(>)**
    - **Relational greater than or equal to (>=)** 
    - **Relational lesser than (<)**
    - **Relational less than or equal to(<=)**

#### [Relational_operator.py](https://github.com/pknviki95/Python/tree/main/concepts/operators/scripts/Relational_operator.py) - Relational operations - greater than(>),greater than or equal to (>=), lesser than (<), less than or equal to(<=):

#### Integer value:

#### greater than(>):

```python
x=10
y=20

greater_than=x>y
print("x is greater than y: ",greater_than)
```
#### output:
```python
x is greater than y:  False
```

#### greater than or equal to (>=):

```python
x=10
y=20

greater_than_or_equal_to=x>=y
print("x is greater than or equal to y: ",greater_than_or_equal_to)
```
#### output:
```python
x is greater than or equal to y:  False
```

#### lesser than (<): 
                
```python
x=10
y=20

lesser_than=x<y
print("x is lesser than y: ",lesser_than)
```
#### output:
```python
x is lesser than y:  True
```

#### less than or equal to(<=):
```python
x=10
y=20

lesser_than_or_equal_to=x<=y
print("x is lesser than or equal to y: ",lesser_than_or_equal_to)
```
#### output:
```python
x is lesser than or equal to y:  True
```

#### String value:

- Relational operators can be performed in string values by changing into ordinal equivalent values then returns the Boolean results
- It compares first char of string and if it is equal and it switched to second and based on relation it returns boolean result

#### greater than(>):

```python
x='viki'
y='guru'

greater_than=x>y     # 118 > 103

print("x is greater than y: ",greater_than)
```
#### output:

```python
x is greater than y:  True
```

#### greater than or equal to (>=):

```python
x='viki'
y='guru'

greater_than_or_equal_to=x>=y       # 118 >= 103

print("x is greater than or equal to y: ",greater_than_or_equal_to)
```
#### output:

```python
x is greater than or equal to y:  True
```

#### lesser than (<): 

```python
x='viki'
y='guru'

lesser_than=x<y             # 118 < 103

print("x is lesser than y: ",lesser_than)
```
#### output:

```python
x is lesser than y:  False
```

#### less than or equal to(<=):
 
```python
x='viki'
y='guru'

lesser_than_or_equal_to=x<=y       # 118 <= 103    

print("x is lesser than or equal to y: ",lesser_than_or_equal_to)
```
#### output:
```python
x is lesser than or equal to y:  False
```

#### Boolean value:

- Boolean values are converted to its equivalent integral value as True=1 and False=0 and it can perform relational operator based on the above values

#### greater than(>):
               
```python
x=True
y=False

greater_than=x>y                    # 1 > 0

print("x is greater than y: ",greater_than)
```
#### output:
```python
x is greater than y:  True
```

#### greater than or equal to (>=):
               
```python
x=True
y=False

greater_than_or_equal_to=x>=y           # 1 >= 0

print("x is greater than or equal to y: ",greater_than_or_equal_to)
```
#### output:
```python
x is greater than or equal to y:  True
```

#### lesser than (<): 
                
```python
x=True
y=False

lesser_than=x<y                         # 1 < 0

print("x is lesser than y: ",lesser_than)
```
#### output:
        
```python
x is lesser than y:  False
```

#### less than or equal to(<=):
                
```python
x=True
y=False

lesser_than_or_equal_to=x<=y                # 1 <= 0 

print("x is lesser than or equal to y: ",lesser_than_or_equal_to)
```
#### output:

```python
x is lesser than or equal to y:  False
```

#### [Relational_type_error.py](https://github.com/pknviki95/Python/tree/main/concepts/operators/scripts/Relational_type_error.py) - Relational operation performed between int and str throws error- Type error

```python
x=10
y='viki'

# Relational operation performed between int and str throws error- Type error

print("Relational operation performed between int and str: ",x<y)
```

#### error:

```python
Traceback (most recent call last):
File "/home/pknviki95/Learning/Python/concepts/operators/scripts/Relational_type_error.py", line 11, in <module>
    print("Relational operation performed between int and str: ",x<y)
TypeError: '<' not supported between instances of 'int' and 'str'
```

#### Multiple relational operations:

- Multiple relational operation can be performed for a values. 
- It returns True boolean result if all the return values are True. 
- It returns False even if there is single false value

#### All values return True:

```python
### All values return True

x=10<20<30<40

print("x value is : ",x)
```
#### output:
```python
x value is :  True
```

#### At least 1 values false return false:
                
```python
# Atleast 1 values false return false

y=10<20<30<40>50

print("y value is : ",y)
```
#### output:
```python
y value is :  False
```
</details>
<details>            
 <summary> Equality operator:</summary>

## Equality operator:

- Equality operators are used to validate if the given two values are equal to (==) and not equal to (!=)
    
    - **Equality equal to (==)** 
    - **Equality not equal to (!=)**

#### [Equality_operator.py](https://github.com/pknviki95/Python/tree/main/concepts/operators/scripts/Equality_operator.py) - Equality operations - equal to (==) and not equal to (!=):

#### Integer value:

#### Equal to(==):

```python
x=10
y=20

Equal_to=x==y

print("x is equal to y: ",Equal_to)
```
#### output:
```python
x is equal to y:  False
```

#### Not Equal to(!=):

```python
x=10
y=20

not_Equal_to=x!=y

print("x is not equal to y: ",not_Equal_to)
```
#### output:
```python
x is not equal to y:  True
```

#### String value:

#### Equal to(==):

```python
x='viki'
y='guru'

Equal_to=x==y

print("x is equal to y: ",Equal_to)
```

#### output:
```python
x is equal to y:  False
```

#### Not Equal to(!=):
```python
                x='viki'
                y='guru'

                not_Equal_to=x!=y

                print("x is not equal to y: ",not_Equal_to)
```
#### output:
```python
                x is not equal to y:  True
```

#### Boolean value:
#### Equal to(==):
```python
x=True
y=False

Equal_to=x==y

print("x is equal to y: ",Equal_to)
```
#### output:
```python
                x is equal to y:  False
```

#### Not Equal to(!=):

```python
x=True
y=False

not_Equal_to=x!=y

print("x is not equal to y: ",not_Equal_to)
```
#### output:
```python
x is not equal to y:  True
```

#### Multiple Equality operations:

- Multiple Equality operation can be performed for a values
- It returns True boolean result if all the return values are True.
- It returns False even if there is single false value*

#### All values return True:

```python
x=10==20==30==40
print("x value is : ",x)
```
#### output:
```python
x value is :  False
```

#### At least 1 values false return false:

```python
y=10==20==30==40!=50
print("y value is : ",y)
```
#### output:
```python
y value is :  False
```
</details>
<details>            
 <summary> Logical operator:</summary>

## Logical operator:

- Logical operator is used to combine conditional statements using and,or,not
    
    - **Logical and (and)**
    - **Logical or (or)**
    - **Logical not (not)**

- Incase of "and";If only every condition passed is satisfied then it return True ; If even one condition doesn't satisfy then it returns False
- Incase of "or"; Even if any one condition passed it returns True; returns False if all the conditions failed
- "not" return complement value of each other

#### [Logical_operator.py](https://github.com/pknviki95/Python/tree/main/concepts/operators/scripts/Logical_operator.py) - Logical operations - and,or,not:

#### Boolean Types:

#### and:

- Return "True" if "both condition passes"
- Return "False" "even if one condition fails"
    
```python
# Return True if both condition passes:
# Return False even if one condition fails:

print("Both True: ",True and True)                  # True
print("1st True and 2nd False: ",True and False)    # False
print("1st False and 2nd True: ",False and True)    # False
print("Both False: ",False and False)               # False
```

#### output:

```python
Both True:  True
1st True and 2nd False:  False
1st False and 2nd True:  False
Both False:  False
```

#### or:

- Return "True" if "at least one condition passes"
- Return "False" if "all condition fails"

```python
# Return True if at least one condition passes:
# Return False if all condition fails:

print("Both True: ",True or True)               # True
print("1st True or 2nd False: ",True or False) # True
print("1st False or 2nd True: ",False or True) # True
print("Both False: ",False or False)            # False
```
#### output:
```python
Both True:  True
1st True or 2nd False:  True
1st False or 2nd True:  True
Both False:  False
```

#### not:

- Return "False" if "condition True"
- Return "True" if "condition False"

```python
# Return False if condition True
# Return True if condition False

print("not True: ",not True)                # False
print("not False: ",not False)              # True
```

#### output:
```python
not True:  False
not False:  True
```

#### Non-Boolean Types:

####  and:

- In Non-boolean Types "and" if the "1<sup>st</sup> argument condition is False"; It returns "1<sup>st</sup> argument value"
- If the "1<sup>st</sup> argument condition is True"; It return "2<sup>nd</sup> argument value"

#### 1<sup>st</sup> argument non-empty - True:

```python
x=10
y=20

print("Non-boolean and 1st argument True returns 2nd argument value: ",x and y)
```
#### output:
```python
Non-boolean and 1st argument True returns 2nd argument value:  20

```
#### 1<sup>st</sup> argument empty - False:

```python
x=''
y='viki'

print("Non-boolean and 1st argument False returns 1st argument value: ",x and y)
```
#### output:
```python
Non-boolean and 1st argument False returns 1st argument value:  
```

#### or:

- In Non-boolean Types or if the "1<sup>st</sup> argument condition is False"; It return "2<sup>nd</sup> argument value".
- If the "1<sup>st</sup> argument condition is True"; It return "1<sup>st</sup> argument value."

#### 1<sup>st</sup> argument non-empty - True

```python
x=10
y=20

print("Non-boolean or 1st argument True returns 1st argument value: ",x or y)
```
#### output:
```python
Non-boolean or 1st argument True returns 1st argument value:  10
```

#### 1<sup>st</sup> argument empty - False

```python
x=''
y='viki'

print("Non-boolean or 1st argument False returns 2nd argument value: ",x or y)
```
#### output:
```python
Non-boolean or 1st argument False returns 2nd argument value:  viki
```
</details>
<details>
<summary>Bitwise operator:</summary>

## Bitwise operator:

- Bitwise operators are used to compare (binary) numbers
    - **Bitwise and (&)** 
    - **Bitwise or (|)** 
    - **Bitwise x-or (^)** 
    - **Bitwise complement (~)** 
    - **Bitwise left shift (<<)** 
    - **Bitwise Right shift (>>)** 

- Bitwise operators are applicable only for **"int"** and **"bool"** datatype.
- If other datatypes are performed with Bitwise operation it returns type error.

#### [Bitwise_typeerror.py](https://github.com/pknviki95/Python/tree/main/concepts/operators/scripts/Bitwise_typeerror.py) - Bitwise operations throws error is used other than "int"/"bool" type - Type error

```python
str_input_1='viki'
str_input_2='guru'

# Bitwise & operations throws error - Type error

print("Bitwise operation for string values: ",str_input_1&str_input_2)
```
#### error:
```python
Traceback (most recent call last):
File "/home/pknviki95/Learning/Python/concepts/operators/scripts/Bitwise_typeerror.py", line 12, in <module>
    print("Bitwise operation for string values: ",str_input_1&str_input_2)
TypeError: unsupported operand type(s) for &: 'str' and 'str'
```

#### [Bitwise_operator.py](https://github.com/pknviki95/Python/tree/main/concepts/operators/scripts/Bitwise_operator.py) - Bitwise operator - &, |, ^, ~,<<, >> :

#### Bitwise and (&):

- Returns "1" if both values are "bitwise 1".
- Returns "0" if anyone values are "bitwise 0"

```python
x=10
y=40

# Both 1/True return 1
# If any one 0 return 0

print("Bitwise and (&) for x and y: ",x&y)
```

#### Explanation:

| Integer/Bitwise | 32 |16|8|4|2|1|
|----- |:---:|:---:|:---:|:---:|:---:|:---:|
| 10 |  0|0|1|0|1|0|
| 40 | 1 |0|1|0|0|0|
| Bitwise (&) | 0|0|1|0|0|0|
| Final value (+)<br> $(8)$|0|0|8|0|0|0|

#### output:
```python
Bitwise and (&) for x and y:  8
```


#### Bitwise or (|):

- Returns "1" even if one value is "bitwise 1"
- Returns "0" if both values are "bitwise 0"

```python
x=10
y=40

# Both 1/True return 1
# If at least 1 return 1
# If Both zero returns 0

print("Bitwise or (|) for x or y: ",x|y)
```

#### Explanation:

| Integer/Bitwise| 32 |16|8|4|2|1|
|----- |:---:|:---:|:---:|:---:|:---:|:---:|
| 10 |  0|0|1|0|1|0|
| 40 | 1 |0|1|0|0|0|
| Bitwise or  | 1|0|1|0|1|0|
| Final value (+)<br>(i.e) $(32+8+2) = 42$|```32```|0|```8```|0|```2```|0 |

#### output:
```python
Bitwise or (|) for x or y:  42
```

#### Bitwise x-or (^):

- Returns "1" if both values are "different"
- Returns "0" if anyone values are "same"
              
```python
x=10
y=40

# Both different return 1
# If both same returns 0

print("Bitwise x-or (^) for x x-or y: ",x^y)
```

#### Explanation:

| Integer/Bitwise| 32 |16|8|4|2|1|
|----- |:---:|:---:|:---:|:---:|:---:|:---:|
| 10 |  0|0|1|0|1|0|
| 40 | 1 |0|1|0|0|0|
| Bitwise ^  | 1|0|0|0|1|0|
| Final value (+)<br>(i.e) $(32+2) = 34$|```32```|0|0|0|```2```|0 |

#### output:
```python
Bitwise x-or (^) for x x-or y:  34
```

#### Bitwise complement(~):

- Bitwise complement performs specific mathematical complement operations.
- By default Python has 32-bit values
- The Most significant bits acts as "sign bit"
- MSB values are always used to determine the positive or negative value
```               
                0 - It is Positive
                1 - It is Negative
```
- Positive numbers are directly added to the memory
- Negative numbers are represented in 2'<sup>s</sup> complement.

#### Positive value complement:

```python
z=4

print("Bitwise complement (~) for positive ~z: ",~z)
```

#### output:
```python
Bitwise complement (~) for positive ~z:  -5
```

#### Flow of 2'<sup>s</sup>  complement for positive value calculation explanation:


- **Step-1 : Initial value with 32-bit:**
    - MSB 

        ```0 - if Initial value is Positive```
    - other 31-bit based on Initial value
- **Step-2 : (~) complement value:**
    - Converting all values to complement values of initial bit value ( 0 to 1 ; 1 to 0)  
- **Step-3 : 1'<sup>s</sup> complement on 31-bits:**
    - 1'<sup>s</sup> complement is converting the 31-bit complement values with its complement values 
    - (i.e) ( 0 to 1 ; 1 to 0) on 31-bit

        $(1'^s complement)$ = convert ```0 to 1``` ; ```1 to 0```

    - MSB value remains same as complement value.   
- **Step-4 : 2'<sup>s</sup> complement on 1'<sup>s</sup> complement 31-bits value:**
    - 2'<sup>s</sup> complement is adding 1 to 1'<sup>s</sup> complement 

        $(2'^s complement)$ = $(1'^s complement + 1)$

- **Step-5 : Final value MSB+2'<sup>s</sup> complement 31-bit:**
    - Based on MSB
            
        
        ```0 - It is Positive```

        ```1 - It is Negative```
    -  2'<sup>s</sup> complement 31-bit value

| Values | MSB          | 31-bit |
| :--- |:---|:---|
|   4           | ```0``` | ```000 0000 0000 0000 0000 0000 0000 0100```|
|~ 4 (complement)|```1```|```111 1111 1111 1111 1111 1111 1111 1011```|
|$(1'^s complement)$ on 31-bit values of complement |```1```| ```000 0000 0000 0000 0000 0000 0000 0100```|
|$(2'^s complement)$ = $(1'^s complement + 1)$ on 31- bit values|```1```|$(2'^s complement)$ = $(1'^s complement  + 1)$ <br><br>   ```000 0000 0000 0000 0000 0000 0000 0101```|
|Final value|-| 5|

#### Negative value complement:

```python
z=-11

print("Bitwise complement (~) for Negative ~z: ",~z)
```
#### output:
```python
Bitwise complement (~) for Negative ~z:  10
```

#### Flow of 2'<sup>s</sup>  complement for Negative value calculation explanation:

- **Step-1 : Initial value with 32-bit:**
    - MSB 
      
        ```1 - if Initial value is Negative```
    
    - other 31-bit based on Initial value
- **Step-2: Covert 31-bit values to 2'<sup>s</sup> complement value:**
    - 1'<sup>s</sup> complement is converting the 31-bit complement values with its complement values (i.e) ( 0 to 1 ; 1 to 0) on 31-bit

        $(1'^s complement)$ = convert ```0 to 1``` ; ```1 to 0```
    - 2'<sup>s</sup> complement is adding 1 to 1'<sup>s</sup> complement 

        $(2'^s complement)$ = $(1'^s complement + 1)$
- **Step-3 : (~) complement value of above converted negative values:**
    - Converting all values to complement values of 2'<sup>s</sup> complement obtained from above ( 0 to 1 ; 1 to 0)

        $(1'^s complement)$ = convert ```0 to 1``` ; ```1 to 0```

- **Step-4 : Final value of 32-bit complement value:**
    - Based on MSB

        ```0 - It is Positive```

        ```1 - It is Negative```
    -  31-bit value is taken as it is as it is positive MSB value.
    - $(2^n * bit value)$ (i.e) $(2^8*1)+(2^1*1) = 10$

| Values | MSB          | 31-bit |
| :--- |:---|:---|
|  - 11           | ```1``` | ```000 0000 0000 0000 0000 0000 0000 1011```|
|$(1'^s complement)$ on 31-bit values of value |```1```| ```111 1111 1111 1111 1111 1111 1111 0100```|
|$(2'^s complement)$ = $(1'^s complement + 1)$  on 31- bit values|```1```|$(2'^s complement)$ = $(1'^s complement + 1)$ <br><br>   ```111 1111 1111 1111 1111 1111 1111 0101```|
|~ -11 (complement)|```0```|```000 0000 0000 0000 0000 0000 0000 1010```|
|Final value|+| 10|
 
#### Bitwise left shift(<<):
- Shift of bit values to the left.
- The values would be Multiple of 2<sup>n</sup> (i.e) n - shift range
- Left shift is filled with "0" bits in missing position
#### Positive value:

```python
z=24
# shift left by 2 bits
print("Bitwise leftshift (<<) for Positive z: ",z<<2)
```
#### output:
```python
Bitwise leftshift (<<) for Positive z:  96
```

| Values | MSB          | value bits |
| :--- |:---|:---|
|  24           | ```0``` | ```11000``` |
|Bit wise left shift (<<) by 2|```0```|```11000 00```|
|Final value|+| $(2^*1)+(2^5*1)$<br>=  96|

#### 🚩 Left shift : Multiple of $(value*2^n)= 24*2^2 =96$ (i.e) $(2^*1)+(2^5*1) = 96$

#### Negative value:

```python
z=-24
# shift left by 2 bits
print("Bitwise leftshift (<<) for Negative z: ",z<<2)
```
#### output:
```python
Bitwise leftshift (<<) for Negative z:  -96
```

| Values | MSB          | value bits |
| :--- |:---|:---|
|  - 24           | ```1``` | ```11000``` |
|$(1'^s complement)$ on value bits of value |```1```| ```00111```|
|$(2'^s complement)$ = $(1'^s complement + 1)$  on value bits|```1```|$(2'^s complement)$ = $(1'^s complement  + 1) <br><br>   ```01000```|
|Bit wise Left shift (<<) by 2|```1```|```01000 00```|
|Final value|-| $(2^7*1)+(2^5*1)$ <br>= -96|

#### Bitwise right shift(>>):

- Shift of bit values to the right.
- The values would be divisible of 2<sup>n</sup> (i.e) n - shift range.
- Right shift is filled with "sign bit" in missing position.

#### Positive value:

```python
z=24
# shift right by 2 bits
print("Bitwise rightshift (>>) for Positive z: ",z>>2)
```

#### output:
```python
Bitwise rightshift (>>) for Positive z:  6
```

| Values | MSB          | value bits |
| :--- |:---|:---|
|  24           | ```0``` | ```11000``` |
|**Bit wise right shift (>>) by 2**|```0```|```110```|
|**Final value**|+| $(2^2*1)+(2^1*1)$ <br> =  6|

#### 🚩 Right shift : Divisible of $(value/2^n)= 24/2^*2=6$ (i.e) $(2^2*1)+(2^1*1) = 6$

#### Negative value:

```python
z=-24

# shift right by 2 bits

print("Bitwise rightshift (>>) for Negative z: ",z>>2)
```

#### output:

```python
Bitwise rightshift (>>) for Negative z:  -6
```

| Values | MSB          | value bits |
| :--- |:---|:---|
|  - 24           | ```1``` | ```11000``` |
|$(1'^s complement)$ on value bits of value |```1```|```00111```|
|$(2'^s complement)$ = $(1'^s complement + 1)$  on value bits|```1```|$(2'^s complement)$ = $(1'^s complement + 1)$ <br><br>   ```01000```|
|Bit wise right shift (>>) by 2|```1```|```010```|
|**Final value**|-| $(2^3*1)+(2^1*1)$ <br>= - 6|

</details>
<details>
<summary>Assignment operator:</summary>

## Assignment operator:

- Performs operation to assign values to left object/operand.
- combination of Assign operator with other operator.
    
    - **Assign operator (=)**

- **Assign with Arithmetic operation:** 
    - **Add and Assign operator (+=)**
    - **Subtract and Assign operator (-=)**
    - **Multiply and Assign operator (*=)**
    - **Division and Assign operator (/=)**
    - **Floordivision and Assign operator (//=)**
    - **Modulo and Assign operator (%=)**
    - **Exponential and Assign operator (\*\*=)**
- **Assign with Bitwise operation:**
    - **Bitwise and (&) and Assign operator (&=)**
    - **Bitwise or (|) and Assign operator (|=)**
    - **Bitwise x-or (^) and Assign operator (^=)**
    - **Bitwise leftshift (<<) and Assign operator (<<=)**
    - **Bitwise rightshift (>>) and Assign operator (>>=)**

#### [Assignment_operator.py](https://github.com/pknviki95/Python/tree/main/concepts/operators/scripts/Assignment_operator.py) - Assignment operator - &=, |=, ^=,<<=, >>= :

#### Assign operator (=):

```python
x=20   #left operand = value
y=10

print("Assignment operator(=): ",(x,y))
```
#### output:
```python
Assignment operator(=):  (20, 10)
```

#### Assign with Arithmetic operation:

#### Add and Assign operator (+=):

```python
x=20   #left operand = value
y=10

x+=y   # equivalent to x=x+y

print("Add and Assign operator (+=) of x : ",x)
```
#### output:
```python
Add and Assign operator (+=) of x :  30
```

#### Subtract and Assign operator (-=):

```python
x=20   #left operand = value
y=10

x-=y   # equivalent to x=x-y

print("Subtract and Assign operator (-=): of x : ",x)
```
#### output:
```python
Subtract and Assign operator (-=): of x :  10
```


#### Multiply and Assign operator (*=):

```python
x=20   #left operand = value
y=10

x*=y   # equivalent to x=x*y

print("Multiply and Assign operator (*=) of x : ",x)
```
#### output:
```python
Multiply and Assign operator (*=) of x :  200
```

#### Division and Assign operator (/=):
               
```python
x=20   #left operand = value
y=10

x/=y   # equivalent to x=x/y

print("Division and Assign operator (/=) of x : ",x)
```
#### output:
```python
Division and Assign operator (/=) of x :  2.0
```

#### Floordivision and Assign operator (//=):
               
```python
x=20   #left operand = value
y=10

x//=y   # equivalent to x=x//y

print("Floordivision and Assign operator (//=) of x : ",x)
```
#### output:
```python
Floordivision and Assign operator (//=) of x :  2
```

#### Exponential and Assign operator (**=):
                
```python
x=20   #left operand = value
y=10

x**=y   # equivalent to x=x**y

print("Exponential and Assign operator (**=) of x : ",x)
```
#### output:
```python
Exponential and Assign operator (**=) of x :  10240000000000
```

#### Modulo and Assign operator (%=):
                
```python
x=20   #left operand = value
y=10

x%=y   # equivalent to x=x%y

print("Modulo and Assign operator (%=) x : ",x)
```
#### output:
```python
Modulo and Assign operator (%=) x :  0
```

#### Assign with Bitwise operation:

#### Bitwise and (&) and Assign operator (&=):

```python
x=20
y=10

x&=y   # equivalent to x=x&y

print("Bitwise and (&) and Assign operator (&=) x : ",x)
```
#### output:
```python
Bitwise and (&) and Assign operator (&=) x :  0
```

#### Bitwise or (|) and Assign operator (|=):

```python
x=20
y=10

x|=y   # equivalent to x=x|y

print("Bitwise or (|) and Assign operator (|=) x : ",x)
```
#### output:
```python
Bitwise or (|) and Assign operator (|=) x :  30
```

#### Bitwise x-or (^) and Assign operator (^=):

```python
x=20
y=10

x^=y   # equivalent to x=x^y

print("Bitwise x-or (^) and Assign operator (^=) x : ",x)
```
#### output:
```python
Bitwise x-or (^) and Assign operator (^=) x :  30
```

#### Bitwise leftshift (<<) and Assign operator (<<=):

```python
x=20
y=10

x<<=y   # equivalent to x=x<<y

print("Bitwise leftshift (<<) and Assign operator (<<=) x : ",x)
```
#### output:
```python
Bitwise leftshift (<<) and Assign operator (<<=) x :  20480
```
#### Bitwise rightshift (>>) and Assign operator (>>=):
```python
x=20
y=10

x>>=y   # equivalent to x=x>>y

print("Bitwise rightshift (>>) and Assign operator (>>=) x : ",x)
```
#### output:
```python
Bitwise rightshift (>>) and Assign operator (>>=) x :  0
```
#### Limitation of Assignment operator:

#### Initialization of variable:
- If you are trying to perform any operations for a variable without initializing throws error - ```Name error``` 

#### [Assignment_arithmetic_Nameerror.py](https://github.com/pknviki95/Python/tree/main/concepts/operators/scripts/Assignment_arithmetic_Nameerror.py) - To perform any operations for a variable without initializing throws error - ```Name error```

```python
list_numbers=eval(input("Enter the list of numbers: "))

'''
commenting empty global variable initialization 
To understand the non-initialization - Name error
'''
# sum_value=0

for numbers in list_numbers:

    # Arithmetic and Assign operator to perform sum

    sum_value+=numbers

print(sum_value)
```
#### input:
```python
Enter the list of numbers: [1,2]
```
#### error:

```python
Traceback (most recent call last):
  File "/home/pknviki95/Learning/Python/practices/DurgaSoft/P10_for_loop_sum_of_num_list.py", line 15, in <module>
    sum_value+=numbers
NameError: name 'sum_value' is not defined
```
</details>
<details>
<summary>Ternary operator:</summary>

## Ternary operator:

- Python supports ternary operator as it supports operation of three operands.

### Syntax:
```python
            [True value] if [condition] else [false value]
```
#### [Ternary_operator.py](https://github.com/pknviki95/Python/tree/main/concepts/operators/scripts/Ternary_operator.py) - Ternary operator characteristics :
```python
a=10
b=20

# [True value] if [condition] else [false value]

c=50 if a==b else 40

print("Ternary operator value of c: ",c)
```
#### output:
```python
Ternary operator value of c:  40
```

### Nesting of ternary operator:

- Nested ternary operator can be performed for multiple operands scenario.

#### Syntax:
```python
        [True value] if [condition] else [True value] if [condition] else [false value]
```

#### [ternary_nested_operator.py](https://github.com/pknviki95/Python/tree/main/concepts/operators/scripts/ternary_nested_operator.py) -Nested ternary operator with multiple operands scenario:

```python
a=30
b=20
c=60

# [True value] if [condition] else [True value] if [condition] else [false value]

final=a if a<b and a<c else b if b<a and b<c else c

print("Ternary operator value of final: ",final)
```
#### output:
```python
Ternary operator value of final:  20
```
</details>
<details>
<summary>Identity operator:</summary>

## Identity operator:

- Identity operators returns boolean values by verifying the identity values of objects.

    - **Identity operator is**
    - **Identity operator isnot**
- The Identity operator is applicable only if you want to compare address/reference values.

#### [Identity_operator.py](https://github.com/pknviki95/Python/tree/main/concepts/operators/scripts/Identity_operator.py) -Identity operator - is, isnot :

#### Identity operator is:

- Returns "True" if both identity values point to the same objects; else it returns "False".

#### Identity operator is:

#### is same identity - Returns True:

```python
x=10
y=10

print(f"identity of x= {id(x)}")
print(f"identity of y= {id(y)}")

# Is same identity - Returns True

print("x is y",x is y)
```
#### output:
```python
identity of x= 130218328064528
identity of y= 130218328064528
x is y True
```
#### is Different identity - Returns False:
```python
x=10
y=20

print(f"identity of x= {id(x)}")
print(f"identity of y= {id(y)}")

# Is Different identity - Returns False

print("x is y",x is y)
```
#### output:
```python
identity of x= 130218328064528
identity of y= 130218328064848
x is y False
```

#### Identity operator isnot:

- Returns "True" if both identity values doesn't point to the same objects; else it returns "False".

#### isnot same identity - Returns False:

```python
x=10
y=10

print(f"identity of x= {id(x)}")
print(f"identity of y= {id(y)}")

# isnot same identity - Returns True

print("x is y",x is y)
```
#### output:
```python
identity of x= 136481443152400
identity of y= 136481443152400
x is y True
```

#### isnot Different identity - Returns True:

```python
x=10
y=20

print(f"identity of x= {id(x)}")
print(f"identity of y= {id(y)}")
X

# isnot Different identity - Returns True

print("x is y",x is y)
```
#### output:
```python
identity of x= 136481443152400
identity of y= 136481443152720
x is y False
```
</details>
<details>
<summary>Membership operator:</summary>

## Membership operator:

- Membership operator returns the boolean values of members/elements in sequence objects.
    
    - **Membership operator in**
    - **Membership operator not in**

#### [Membership_operator.py](https://github.com/pknviki95/Python/tree/main/concepts/operators/scripts/Membership_operator.py) - Membership operator - in, notin :

#### Membership operator in:

- Returns "True" if member/element present in sequence objects; else it returns "False". 

#### String Sequence:

```python
str_sequence="I am Vignesh"

print(" member present in str_sequence: ",'V' in str_sequence)

# Python is case-sensitive so it return false

print(" member present in str_sequence: ",'v' in str_sequence)
```
#### output:
```python
member present in str_sequence:  True
member present in str_sequence:  False
```

#### List Sequence:

```python
list_sequence=[1,2,5,'viki',2.5]

print(" member present in list_sequence: ",1 in list_sequence)

# Python is case-sensitive so it return false

print(" member present in list_sequence: ",'Viki' in list_sequence)
```
#### output:
```python
member present in list_sequence:  True
member present in list_sequence:  False
```

#### Tuple Sequence:

```python
tuple_sequence=(1,2,5,'viki',2.5)

print(" member present in tuple_sequence: ",8 in tuple_sequence)

# Python is case-sensitive so it return false

print(" member present in tuple_sequence: ",'viki' in tuple_sequence)
```
#### output:
```python
member present in tuple_sequence:  False
member present in tuple_sequence:  True
```

#### Set Sequence:

```python
Set_sequence={1,2,5,'viki',2.5}

print(" member present in Set_sequence: ",8 in Set_sequence)

# Python is case-sensitive so it return false

print(" member present in Set_sequence: ",'Viki' in Set_sequence)
```
#### output:
```python
member present in Set_sequence:  False
member present in Set_sequence:  False
```

#### Dictionary Sequence:

```python
dict_sequence={1:2,5:'viki',7:2.5}

print(" member present in dict_sequence: ",1 in dict_sequence)

# Python is case-sensitive so it return false
# By default in looks for key values in dictionary
print(" member present in dict_sequence: ",'viki' in dict_sequence)
```
#### output:
```python
member present in dict_sequence:  True
member present in dict_sequence:  False
```

#### Membership operator not in:

- Returns "True" if member/element not present in sequence objects; else it returns "False".

#### String Sequence:

```python
str_sequence="I am Vignesh"

print(" member present not in str_sequence: ",'V' not in str_sequence)

# Python is case-sensitive so it return false

print(" member present not in str_sequence: ",'v' not in str_sequence)
```
#### output:
```python
member present not in str_sequence:  False
member present not in str_sequence:  True
```

#### List Sequence:

```python
list_sequence=[1,2,5,'viki',2.5]

print(" member present not in list_sequence: ",1 not in list_sequence)

# Python is case-sensitive so it return false

print(" member present not in list_sequence: ",'Viki' not in list_sequence)
```
#### output:
```python
member present not in list_sequence:  False
member present not in list_sequence:  True
```

#### Tuple Sequence:

```python
tuple_sequence=(1,2,5,'viki',2.5)

print(" member present not in tuple_sequence: ",8 not in tuple_sequence)

# Python is case-sensitive so it return false

print(" member present not in tuple_sequence: ",'viki' not in tuple_sequence)
```
#### output:
```python
member present not in tuple_sequence:  True
member present not in tuple_sequence:  False
```

#### Set Sequence:

```python
Set_sequence={1,2,5,'viki',2.5}

print(" member present not in Set_sequence: ",8 not in Set_sequence)

# Python is case-sensitive so it return false

print(" member present not in Set_sequence: ",'Viki' not in Set_sequence)
```
#### output:
```python
member present not in Set_sequence:  True
member present not in Set_sequence:  True
```

#### Dictionary Sequence:

```python
dict_sequence={1:2,5:'viki',7:2.5}

print(" member present not in dict_sequence: ",1 not in dict_sequence)

# Python is case-sensitive so it return false
# By default in looks for key values in dictionary
print(" member present not in dict_sequence: ",'viki' not in dict_sequence)
```
#### output:
```python
member present not in dict_sequence:  False
member present not in dict_sequence:  True
```
</details>
<details>
<summary>operator precedence:</summary>

## operator precedence:

- Operator precedence describes the order in which operations are performed.

|Operator| Precedence order|
|:---|:---|
|```( )``` |Parenthesis  |
|```**```  |Exponentiation (raise to the power) |
|```~```  ```+```  ```-```  |Complement, unary plus and minus (method names for the last two are +@ and -@) |
|```*``` ```/``` ```%``` ```//```  |Multiply, divide, modulo and floor division |
|```+``` ```-```  |Addition and subtraction |
|```>>``` ```<<```  |Right and left bitwise shift |
|```&```  |Bitwise 'AND' |
|```^``` ```\``` ```\|```  |Bitwise exclusive 'OR' and regular 'OR' |
|```<=``` ```<``` ```>``` ```>=```  |Comparison operators |
|```==``` ```!=```  |Equality operators |
|```=``` ```%=``` ```/=``` ```//=``` ```-=``` ```+=``` ```*=``` ```**=```  |Assignment operators |
|```is``` ```isnot```  |Identity operators |
|```in``` ```not in```  |Membership operators |
|```not``` ```or``` ```and```  |Logical operators |

#### [operator_precedence.py](https://github.com/pknviki95/Python/tree/main/concepts/operators/scripts/operator_precedence.py) - operator precedence order:

```python
x=3/2*4+3+(10/5)**3-2
print(x)
```
#### output:
 ```python
15.0

 ```
#### Precedence order for above :

```python
1. (10/5) =2 - parenthesis 
2. 2**3 = 8 - Exponential
3. 3/2 = 1.5 - Division
4. 1.5*4 = 6.0 - Multiplication 
5. 6+3+8-2 = 15.0- Addition and subtraction
```
