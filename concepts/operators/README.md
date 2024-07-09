# Python Operators:

- **Operators are used to perform operations on variables and values.**
- **Based on types of operation it is divided into different types.** 
            
    - **Arithmetic operator**
    - **Relational operator**

            
## Arithmetic operators:

- **Arithmetic operators are used to perform arithmetic operations such as addition,Subtraction,Multiplication,Division,Modulo,Floor division,Exponential**

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

- **Relational Operators in python helps to find the relation between values and return boolean result; some of the relationa operations are greater than(>),greater than or equal to (>=), lesser than (<), less than or equal to(<=)**

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

### Atleast 1 values false return false:
                
                # Atleast 1 values false return false
                
                y=10<20<30<40>50
                
                print("y value is : ",y)
#### output:
                y value is :  False