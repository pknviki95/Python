# Python Operators:

- **Operators are used to perform operations on variables and values.**
- **Based on types of operation it is divided into different types.** 
            
    - **Arithmetic operator**
    - **Relational operator**

            
## Arithmetic operators:

- **Arithmetic operators are used to perform arithmmetic operations such as addition,Subtraction,Multiplication,Division,Modulo,Floor division,Exponential**

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