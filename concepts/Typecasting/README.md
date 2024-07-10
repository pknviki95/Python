# Type casting

- The process of **converting one datatype value to other** is called Type casting
- It is also called **type coersion**

## Types of type casting function:
- **integer typecasting**
- **float typecasting**
- **complex typecasting**
- **boolean typecasting**
- **string typecasting**

## integer typecasting :

### int():

- int() function is used **to convert other datatypes to integer type value.**

            int(variable)

### float to integer value:

- float value **can be converted to integer value; it neglects the decimal value and return the int value present before decimal point**

### [typecasting_int.py](https://github.com/pknviki95/Python/tree/main/concepts/Typecasting/int/typecasting_int.py) - To convert float datatypes to integer value using int():

            float_value=10.998

            #integer value by neglecting decimal value
            print("float converted to int: {}".format(int(float_value)))        
#### output:
            float converted to int: 10
### Complex to integer value:

- **complex value cannot be converted to integer value as it has imaginary part to it so it throws type error**

### [typecast_int_complex_error.py](https://github.com/pknviki95/Python/tree/main/concepts/Typecasting/int/typecast_int_complex_error.py) - To convert complex datatypes to integer value using int()- Type error:

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

### [typecasting_int.py](https://github.com/pknviki95/Python/tree/main/concepts/Typecasting/int/typecasting_int.py) - To convert Boolean datatypes to integer value using int():
            
            boolean_value=True

            #Integer value as it returns its equivalent integer value (i.e) True=1 and False=0
            print("Boolean converted to int: {}".format(int(boolean_value)))
#### output:
            Boolean converted to int: 1
### String to integer value:

- String value **can be converted to integer value; but the value should be integral and base-10 defined**

### [typecasting_int.py](https://github.com/pknviki95/Python/tree/main/concepts/Typecasting/int/typecasting_int.py) - To convert string datatypes to integer value using int() with base-10 :

            string_value='15'

            # #Integer value as it returns integer value as it is in base-10
            print("String converted to int: {}".format(int(string_value))) 
#### output:
            String converted to int: 15
- If the basic rule as above if any string is not defined in integral with base-10 it will throw value error
**(i.e) value should be decimal values ; oct,bin,hex,float values are not possible to typecast**

### [typecast_diffbase_str_int_error.py](https://github.com/pknviki95/Python/tree/main/concepts/Typecasting/int/typecast_diffbase_str_int_error.py) - To convert string datatypes to integer value using int() without base-10 - Value error:

            string_value='0B111'

            #Integer value as it returns value error as it is not in base-10
            print("String without base-10 converted to int: {}".format(int(string_value))) 
#### error

            Traceback (most recent call last):
            File "/home/pknviki95/Learning/Python/concepts/Typecasting/typecast_diffbase_str_int_error.py", line 13, in <module>
                print("String without base-10 converted to int: {}".format(int(string_value))) 
            ValueError: invalid literal for int() with base 10: '0B111'

| **Typecasting**  |  **Possibilities** | **Description** |
| :---:   | :---: | :--- |
| **float to int**  |  **Possible**   |  **It neglects after decimal value and return int value** |
| **complex to int**  |  **Not Possible**   |  **it has imaginary part to it so it throws type error** |
| **boolean to int**  |  **Possible**   |  **It returns its equivalent integer value (i.e) True=1 and False=0** |
| **str with (base-10) to int**  |  **Possible**   |  **It returns its integer value if the value is base-10** |
| **str without (base-10) to int**  |  **Not Possible**   |  **It throws type error if the value is not base-10** |

## float typecasting :
### float():
- float() function is used **to convert other datatypes to float type value.**

            float(variable)

### Integer to float value:

- Integer value **can be converted to float value; it includes the decimal value and return the float value with decimal point**

### [typecasting_float.py](https://github.com/pknviki95/Python/tree/main/concepts/Typecasting/float/typecasting_float.py) - To convert integer datatypes to float value using float():

            integer_value=10

            #float value by including decimal value
            print("integer converted to float: {}".format(float(integer_value))) 
#### output:
            integer converted to float: 10.0
### complex to float value:

- **complex value cannot be converted to float value as it has imaginary part to it so it throws type error**

### [typecast_float_complex_error.py](https://github.com/pknviki95/Python/tree/main/concepts/Typecasting/float/typecast_float_complex_error.py) - To convert complex datatypes to float value using float()- Type error:

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

### [typecasting_float.py](https://github.com/pknviki95/Python/tree/main/concepts/Typecasting/float/typecasting_float.py) - To convert Boolean datatypes to float value using float():
            
            boolean_value=True

            # float value as it returns its equivalent integer value with decimal point (i.e) True=1.0 and False=0.0
            print("Boolean converted to float: {}".format(float(boolean_value))) 
#### output:
            Boolean converted to float: 1.0
### string to float value:

- String value **can be converted to float value; but the value should be integral and float with base-10 defined**

### [typecasting_float.py](https://github.com/pknviki95/Python/tree/main/concepts/Typecasting/float/typecasting_float.py) - To convert string datatypes to float value using float() with base-10 :

            string_value='15'

            # float value as it returns float value/integer value as it is in base-10
            print("String converted to float: {}".format(float(string_value))) 
#### output:
            String converted to float: 15.0
- If the basic rule as above if any string is not defined in integral with base-10 it will throw value error
**(i.e) value should be decimal/float values ; oct,bin,hex values are not possible to typecast**

### [typecast_diffbase_str_float_error.py](https://github.com/pknviki95/Python/tree/main/concepts/Typecasting/float/typecast_diffbase_str_float_error.py) - To convert string datatypes to float value using float() without base-10 - Value error:

            string_value='0B111'

            #float value as it returns value error as it is not in base-10
            print("String without base-10 converted to float: {}".format(float(string_value))) 
#### error

            Traceback (most recent call last):
            File "/home/pknviki95/Learning/Python/concepts/Typecasting/float/typecast_diffbase_str_float_error.py", line 11, in <module>
                print("String without base-10 converted to float: {}".format(float(string_value)))
            ValueError: could not convert string to float: '0B111'

| **Typecasting**  |  **Possibilities** | **Description** |
| :---:   | :---: | :--- |
| **int to float**  |  **Possible**   |  **It include after decimal value and return float value** |
| **complex to float**  |  **Not Possible**   |  **it has imaginary part to it so it throws type error** |
| **boolean to float**  |  **Possible**   |  **It returns its equivalent integer value with decimal point(i.e) True=1 and False=0** |
| **str with (base-10) to float**  |  **Possible**   |  **It returns its integer value with decimal point if the value is base-10** |
| **str without (base-10) to float**  |  **Not Possible**   |  **It throws type error if the value is not base-10** |

## complex typecasting :
### complex():
- complex() function is used **to convert other datatypes to complex type value.**

            complex(real variable,imaginary variable)

### Integer to complex value:

- Integer value **can be converted to complex value; it includes the integer value to complex based on the declaration; if declared only real part it add the imaginary part with "real_value+0j"**

            (i.e)complex(real variable+0j)

### [typecasting_complex.py](https://github.com/pknviki95/Python/tree/main/concepts/Typecasting/complex/typecasting_complex.py) - To convert integer datatypes to complex value using complex() for real value:
            #integer to complex value with real variable:
            
            integer_value=10

            #complex value by including real_value+0j
            print("integer converted to complex real value: {}".format(complex(integer_value))) 
#### output:
            integer converted to complex real value: (10+0j)           
- **If integer value is passed to imaginary value it adds imaginary part value to it "real_value+imaginary_value j"** 

            (i.e)complex(real variable+[imaginary variable]j)

### [typecasting_complex.py](https://github.com/pknviki95/Python/tree/main/concepts/Typecasting/complex/typecasting_complex.py) - To convert integer datatypes to complex value using complex() for real value and imaginary value:

            #integer to complex value with real variable and imaginary variable:

            integer_real_value=10
            integer_img_value=20

            #complex value by including real_value+img_valuej
            print("integer converted to complex real value and imaginary : {}".format(complex(integer_real_value,integer_img_value)))
#### output:
            integer converted to complex real value and imaginary value: (10+20j) 
### float to complex value:

- float value **can be converted to complex value; it includes the float value to complex based on the declaration; if declared only real part it add the imaginary part with "real_value+0j"**

### [typecasting_complex.py](https://github.com/pknviki95/Python/tree/main/concepts/Typecasting/complex/typecasting_complex.py) - To convert float datatypes to complex value using complex() for real value:
            float_value=10.5

            #complex value by including real_value+0j
            print("float converted to complex real value: {}".format(complex(float_value))) 
#### output:
            float converted to complex real value: (10.5+0j)
- **If float value is passed to imaginary value it adds imaginary part value to it "real_value+imaginary_value j"** 

### [typecasting_complex.py](https://github.com/pknviki95/Python/tree/main/concepts/Typecasting/complex/typecasting_complex.py) - To convert float datatypes to complex value using complex() for real value and imaginary value:

            float_real_value=10.5
            float_img_value=20.8

            #complex value by including real_value+img_valuej
            print("float converted to complex real value and imaginary value: {}".format(complex(float_real_value,float_img_value)))
#### output:
            float converted to complex real value and imaginary value: (10.5+20.8j)

### Boolean to complex value:

- Boolean value **can be converted to complex value; it returns its equivalent integer value  (i.e) True=1 and False=0**

### [typecasting_complex.py](https://github.com/pknviki95/Python/tree/main/concepts/Typecasting/complex/typecasting_complex.py) - To convert Boolean datatypes to complex value using complex() for real value:
            bool_value=True

            #complex value by including real_value+0j
            print("bool converted to complex real value: {}".format(complex(bool_value))) 
#### output:
            bool converted to complex real value: (1+0j)
- **If bool value is passed to imaginary value it adds imaginary part value to it "real_value+imaginary_value j"** 

### [typecasting_complex.py](https://github.com/pknviki95/Python/tree/main/concepts/Typecasting/complex/typecasting_complex.py) - To convert Boolean datatypes to complex value using complex() for real value and imaginary value:

            bool_real_value=True
            bool_img_value=False

            #complex value by including real_value+img_valuej
            print("bool converted to complex real value and imaginary value: {}".format(complex(bool_real_value,bool_img_value)))
#### output:
            bool converted to complex real value and imaginary value: 1j
### string to complex value:

- String value **can be converted to complex value; but the value should be integral and float with base-10 defined**

### [typecasting_complex.py](https://github.com/pknviki95/Python/tree/main/concepts/Typecasting/complex/typecasting_complex.py) - To convert string datatypes to complex value using complex() for real value with base-10 :

            string_value='15'

            #complex value by including real_value+0j
            print("str converted to complex real value: {}".format(complex(string_value))) 
#### output:
            str converted to complex real value: (15+0j)
- **It throws Type error as second argument in complex() function should not be a string; only first argument of complex function supports string variable**

            (i.e) complex('real variable')  

### [typecast_str_complex_arg_error.py](https://github.com/pknviki95/Python/tree/main/concepts/Typecasting/complex/typecast_str_complex_arg_error.py) - To convert string datatypes to complex value using complex() for real value and imaginary value - Type error:

            str_real_value='10.5'
            str_img_value='20'

            #complex value by including real_value+img_valuej - It throws Type error as second argument in complex() function should not be a string
            print("str converted to complex real value and imaginary value: {}".format(complex(str_real_value,str_img_value)))
#### error

            Traceback (most recent call last):
            File "/home/pknviki95/Learning/Python/concepts/Typecasting/complex/typecasting_complex.py", line 90, in <module>
                print("str converted to complex real value and imaginary value: {}".format(complex(str_real_value,str_img_value)))
            TypeError: complex() can't take second arg if first is a string

- **If the basic rule as above if any string is not defined in integral with base-10 it will throw value error**
**(i.e) value should be decimal/float values ; oct,bin,hex values are not possible to typecast**

### [typecast_diffbase_str_complex_error.py](https://github.com/pknviki95/Python/tree/main/concepts/Typecasting/complex/typecast_diffbase_str_complex_error.py) - To convert string datatypes to complex value using complex() without base-10 - Value error:

            string_value='0B111'

            #complex value as it returns value error as it is not in base-10
            print("String without base-10 converted to complex real value: {}".format(complex(string_value))) 
#### error

            Traceback (most recent call last):
            File "/home/pknviki95/Learning/Python/concepts/Typecasting/complex/typecast_diffbase_str_complex_error.py", line 9, in <module>
                print("String without base-10 converted to complex real value: {}".format(complex(string_value)))
            ValueError: complex() arg is a malformed string

| **Typecasting**  |  **Possibilities** | **Description** |
| :---:   | :---: | :--- |
| **int to complex**  |  **Possible**   |  **It include integer value to real and imaginary part based on argument passed in complex() function** |
| **float to complex**  |  **Possible**   |  **It include float value to real and imaginary part based on argument passed in complex() function** |
| **boolean to complex**  |  **Possible**   |  **It returns its equivalent integer value to real and imaginary part based on argument passed in complex() function (i.e) True=1 and False=0** |
| **str with (base-10) to complex in 1<sup>st</sup> argument**  |  **Possible**   |  **It returns its integer value to real and imaginary part based on argument passed in complex() function if the value is base-10** <br> **complex('str variable',not str variable) - correct argument passing** </br>|
| **str with (base-10) to complex in 2<sup>nd</sup> argument**  |  **Not Possible**   |  **Only first argument of the complex function can be passed with string if it is passed in second argument it throws Type error** <br> **complex('str variable','str variable') - type error** </br>|
| **str without (base-10) to complex**  |  **Not Possible**   |  **It throws type error if the value is not base-10** |

## boolean typecasting :
### bool():

- bool() function is used **to convert other datatypes to bool type value.**

            bool(variable)

### Integer to bool value:

- Integer value can be converted **to bool value; It returns "True if the value is non-zero" if the value is "zero then it return False"**

### [typecasting_bool.py](https://github.com/pknviki95/Python/tree/main/concepts/Typecasting/bool/typecasting_bool.py) - To convert integer datatypes to boolean  value using bool():

            integer_non_zero_value=10
            integer_zero_value=0

            # Non-zero integer value return True boolean value
            print("integer non_zero value converted to boolean  : {}".format(bool(integer_non_zero_value)))

            # zero integer value return False boolean value
            print("integer zero value converted to boolean : {}".format(bool(integer_zero_value)))
#### output:
            integer non_zero value converted to boolean  : True
            integer zero value converted to boolean : False
### Float to bool value:

- float value can be converted **to bool value; It returns "True if the value is non-zero" if the value is "zero then it return False"**

### [typecasting_bool.py](https://github.com/pknviki95/Python/tree/main/concepts/Typecasting/bool/typecasting_bool.py) - To convert float datatypes to boolean  value using bool():

            float_non_zero_value=0.123
            float_zero_value=0.0

            # Non-zero float value return True boolean value
            print("float non_zero value converted to boolean  : {}".format(bool(float_non_zero_value)))

            # zero float value return False boolean value
            print("float zero value converted to boolean : {}".format(bool(float_zero_value)))
#### output:
            float non_zero value converted to boolean  : True
            float zero value converted to boolean : False
### complex to bool value:

- complex value can be converted **to bool value; It returns "True if the value is non-zero in either real and imaginary part " if the value is "zero in both real and imaginary part then it return False"**

### [typecasting_bool.py](https://github.com/pknviki95/Python/tree/main/concepts/Typecasting/bool/typecasting_bool.py) - To convert complex datatypes to boolean  value using bool():

            complex_non_zero_value=123+0j
            complex_zero_value=0+0j

            # Non-zero complex value in either real and imaginary part return True boolean value
            print("complex non_zero value converted to boolean  : {}".format(bool(complex_non_zero_value)))

            # zero complex value in both real and imaginary part return False boolean value
            print("complex zero value converted to boolean : {}".format(bool(complex_zero_value)))
#### output:
            complex non_zero value converted to boolean  : True
            complex zero value converted to boolean : False
### string to bool value:

- String datatypes can be **converted to bool; If the "string passed is non-empty then it returns True";If the "string passed is empty then it returns False"**

### [typecasting_bool.py](https://github.com/pknviki95/Python/tree/main/concepts/Typecasting/bool/typecasting_bool.py) - To convert string datatypes to boolean  value using bool():

            str_non_empty_value='Hello'
            str_empty_value=''

            # Non-empty string value return True boolean value
            print("string non_empty value converted to boolean  : {}".format(bool(str_non_empty_value)))

            # zero complex value in both real and imaginary part return False boolean value
            print("string empty value converted to boolean : {}".format(bool(str_empty_value)))
#### output:
            string non_empty value converted to boolean  : True
            string empty value converted to boolean : False

| **Typecasting**  |  **Possibilities** | **Description** |
| :---:   | :---: | :--- |
| **int to bool**  |  **Possible**   | **It returns "True if the value is non-zero" if the value is "zero then it return False"**|
| **float to bool**  |  **Possible**   |  **It returns "True if the value is non-zero" if the value is "zero then it return False"**|
| **complex to bool**  |  **Possible**   |  **It returns "True if the value is non-zero" in either real and imaginary part;if the value is "zero in both real and imaginary part then it return False"**|
| **str to bool**  |  **Possible**   |  **It returns "True if the string is non-empty";return "False if it is empty-string"**|


## string typecasting :

### str():

- str() function is used **to convert other datatypes to string type value.**

            str(variable)

### Integer to string:

- Integer datatypes can be **converted to string value without any restriction it just every base value to decimal value and converts as string**

### [typecasting_str.py](https://github.com/pknviki95/Python/tree/main/concepts/Typecasting/str/typecasting_str.py) - To convert Integer datatypes to string  value using str():

            integer_value=0B111

            # Integer value converted to string value
            print("Integer  value converted to string  : {}".format(str(integer_value)))
#### output:
            Integer  value converted to string  : 7

### Float to string:

- Float datatypes can be **converted to string value without any restriction it just every base value to decimal value and converts as string**

### [typecasting_str.py](https://github.com/pknviki95/Python/tree/main/concepts/Typecasting/str/typecasting_str.py) - To convert float datatypes to string  value using str():

            float_value=10.25

            # float value converted to string value
            print("float  value converted to string  : {}".format(str(float_value)))
#### output:
            float  value converted to string  : 10.25
### Boolean to string:

- Boolean datatypes can be **converted to string value without any restriction it just converts as string**

### [typecasting_str.py](https://github.com/pknviki95/Python/tree/main/concepts/Typecasting/str/typecasting_str.py) - To convert Boolean datatypes to string  value using str():

            Boolean_value=True

            # Boolean value converted to string value
            print("Boolean  value converted to string  : {}".format(str(Boolean_value)))

#### output:
            Boolean  value converted to string  : True

### complex to string

- complex datatypes can be **converted to string value without any restriction it just converts as string**

### [typecasting_str.py](https://github.com/pknviki95/Python/tree/main/concepts/Typecasting/str/typecasting_str.py) - To convert complex datatypes to string  value using str():
        
            complex_value=123+0j

            # complex value converted to string value
            print("complex  value converted to string  : {}".format(str(complex_value)))
#### output:
            complex  value converted to string  : (123+0j)

| **Typecasting**  |  **Possibilities** | **Description** |
| :---:   | :---: | :--- |
| **int to str**  |  **Possible**   | **It returns the string value of integer value**|
| **float to str**  |  **Possible**   |  **It returns the string value of float value**|
| **boolean to str**  |  **Possible**   |  **It returns the string value of boolean value**|
| **complex to str**  |  **Possible**   |  **It returns the string value of complex value**|

## Summary of Typecasting:

| **Typecasting**  |  **int()** | **float()** | **bool()** | **complex()** |**str()** |
| :---:   | :---: | :---: | :---:   | :---: | :---: |
| **int()**  | :heavy_check_mark:  | :heavy_check_mark: | :heavy_check_mark: | :x: | :heavy_check_mark: - for int with base-10 <br> :x: - for int without base-10(float,hex,oct,bin) |
| **float()**  |  :heavy_check_mark: | :heavy_check_mark: | :heavy_check_mark: | :x: |:heavy_check_mark: - for int/float base-10 <br> :x: - for int/float without base-10 |
| **bool()**  |  :heavy_check_mark: | :heavy_check_mark: | :heavy_check_mark: | :heavy_check_mark: |:heavy_check_mark: |
| **complex()**  |  :heavy_check_mark:| :heavy_check_mark: | :heavy_check_mark: | :heavy_check_mark: |:heavy_check_mark: - for str base-10 1<sup>st</sup> argument <br> :x: - for str base-10 2<sup>nd</sup> argument <br> :x: - for str without (base-10)|
| **str()**  |  :heavy_check_mark: | :heavy_check_mark: | :heavy_check_mark: | :heavy_check_mark: |:heavy_check_mark:|