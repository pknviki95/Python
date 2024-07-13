# Python Operators:

- **Operators are used to perform operations on variables and values.**

## Types of operators:

- **Based on types of operation it is divided into different types.** 
            
    - **Arithmetic operator**
    - **Relational operator**
    - **Equality operator**
    - **Logical operator**
    - **Bitwise operator**

            
## Arithmetic operator:

- **Arithmetic operators are used to perform arithmetic operations such as addition,Subtraction,Multiplication,Division,Modulo,Floor division,Exponential**

    - **Arithmetic addition (+)**
    - **Arithmetic Subtraction(-)**
    - **Arithmetic Multiplication(*)**
    - **Arithmetic Division(/)**
    - **Arithmetic Modulo(%)**
    - **Arithmetic Floor division(//)**
    - **Arithmetic Exponential(i<sup>\*\*n</sup>).** 

### [Arithmetic_operator.py](https://github.com/pknviki95/Python/tree/main/concepts/operators/scripts/Arithmetic_operator.py) - Arithmetic operation for given values:

### Addition:

- **Addition operator (+) is used for performing addition of values**
  
                x=10
                y=5

                ### Addition:

                addition=x+y
                print("Addition of x and y: ",addition)
#### output:

                Addition of x and y:  15

### Subtraction:

- **Subtraction operator (-) is used for performing Subtraction of values**
                
                x=10
                y=5

                ### Subtraction:

                Subtraction=x-y
                print("Subtraction of x and y: ",Subtraction)
#### output:
                Subtraction of x and y:  5

### Multiplication:

- **Multiplication operator (*) is used for performing Multiplication of values**

                x=10
                y=5
                
                # Multiplication

                Multiplication=x*y
                print("Multiplication of x and y: ",Multiplication)
#### output:
                Multiplication of x and y:  50

### Modulo:

- **Modulo operator (%) is used for performing Modulo operation of values to return its reminder value**
                
                x=10
                y=5

                # Modulo

                Modulo=x%y
                print("Modulo of x and y: ",Modulo)
#### output:
                Modulo of x and y:  0

### Division:

- **Division operator (/) is used for performing Division of values**
- **Division always return Float type**
                
                x=10
                y=5

                # Division

                Division=x/y
                print("Division of x and y: ",Division)
#### output:
                Division of x and y:  2.0

### Floor Division:

- **Floor Division operator (//) is used for performing Floor Division of values**
- **Floor Division return integer value/decimal values based on input**
- **(i.e) If both are integer then it return Integer value; if any one float then it return float value**

                x=10
                y=5

                # Floordivision
                
                Floordivision=x//y
                print("Floordivision of x and y: ",Floordivision)
#### output:
                Floordivision of x and y:  2

### Exponential or power:

- **Exponential return power value of the value passed**
                
                i**n

                x=10

                # Exponential
                
                Exponential=x**2
                print("Exponential of x: ",Exponential)
#### output:
                Exponential of x:  100

 
### [Arithmetic_zerodivision_error.py](https://github.com/pknviki95/Python/tree/main/concepts/operators/scripts/Arithmetic_zerodivision_error.py) - Division,floor division,Modulo operation with zero throws error - Zero division error:

- **Division,floor division,Modulo operation performed with zero throws Zerodivision error**

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

#### error:

                Traceback (most recent call last):
                File "/home/pknviki95/Learning/Python/concepts/operators/scripts/Arithmetic_zerodivision_error.py", line 9, in <module>
                    x=2/0
                ZeroDivisionError: division by zero

## Relational operator:

- **Relational Operators in python helps to find the relation between values and return boolean result; some of the relational operations are greater than(>),greater than or equal to (>=), lesser than (<), less than or equal to(<=)**

    - **Relational greater than(>)**
    - **Relational greater than or equal to (>=)** 
    - **Relational lesser than (<)**
    - **Relational less than or equal to(<=)**

### [Relational_operator.py](https://github.com/pknviki95/Python/tree/main/concepts/operators/scripts/Relational_operator.py) - Relational operations - greater than(>),greater than or equal to (>=), lesser than (<), less than or equal to(<=):

### 1: Integer value:

### greater than(>):

                x=10
                y=20

                greater_than=x>y
                print("x is greater than y: ",greater_than)
#### output:
                x is greater than y:  False

### greater than or equal to (>=):

                x=10
                y=20

                greater_than_or_equal_to=x>=y
                print("x is greater than or equal to y: ",greater_than_or_equal_to)
#### output:
                x is greater than or equal to y:  False

### lesser than (<): 
                
                x=10
                y=20
                
                lesser_than=x<y
                print("x is lesser than y: ",lesser_than)
#### output:
                x is lesser than y:  True

### less than or equal to(<=):
                x=10
                y=20
                
                lesser_than_or_equal_to=x<=y
                print("x is lesser than or equal to y: ",lesser_than_or_equal_to)
#### output:
                x is lesser than or equal to y:  True

### 2: String value:

- **Relational operators can be performed in string values by changing into ordinal equivalent values then returns the Boolean results**
- **It compares first char of string and if it is equal and it switched to second and based on relation it returns boolean result**

### greater than(>):

                x='viki'
                y='guru'
                
                greater_than=x>y     # 118 > 103
                
                print("x is greater than y: ",greater_than)
#### output:

                x is greater than y:  True

### greater than or equal to (>=):

                x='viki'
                y='guru'

                greater_than_or_equal_to=x>=y       # 118 >= 103
                
                print("x is greater than or equal to y: ",greater_than_or_equal_to)
#### output:

                x is greater than or equal to y:  True

### lesser than (<): 

                x='viki'
                y='guru'

                lesser_than=x<y             # 118 < 103
                
                print("x is lesser than y: ",lesser_than)
#### output:

                x is lesser than y:  False

### less than or equal to(<=):
 
                x='viki'
                y='guru'

                lesser_than_or_equal_to=x<=y       # 118 <= 103    

                print("x is lesser than or equal to y: ",lesser_than_or_equal_to)
#### output:
                x is lesser than or equal to y:  False

### 3: Boolean value:

- **Boolean values are converted to its equivalent integral value as True=1 and False=0 and it can perform relational operator based on the above values**

### greater than(>):
               
                x=True
                y=False

                greater_than=x>y                    # 1 > 0
                
                print("x is greater than y: ",greater_than)
#### output:
                x is greater than y:  True

### greater than or equal to (>=):
               
                x=True
                y=False

                greater_than_or_equal_to=x>=y           # 1 >= 0
                
                print("x is greater than or equal to y: ",greater_than_or_equal_to)
#### output:
                x is greater than or equal to y:  True

### lesser than (<): 
                
                x=True
                y=False

                lesser_than=x<y                         # 1 < 0
                
                print("x is lesser than y: ",lesser_than)
#### output:
        
                x is lesser than y:  False

### less than or equal to(<=):
                
                x=True
                y=False

                lesser_than_or_equal_to=x<=y                # 1 <= 0 
                
                print("x is lesser than or equal to y: ",lesser_than_or_equal_to)
#### output:

                x is lesser than or equal to y:  False

### [Relational_type_error.py](https://github.com/pknviki95/Python/tree/main/concepts/operators/scripts/Relational_type_error.py) - Relational operation performed between int and str throws error- Type error

                x=10
                y='viki'

                # Relational operation performed between int and str throws error- Type error

                print("Relational operation performed between int and str: ",x<y)

#### error:

                Traceback (most recent call last):
                File "/home/pknviki95/Learning/Python/concepts/operators/scripts/Relational_type_error.py", line 11, in <module>
                    print("Relational operation performed between int and str: ",x<y)
                TypeError: '<' not supported between instances of 'int' and 'str'

### 4: Multiple relational operations:

- **Multiple relational operation can be performed for a values** 
- **It returns True boolean result if all the return values are True.** 
- **It returns False even if there is single false value**

### All values return True:

                ### All values return True

                x=10<20<30<40

                print("x value is : ",x)
#### output:
                x value is :  True

### At least 1 values false return false:
                
                # Atleast 1 values false return false
                
                y=10<20<30<40>50
                
                print("y value is : ",y)
#### output:
                y value is :  False

## Equality operator:

- **Equality operators are used to validate if the given two values are equal to (==) and not equal to (!=)**
    
    - **Equality equal to (==)** 
    - **Equality not equal to (!=)**

### [Equality_operator.py](https://github.com/pknviki95/Python/tree/main/concepts/operators/scripts/Equality_operator.py) - Equality operations - equal to (==) and not equal to (!=):

### Integer value:

### Equal to(==):

                x=10
                y=20

                Equal_to=x==y

                print("x is equal to y: ",Equal_to)
#### output:
                x is equal to y:  False

### Not Equal to(!=):

                x=10
                y=20

                not_Equal_to=x!=y

                print("x is not equal to y: ",not_Equal_to)
#### output:
            x is not equal to y:  True

### string value:

                x='viki'
                y='guru'

                Equal_to=x==y

                print("x is equal to y: ",Equal_to)

#### output:
                x is equal to y:  False

### Not Equal to(!=):
                x='viki'
                y='guru'

                not_Equal_to=x!=y

                print("x is not equal to y: ",not_Equal_to)
#### output:
                x is not equal to y:  True

### Boolean value:

                x=True
                y=False

                Equal_to=x==y
                
                print("x is equal to y: ",Equal_to)
#### output:
                x is equal to y:  False

### Not Equal to(!=):

                x=True
                y=False

                not_Equal_to=x!=y
                
                print("x is not equal to y: ",not_Equal_to)
#### output:
                x is not equal to y:  True

### 4: Multiple Equality operations:

- **Multiple Equality operation can be performed for a values** 
- **It returns True boolean result if all the return values are True.** 
- **It returns False even if there is single false value**

### All values return True:

                x=10==20==30==40
                print("x value is : ",x)
#### output:
                x value is :  False

### At least 1 values false return false:

                y=10==20==30==40!=50
                print("y value is : ",y)
#### output:
                y value is :  False

## Logical operator:

- **Logical operator is used to combine conditional statements using and,or,not**
    
    - **Logical and (and)**
    - **Logical or (or)**
    - **Logical not (not)**

- **Incase of "and";If only every condition passed is satisfied then it return True ; If even one condition doesn't satisfy then it returns False**
- **Incase of "or"; Even if any one condition passed it returns True; returns False if all the conditions failed**
- **"not" return complement value of each other**

### [Logical_operator.py](https://github.com/pknviki95/Python/tree/main/concepts/operators/scripts/Logical_operator.py) - Logical operations - and,or,not:

### Boolean Types:

### and:

- **Return "True" if "both condition passes"**
- **Return "False" "even if one condition fails"**
    
                # Return True if both condition passes:
                # Return False even if one condition fails:

                print("Both True: ",True and True)                  # True
                print("1st True and 2nd False: ",True and False)    # False
                print("1st False and 2nd True: ",False and True)    # False
                print("Both False: ",False and False)               # False

#### output:

                Both True:  True
                1st True and 2nd False:  False
                1st False and 2nd True:  False
                Both False:  False

### or:

- **Return "True" if "at least one condition passes"**
- **Return "False" if "all condition fails"**

                # Return True if at least one condition passes:
                # Return False if all condition fails:

                print("Both True: ",True or True)               # True
                print("1st True or 2nd False: ",True or False) # True
                print("1st False or 2nd True: ",False or True) # True
                print("Both False: ",False or False)            # False
#### output:
                Both True:  True
                1st True or 2nd False:  True
                1st False or 2nd True:  True
                Both False:  False

### not:

- **Return "False" if "condition True"**
- **Return "True" if "condition False"**

                # Return False if condition True
                # Return True if condition False

                print("not True: ",not True)                # False
                print("not False: ",not False)              # True

#### output:
                not True:  False
                not False:  True

### Non-Boolean Types:

###  and:

- **In Non-boolean Types "and" if the "1<sup>st</sup> argument condition is False"; It returns "1<sup>st</sup> argument value"**
- **If the "1<sup>st</sup> argument condition is True"; It return "2<sup>nd</sup> argument value"**

### 1<sup>st</sup> argument non-empty - True

                x=10
                y=20

                print("Non-boolean and 1st argument True returns 2nd argument value: ",x and y)
#### output:
                Non-boolean and 1st argument True returns 2nd argument value:  20

### 1<sup>st</sup> argument empty - False

                x=''
                y='viki'

                print("Non-boolean and 1st argument False returns 1st argument value: ",x and y)
#### output:
                Non-boolean and 1st argument False returns 1st argument value:  

### or:

- **In Non-boolean Types or if the "1<sup>st</sup> argument condition is False"; It return "2<sup>nd</sup> argument value".**
- **If the "1<sup>st</sup> argument condition is True"; It return "1<sup>st</sup> argument value."**

### 1<sup>st</sup> argument non-empty - True

                x=10
                y=20

                print("Non-boolean or 1st argument True returns 1st argument value: ",x or y)
#### output:
                Non-boolean or 1st argument True returns 1st argument value:  10

### 1<sup>st</sup> argument empty - False

                x=''
                y='viki'

                print("Non-boolean or 1st argument False returns 2nd argument value: ",x or y)
#### output:
                Non-boolean or 1st argument False returns 2nd argument value:  viki

## Bitwise operator:

- **Bitwise operators are used to compare (binary) numbers**
    - **Bitwise and (&)** 
    - **Bitwise or (|)** 
    - **Bitwise x-or (^)** 
    - **Bitwise complement (~)** 
    - **Bitwise left shift (<<)** 
    - **Bitwise Right shift (>>)** 

- **Bitwise operators are applicable only for "int" and "bool" datatype**
- **If other datatypes are performed with Bitwise operation it returns type error.**

### [Bitwise_typeerror.py](https://github.com/pknviki95/Python/tree/main/concepts/operators/scripts/Bitwise_typeerror.py) - Bitwise operations throws error is used other than "int"/"bool" type - Type error

                str_input_1='viki'
                str_input_2='guru'

                # Bitwise & operations throws error - Type error

                print("Bitwise operation for string values: ",str_input_1&str_input_2)
#### error:
                Traceback (most recent call last):
                File "/home/pknviki95/Learning/Python/concepts/operators/scripts/Bitwise_typeerror.py", line 12, in <module>
                    print("Bitwise operation for string values: ",str_input_1&str_input_2)
                TypeError: unsupported operand type(s) for &: 'str' and 'str'

### [Bitwise_operator.py](https://github.com/pknviki95/Python/tree/main/concepts/operators/scripts/Bitwise_operator.py) - Bitwise operator - &, |, ^, ~,<<, >> :

### Bitwise and (&):

- **Returns "1" if both values are "bitwise 1"**
- **Returns "0" if anyone values are "bitwise 0"** 

                x=10
                y=40

                # Both 1/True return 1
                # If any one 0 return 0

                print("Bitwise and (&) for x and y: ",x&y)

#### Explanation:

| Integer/Bitwise | 32 |16|8|4|2|1|
|----- |:---:|:---:|:---:|:---:|:---:|:---:|
| 10 |  0|0|1|0|1|0|
| 40 | 1 |0|1|0|0|0|
| Bitwise (&) | 0|0|1|0|0|0|
| Final value (+)|0|0|8|0|0|0|

#### output:
                Bitwise and (&) for x and y:  8


### Bitwise or (|):

- **Returns "1" even if one value is "bitwise 1"**
- **Returns "0" if both values are "bitwise 0"** 

                x=10
                y=40

                # Both 1/True return 1
                # If at least 1 return 1
                # If Both zero returns 0

                print("Bitwise or (|) for x or y: ",x|y)

#### Explanation:

| Integer/Bitwise| 32 |16|8|4|2|1|
|----- |:---:|:---:|:---:|:---:|:---:|:---:|
| 10 |  0|0|1|0|1|0|
| 40 | 1 |0|1|0|0|0|
| Bitwise or  | 1|0|1|0|1|0|
| Final value (+)|32|0|8|0|2|0 |

#### output:
                Bitwise or (|) for x or y:  42

### Bitwise x-or (^):

- **Returns "1" if both values are "different"**
- **Returns "0" if anyone values are "same"** 
              
                x=10
                y=40

                # Both different return 1
                # If both same returns 0

                print("Bitwise x-or (^) for x x-or y: ",x^y)

#### Explanation:

| Integer/Bitwise| 32 |16|8|4|2|1|
|----- |:---:|:---:|:---:|:---:|:---:|:---:|
| 10 |  0|0|1|0|1|0|
| 40 | 1 |0|1|0|0|0|
| Bitwise ^  | 1|0|0|0|1|0|
| Final value (+)|32|0|0|0|2|0 |

#### output:
                Bitwise x-or (^) for x x-or y:  34

### Bitwise complement(~):

- **Bitwise complement performs specific mathematical complement operations.**
- **By default Python has 32-bit values**
- **The Most significant bits acts as "sign bit"** 
- **MSB values are always used to determine the positive or negative value**
                
                0 - It is Positive
                1 - It is Negative

- Positive numbers are directly added to the memory
- Negative numbers are represented in 2'<sup>s</sup> complement.

### Positive value complement:


                z=4

                print("Bitwise complement (~) for positive ~z: ",~z)

#### output:
                Bitwise complement (~) for positive ~z:  -5

#### Flow of 2'<sup>s</sup>  complement for positive value calculation explanation:


- Step-1 : **Initial value with 32-bit:**
    - MSB (0 - if Initial value is Positive )
    - other 31-bit based on Initial value
- Step-2 : **(~) complement value:**
    - Converting all values to complement values of initial bit value ( 0 to 1 ; 1 to 0)  
- Step-3 : **1's complement on 31-bits:**
    - 1'<sup>s</sup> complement is converting the 31-bit complement values with its complement values (i.e) ( 0 to 1 ; 1 to 0) on 31-bit

            1's complement = 0 to 1 ; 1 to 0 on 31-bit

    - MSB value remains same as complement value.   
- Step-4 : **2's complement on 1's complement 31-bits value:**
    - 2'<sup>s</sup> complement is adding 1 to 1'<sup>s</sup> complement 

            2's complement = 1's complement + 1

- Step-5 : **Final value MSB+2'<sup>s</sup> complement 31-bit:**
    - Based on MSB

                0 - It is Positive
                1 - It is Negative
    -  2'<sup>s</sup> complement 31-bit value

| Values | MSB          | 31-bit |
| :--- |:---|:---|
|   4           | 0 | 000 0000 0000 0000 0000 0000 0000 0100|
|~ 4 (complement)|1|111 1111 1111 1111 1111 1111 1111 1011|
|**1'<sup>s</sup> complement** on 31-bit values of complement |1| 000 0000 0000 0000 0000 0000 0000 0100|
|**(2'<sup>s</sup> complement = 1'<sup>s</sup> complement + 1)**  on 31- bit values|1|**2'<sup>s</sup> complement** = **1'<sup>s</sup> complement**  + 1 <br><br>   000 0000 0000 0000 0000 0000 0000 0101|
|**Final value**|-| 5|

### Negative value complement:

                z=-11

                print("Bitwise complement (~) for Negative ~z: ",~z)
#### output:
            Bitwise complement (~) for Negative ~z:  10

#### Flow of 2'<sup>s</sup>  complement for Negative value calculation explanation:

- Step-1 : **Initial value with 32-bit:**
    - MSB ( 1 - if Initial value is Negative)
    - other 31-bit based on Initial value
- Step-2: **Covert 31-bit values to 2'<sup>s</sup> complement value:**
    - 1'<sup>s</sup> complement is converting the 31-bit complement values with its complement values (i.e) ( 0 to 1 ; 1 to 0) on 31-bit

            1's complement = 0 to 1 ; 1 to 0 on 31-bit
    - 2'<sup>s</sup> complement is adding 1 to 1'<sup>s</sup> complement 

            2's complement = 1's complement + 1
- Step-3 : **(~) complement value of above converted negative values:**
    - Converting all values to complement values of 2'<sup>s</sup> complement obtained from above ( 0 to 1 ; 1 to 0)

        1's complement = 0 to 1 ; 1 to 0 on 31-bit

- Step-4 : **Final value of 32-bit complement value:**
    - Based on MSB

                0 - It is Positive
                1 - It is Negative
    -  31-bit value is taken as it is as it is positive MSB value.
    - 2<sup>n</sup> * bit value (i.e) (2<sup>8</sup>x1)+(2<sup>1</sup>x1) = 10**

| Values | MSB          | 31-bit |
| :--- |:---|:---|
|  - 11           | 1 | 000 0000 0000 0000 0000 0000 0000 1011|
|**1'<sup>s</sup> complement** on 31-bit values of value |1| 111 1111 1111 1111 1111 1111 1111 0100|
|**(2'<sup>s</sup> complement = 1'<sup>s</sup> complement + 1)**  on 31- bit values|1|**2'<sup>s</sup> complement** = **1'<sup>s</sup> complement**  + 1 <br><br>   111 1111 1111 1111 1111 1111 1111 0101|
|~ -11 (complement)|0|000 0000 0000 0000 0000 0000 0000 1010|
|**Final value**|+| 10|
 
### Bitwise left shift(<<):
- **Shift of bit values to the left.**
- **The values would be Multiple of 2<sup>n</sup> (i.e) n - shift range**
- **Left shift is filled with "0" bits in missing position**
### Positive value:

                z=24
                # shift left by 2 bits
                print("Bitwise leftshift (<<) for Positive z: ",z<<2)
#### output:
                Bitwise leftshift (<<) for Positive z:  96

| Values | MSB          | value bits |
| :--- |:---|:---|
|  24           | 0 | 11000 |
|**Bit wise left shift (<<)**|0|11000 00|
|**Final value**|+| (2<sup>6</sup>x1)+(2<sup>5</sup>x1)<br>=  96|

#### :100: Left shift : multiple of valuex2<sup>n</sup> (i.e) 24x2<sup>2</sup> = 24*4 = 96** 

### Negative value:

                z=-24
                # shift left by 2 bits
                print("Bitwise leftshift (<<) for Negative z: ",z<<2)
#### output:
                Bitwise leftshift (<<) for Negative z:  -96

| Values | MSB          | value bits |
| :--- |:---|:---|
|  - 24           | 1 | 11000 |
|**1'<sup>s</sup> complement** on value bits of value |1| 00111|
|**(2'<sup>s</sup> complement = 1'<sup>s</sup> complement + 1)**  on value bits|1|**2'<sup>s</sup> complement** = **1'<sup>s</sup> complement**  + 1 <br><br>   01000|
|**Bit wise Left shift (<<)**|1|01000 00|
|**Final value**|-| (2<sup>7</sup>x1)+(2<sup>5</sup>x1)<br>= -96|

### Bitwise right shift(>>):

- **Shift of bit values to the right.**
- **The values would be divisible of 2<sup>n</sup> (i.e) n - shift range**
- **Right shift is filled with "sign bit" in missing position**

### Positive value:

                z=24
                # shift right by 2 bits
                print("Bitwise rightshift (>>) for Positive z: ",z>>2)

#### output:
                Bitwise rightshift (>>) for Positive z:  6

| Values | MSB          | value bits |
| :--- |:---|:---|
|  24           | 0 | 11000 |
|**Bit wise right shift (>>)**|0|110|
|**Final value**|+| (2<sup>2</sup>x1)+(2<sup>1</sup>x1)<br>=  6|

#### :100: Right shift : divisible of value/2<sup>n</sup> (i.e) 24/2<sup>2</sup> = 24/4 = 6** 

### Negative value:

                z=-24
                # shift right by 2 bits
                print("Bitwise rightshift (>>) for Negative z: ",z>>2)

#### output:

                Bitwise rightshift (>>) for Negative z:  -6

| Values | MSB          | value bits |
| :--- |:---|:---|
|  - 24           | 1 | 11000 |
|**1'<sup>s</sup> complement** on value bits of value |1| 00111|
|**(2'<sup>s</sup> complement = 1'<sup>s</sup> complement + 1)**  on value bits|1|**2'<sup>s</sup> complement** = **1'<sup>s</sup> complement**  + 1 <br><br>   01000|
|**Bit wise right shift (>>)**|1|010|
|**Final value**|-| (2<sup>3</sup>x1)+(2<sup>1</sup>x1)<br>= - 6|