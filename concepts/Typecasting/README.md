# Type casting

- The process of **converting one datatype value to other** is called Type casting
- It is also called **type coersion**

## Types of type casting function:

## int():

- int() function is used **to convert other datatypes to integer type value.**

            int(variable)

### float to integer value:

- float value **can be converted to integer value; it neglects the decimal value and return the int value present before decimal point**

### Program: To convert float datatypes to integer value using int():

            float_value=10.998

            #integer value by neglecting decimal value
            print("float converted to int: {}".format(int(float_value)))        

### complex to integer value:

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

### Boolean to integer value:

- Boolean value **can be converted to integer value; it returns its equivalent integer value (i.e) True=1 and False=0**

### Program: To convert Boolean datatypes to integer value using int():
            
            boolean_value=True

            #Integer value as it returns its equivalent integer value (i.e) True=1 and False=0
            print("Boolean converted to int: {}".format(int(boolean_value)))

### string to integer value:

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

### float():

- float() function is used **to convert other datatypes to float type value.**

            float(variable)

### integer to float value:

- integer value **can be converted to float value; it includes the decimal value and return the float value with decimal point**

### Program: To convert integer datatypes to float value using float():

            integer_value=10

            #float value by including decimal value
            print("integer converted to float: {}".format(float(integer_value))) 

### complex to float value:

- **complex value cannot be converted to float value as it has imaginary part to it so it throws type error**

### Program: To convert complex datatypes to float value using float()- Type error:

            complex_value=10+20j

            #Type error as complex to float value is not possible due to img part
            print("complex converted to float: {}".format(float(complex_value)))     
#### error:

            Traceback (most recent call last):
            File "/home/pknviki95/Learning/Python/concepts/Typecasting/float/typecast_float_complex_error.py", line 12, in <module>
                print("complex converted to float: {}".format(float(complex_value)))
            TypeError: float() argument must be a string or a real number, not 'complex'

### Boolean to float value:

- Boolean value **can be converted to float value; it returns its equivalent integer value with decimal point (i.e) True=1.0 and False=0.0**

### Program: To convert Boolean datatypes to float value using float():
            
            boolean_value=True

            # float value as it returns its equivalent integer value with decimal point (i.e) True=1.0 and False=0.0
            print("Boolean converted to float: {}".format(float(boolean_value))) 

### string to integer value:

- String value **can be converted to float value; but the value should be integral and float with base-10 defined**

### Program: To convert string datatypes to float value using float() with base-10 :

            string_value='15'

            # float value as it returns float value/integer value as it is in base-10
            print("String converted to float: {}".format(float(string_value))) 

- If the basic rule as above if any string is not defined in integral with base-10 it will throw value error
**(i.e) value should be decimal/float values ; oct,bin,hex values are not possible to typecast**

### Program: To convert string datatypes to float value using float() without base-10 - Value error:

            string_value='0B111'

            #float value as it returns value error as it is not in base-10
            print("String without base-10 converted to float: {}".format(float(string_value))) 
#### error

            Traceback (most recent call last):
            File "/home/pknviki95/Learning/Python/concepts/Typecasting/float/typecast_diffbase_str_float_error.py", line 11, in <module>
                print("String without base-10 converted to float: {}".format(float(string_value)))
            ValueError: could not convert string to float: '0B111'

| **Typecasting**  |  **Possibilities** | **Description** |
| :---:   | :---: | :---: |
| **int to float**  |  **Possible**   |  **It include after decimal value and return float value** |
| **complex to float**  |  **Not Possible**   |  **it has imaginary part to it so it throws type error** |
| **boolean to float**  |  **Possible**   |  **It returns its equivalent integer value with decimalpoint(i.e) True=1 and False=0** |
| **str with (base-10) to flaot**  |  **Possible**   |  **It returns its integer value with decimal point if the value is base-10** |
| **str without (base-10) to float**  |  **Not Possible**   |  **It throws type error if the value is not base-10** |

### complex():

- complex() function is used **to convert other datatypes to complex type value.**

            complex(real variable,imaginary variable)

### integer to complex value:

- integer value **can be converted to complex value; it includes the integer value to complex based on the declaration; if declared only real part it add the imaginary part with "real_value+0j"**

            (i.e)complex(real variable+0j)

### Program: To convert integer datatypes to complex value using complex() for real value:
            #integer to complex value with real variable:
            
            integer_value=10

            #complex value by including real_value+0j
            print("integer converted to complex real value: {}".format(complex(integer_value))) 

- **If integer value is passed to imaginary value it adds imaginary part value to it "real_value+imaginary_value j"** 

            (i.e)complex(real variable+[imaginary variable]j)

### Program: To convert integer datatypes to complex value using complex() for real value and imaginary value:

            #integer to complex value with real variable and imaginary variable:

            integer_real_value=10
            integer_img_value=20

            #complex value by including real_value+img_valuej
            print("integer converted to complex real value and imaginary : {}".format(complex(integer_real_value,integer_img_value)))

### float to complex value:

- float value **can be converted to complex value; it includes the float value to complex based on the declaration; if declared only real part it add the imaginary part with "real_value+0j"**

### Program: To convert float datatypes to complex value using complex() for real value:
            float_value=10.5

            #complex value by including real_value+0j
            print("float converted to complex real value: {}".format(complex(float_value))) 

- **If float value is passed to imaginary value it adds imaginary part value to it "real_value+imaginary_value j"** 

### Program: To convert float datatypes to complex value using complex() for real value and imaginary value:

            float_real_value=10.5
            float_img_value=20.8

            #complex value by including real_value+img_valuej
            print("float converted to complex real value and imaginary value: {}".format(complex(float_real_value,float_img_value)))

### bool()
### str()




        