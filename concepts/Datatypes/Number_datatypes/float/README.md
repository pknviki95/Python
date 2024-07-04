# float() -float datatypes:

- Float, or "floating point number" is a number, **positive or negative, containing one or more decimals**
- Float can be represented with **Exponential form/Scientific Notation** with an "e" to indicate the power of 10.
            
            4.5 - postivie float value
            4.6 - Negative float value
            -4.e18 - Exponential form/Scientific Notation (i.e) -4 . * 10^18

NOTE: 
    **Float type variable always returns value with decimal point i.e(5.0)**
    **Float type doesnot support base conversion function it is applicable only for integer type**

### [float_type.py](https://github.com/pknviki95/Python/tree/main/concepts/Datatypes/Number_datatypes/float/scripts/float_type.py) - To find the float type variable using type() function:

            x=11.5 
            print("X value is:",x)   
            print("The type of x is: ",type(x))
#### output:
            X value is: 11.5
            The type of x is:  <class 'float'>

### [float_type.py](https://github.com/pknviki95/Python/tree/main/concepts/Datatypes/Number_datatypes/float/scripts/float_type.py) - To find the exponential float type variable using type() function:

            y=4.e5
            print("Y value is:",y)   
            print("The type of y is: ",type(y))
#### output:
            Y value is: 400000.0
            The type of y is:  <class 'float'>