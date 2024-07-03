# Type casting

- The process of **converting one datatype value to other** is called Type casting
- It is also called **type coersion**

## Types of type casting function:

## int():

- int() function is used **to convert other datatypes to integer type value.**

            int(variable)

#### float to integer value:

- float value **can be converted to integer value; it neglects the decimal value and return the int value present before decimal point**

### Program: To convert float datatypes to integer value using int():

            float_value=10.998

            #integer value by neglecting decimal value
            print("float converted to int: {}".format(int(float_value)))        

#### complex to integer value:

- **complex value cannot be converted to integer value as it has imaginary part to it so it throws type error**

### Program: To convert complex datatypes to integer value using int()- Type error:

            complex_value=10+20j

            #Type error as complex to integer value is not possible due to img part
            print("complex converted to int: {}".format(int(complex_value)))     
#### error:

            Traceback (most recent call last):
            File "/home/pknviki95/Learning/Python/concepts/Typecasting/typecasting_int.py", line 21, in <module>
                print("complex converted to int: {}".format(int(complex_value)))                 
            TypeError: int() argument must be a string, a bytes-like object or a real number, not 'complex'

#### Boolean to integer value:

- Boolean value **can be converted to integer value; it returns its equivalent integer value (i.e) True=1 and False=0**

### Program: To convert Boolean datatypes to integer value using int():
            
            boolean_value=True

            #Integer value as it returns its equivalent integer value (i.e) True=1 and False=0
            print("Boolean converted to int: {}".format(int(boolean_value)))

#### string to integer value:

- String value **can be converted to integer value; but the value should be integral and base-10 defined**

### Program: To convert string datatypes to integer value using int() with base-10 :

            string_value='15'

            # #Integer value as it returns integer value as it is in base-10
            print("String converted to int: {}".format(int(string_value))) 

- If the basic rule as above if any string is not defined in integral with base-10 it will throw value error
**(i.e) value should be decimal values ; oct,bin,hex,float values are not possible to typecast**

### Program: To convert string datatypes to integer value using int() without base-10 - Value error:

            string_value='0B111'

            #Integer value as it returns value error as it is not in base-10
            print("String without base-10 converted to int: {}".format(int(string_value))) 
#### error

            Traceback (most recent call last):
            File "/home/pknviki95/Learning/Python/concepts/Typecasting/typecast_diffbase_str_int_error.py", line 13, in <module>
                print("String without base-10 converted to int: {}".format(int(string_value))) 
            ValueError: invalid literal for int() with base 10: '0B111'

| **Typecasting**  |  **Possibilities** | **Description** |
| :---:   | :---: | :---: |
| **float to int**  |  **Possible**   |  **It neglects after decimal value and return int value** |
| **complex to int**  |  **Not Possible**   |  **it has imaginary part to it so it throws type error** |
| **boolean to int**  |  **Possible**   |  **It returns its equivalent integer value (i.e) True=1 and False=0** |
| **str with (base-10) to int**  |  **Possible**   |  **It returns its integer value if the value is base-10** |
| **str without (base-10) to int**  |  **Not Possible**   |  **It throws type error if the value is not base-10** |

### float()
### complex()
### bool()
### str()




        