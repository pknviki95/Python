# Python Datatypes:

## Various types of datatypes:

- **Number datatypes**
- **Boolean datatypes**
- **String datatypes**
- **List datatypes**
- **Tuple datatypes**
- **Set datatypes**
- **frozenset datatypes**
- **Dictionary datatypes**
- **Range datatypes**
- **Bytes datatypes**
- **Bytearray datatypes**


<details>
<summary>Number datatypes:</summary>

## Number datatypes:

- Python supports the below standard data types.

### Various types of Numbers Datatypes:

- Number datatype are classified based on type of value we use.

    - **Integer datatype**
    - **float datatype**
    - **complex datatype**

## Integer datatypes - int():
 
- Integers – No limit to the value of integers.
- By default Python takes integer as decimal value.
                
```python
        1,1234
```

#### [integer_type.py](https://github.com/pknviki95/Python/tree/main/concepts/Datatypes/Number_datatypes/Integer/scripts/integer_type.py) - To find the integer type variable using type() function:

```python
x=11 
print("X value is:",x)   
print("The type of x is: ",type(x))
```

### Different types of integer Numbers forms:
 
| Integer type | value    | Description  |
| :---:   | :---: | :--- |
|```Decimal form (base-10)``` | ```0-9```   | By default all the number are in decimal form (0-9) |
| ```Binary form (base-2)``` | ```0``` and ```1```   | The binary form has **0b/0B** as the prefix |
| ```Octal form (base-8)``` | ```0-7```   | The octal form has **0o/0O** as the prefix | 
| ```Hexadecimal form (base-16)``` | ```0-9``` and ```A-F```   | The Hexadecimal form has  **0x/0X** as a prefix | 

### Various integral form to decimal conversion:

#### ⚜️ By default Python takes all the integer value as ```decimal value```.


| Integer type | value    | Conversion formula    | Final output|
| :---   | :---: | :---: | :--- |
| ```Binary to decimal``` | A=0b1111   | $(1111)_2$ => $(2^3+2^2+2^1+2^0)$ = $(8*1+4*1+2*1+1* 1)$   | 15 |
| ```Octal to decimal``` | A=0o1234   | $(1234)_8$ => $(8^3+8^2+8^1+8^0)$ = $(512 * 1 + 64 * 2 + 8 * 3 + 1 * 4)$   | 668 |
| ```Hexadecimal to decimal``` | A=0xFACE | $(FACE)$<sub>16</sub> => $(16^3+16^2+16^1+16^0)$ = $(4096*15 + 256 * 10 + 16 * 12+ 1 * 14)$| 64206 | 

### Base Conversion in-built function:

- The in-built base conversion helps to convert from one base to other base integer form.
- These functions are applicable only for integer type.
- Three types

    - **bin()**
    - **hex()**
    - **oct()**

### bin():

- To convert other functions to ```binary form (base-2)```

#### [bin_base_conversion.py](https://github.com/pknviki95/Python/tree/main/concepts/Datatypes/Number_datatypes/Integer/scripts/bin_base_conversion.py) - To convert decimal/octal/hexadecimal form to binary form using bin() function:

#### decimal to binary:
```python
dec_bin=53
print("The binary form of dec_bin : ",bin(dec_bin))
```
#### output:
```python
The binary form of dec_bin :  0b110101
```

#### octal to binary:

```python
oct_bin=0o123
print("The binary form of oct_bin : ",bin(oct_bin))
```
#### output:
```python
The binary form of oct_bin :  0b1010011
```

#### hexadecimal to binary:

```python
hex_bin=0xface
print("The binary form of hex_bin : ",bin(hex_bin))
```
#### output:
```python
The binary form of hex_bin :  0b1111101011001110
```

### hex():

- To convert other functions to ```hexadecimal form (base-16)```.

#### [hex_base_conversion.py](https://github.com/pknviki95/Python/tree/main/concepts/Datatypes/Number_datatypes/Integer/scripts/hex_base_conversion.py) -  To convert decimal/octal/binary form to hexadecimal form using hex() function:

#### decimal to hexadecimal:

```python
dec_hex=123
print("The Hexadecimal form of dec_hex : ",hex(dec_hex))
```

#### output:
```python
The Hexadecimal form of dec_hex :  0x7b
```

#### octal to hexadecimal:

```python
oct_hex=0o123
print("The Hexadecimal form of oct_hex : ",hex(oct_hex))
```
#### output:
```python
The Hexadecimal form of oct_hex :  0x53
```

#### binary to hexadecimal:

```python
bin_hex=0b1111101011001110
print("The Hexadecimal form of bin_hex : ",hex(bin_hex))
```
#### output:
```python
The Hexadecimal form of bin_hex :  0xface
```

### oct(): 

- To convert other functions to ```octal form (base-8)```.

#### [oct_base_conversion.py](https://github.com/pknviki95/Python/tree/main/concepts/Datatypes/Number_datatypes/Integer/scripts/oct_base_conversion.py) -  To convert decimal/hexadecimal/binary form to octal form using oct() function:

#### decimal to octal:

```python
dec_oct=123
print("The octal form of dec_oct : ",oct(dec_oct))
```
#### output:
```python
The octal form of dec_oct :  0o173
```

#### binary to octal:

```python
bin_oct=0b1111101011001110
print("The octal form of bin_oct : ",oct(bin_oct))
```
#### output:
```python
The octal form of hex_oct :  0o443
```

#### hexadecimal to octal:

```python
hex_oct=0x123
print("The octal form of hex_oct : ",oct(hex_oct))
```
#### output:
```python
The octal form of bin_oct :  0o175316
```


## float datatypes - float():

- Float, or "floating point number" is a number, positive or negative, containing one or more decimals.
- Float can be represented with Exponential form/Scientific Notation with an "e" to indicate the power of 10.
            
```python
        4.5  # positive float value
        4.6  # Negative float value
        -4.e18  # Exponential form/Scientific Notation (i.e) -4 . * 10^18
```

#### NOTE:
- Float type variable always returns value with decimal point. (i.e) ```5.0```
- Float type doesn't support base conversion function it is applicable only for integer type.

#### [float_type.py](https://github.com/pknviki95/Python/tree/main/concepts/Datatypes/Number_datatypes/float/scripts/float_type.py) - Program-1 : To find the float type variable using type() function:

```python
x=11.5 
print("X value is:",x)   
print("The type of x is: ",type(x))
```
#### output:
```python
X value is: 11.5
The type of x is:  <class 'float'>
```

#### Program-2 : To find the exponential float type variable using type() function:

```python
y=4.e5
print("Y value is:",y)   
print("The type of y is: ",type(y))
```
#### output:
```python
Y value is: 400000.0
The type of y is:  <class 'float'>
```

## complex datatypes - complex():

- complex type is a number combination of real and imaginary part.
- complex can be represented with ```real+imagj``` (i.e) ```10+12j```.
- Complex datatypes are mostly used in mathematical operations,complex calculation etc.

```python
    complex_variable = real_variable+[imaginary_variable]j
```

#### NOTE:
- imaginary part should always be ```j``` / ```J```; if used any other alphabet it throws error.

#### [complex_img_j_error.py](https://github.com/pknviki95/Python/tree/main/concepts/Datatypes/Number_datatypes/complex/scripts/complex_img_j_error.py) - imaginary part should always be j/J if not it throws error - Syntax error:

```python
# if used anyother alphabet used in imaginary part it throws error

x=11+12i
print("X value is:",x)
```
#### error:
```python
File "/home/pknviki95/Learning/Python/concepts/Datatypes/Number_datatypes/complex/scripts/complex_img_j_error.py", line 1
x=11+12i 
        ^
SyntaxError: invalid decimal literal
```

#### [complex_type.py](https://github.com/pknviki95/Python/tree/main/concepts/Datatypes/Number_datatypes/complex/scripts/complex_type.py) - Program-1 : To find the complex type variable using type() function:

```python
x=11+12j 
print("X value is:",x)   
print("The type of x is: ",type(x))
```
#### output:
```python
X value is: (11+12j)
The type of x is:  <class 'complex'>
```

#### Program-2 : To display the real and imaginary part individually:

```python
x=11+12j 
print("X real value is:",x.real)   
print("X imaginary value is:",x.imag)
```
#### output:
```python
X real value is: 11.0
X imaginary value is: 12.0
```

#### [complex_arithmetic.py](https://github.com/pknviki95/Python/tree/main/concepts/Datatypes/Number_datatypes/complex/scripts/complex_arithmetic.py) - To perform arithmetic operation for complex numbers:

#### Addition:

```python
x=11+12j
y=20+40j
z=x+y 
print("X+Y value is:",z)
```
#### output:
```python
X+Y value is: (31+52j)
```

#### Multiplication:

```python
x=11+12j
y=20+40j
z=x*y 
print("X*Y value is:",z) 
```
#### output:
```python
X*Y value is: (-260+680j)
```

#### Division:

```python
x=11+12j
y=20+40j
z=x/y 
print("X/Y value is:",z)
```
#### output:         
```python
X/Y value is: (0.35-0.1j)
```

### Limitation of complex number declaration:

- The real value of complex number can be a decimal value,float value,octal,hexadecimal,binary values.
- The imaginary value for complex number should be only decimal value if it is declared with other base values it throws syntax error.

| Example | description | Allowance |
| :---:   | :---: | :---: |
| ```x=10+20j``` | decimal values on both real and imag | **Allowed** |
| ```x=10.5+20.5j``` | float values on both real and imag |**Allowed** |
| ```x=0x123+20j``` | hex values 0n real and decimal value on imaginary (same applies for other bases)| **Allowed** |
| ```x=20+0x123j``` | decimal value on real and hex value on imag |**Not Allowed** |

#### [complex_limitation.py](https://github.com/pknviki95/Python/tree/main/concepts/Datatypes/Number_datatypes/complex/scripts/complex_limitation.py) - if updated with imaginary other base values(oct,hex,bin) - Syntax error :

#### binary value:

```python
x=20+0b1111101011001110j 
print("X real value is:",x.real)   
print("X imaginary value is:",x.imag)
```

#### octal value:

```python
x=20+0o123j 
print("X real value is:",x.real)   
print("X imaginary value is:",x.imag)
```

#### hexadecimal value:

```python
x=20+0x123j 
print("X real value is:",x.real)   
print("X imaginary value is:",x.imag)
```

#### error:

```python
File "/home/pknviki95/Learning/Python/concepts/Datatypes/Number_datatypes/complex/scripts/complex_limitation.py", line 10
x=20+0b1111101011001110j 
                        ^
SyntaxError: invalid binary literal
```

### Summary of Number datatypes:

|Number types | Example program   | output    |
| :---:   | :--- | :--- |
| ```integer```  |  x=11 <br>  print("X value is:",x) <br>   print(type(x))   |  X value is: 11 <br> <class 'int'> |
| ```float```    |  y=4.5  <br> print("Y value is:",y)  <br> print(type(y))   |   Y value is: 4.5 <br> <class 'float'> |
| ```complex```  |     z=3+5j <br> print("Z value is:",z)  <br>print(type(z))               |   Z value is: (3+5j) <br> <class 'complex'>         |
</details>

<details>
<summary>Boolean Datatypes:</summary>

## Boolean Datatypes - bool():

- Boolean – bool() is to determine the given value is True or False
- It can be determined if the given input exists , condition is valid or etc.,

```python
            True
            False
```
                
#### NOTE:
- Always the declaration of boolean values should be ```True``` and ```False```
- if declared as ```true``` and ```false``` it throws error in python.

#### [boolean_nameerror.py](https://github.com/pknviki95/Python/tree/main/concepts/Datatypes/Boolean_datatypes/scripts/boolean_nameerror.py) - To find the Boolean type variable using type() function:

```python
#invalid declaration-it return Name error

x=false
print("X value is:",x)   
print("The type of x is: ",type(x))
```
#### error:

```python
Traceback (most recent call last):
File "/home/pknviki95/pknviki/study/python/Python/concepts/Datatypes/Boolean_datatypes/Boolean_type.py", line 5, in <module>
    x=false
NameError: name 'false' is not defined
```

| Boolean type | value    | Description  | Validation |
| :---:   | :---: | :---: | :---: |
| ```True``` | 1   | By default the value is 1 | **True** valid declaration |
| ```False```| 0    | By default the value is 0 | **False** valid declaration|

#### [boolean_type.py](https://github.com/pknviki95/Python/tree/main/concepts/Datatypes/Boolean_datatypes/scripts/boolean_type.py) - To find the Boolean type variable using type() function:

```python
x=True 
print("X value is:",x)   
print("The type of x is: ",type(x))
```
#### output:
```python
X value is: True
The type of x is:  <class 'bool'>
```

#### [boolean_returntype.py](https://github.com/pknviki95/Python/tree/main/concepts/Datatypes/Boolean_datatypes/scripts/boolean_returntype.py) - To find the Boolean return type of variable when condition is invoked:

```python
x=10
y=20
z=x>y 
print("Z value is:",z)   
print("The type of x is: ",type(x))
```
#### output:
```python
Z value is: False
The type of x is:  <class 'bool'>
```
#### [boolean_arithmetic.py](https://github.com/pknviki95/Python/tree/main/concepts/Datatypes/Boolean_datatypes/scripts/boolean_arithmetic.py) - To find the arithmetic value of two boolean input:

```python
x=True              # By default True=1 ; False=0
y=False
z=x+y               # z=1+0=1    
print("Z value is:",z)   
print("The type of x is: ",type(x))
```
#### output:
```python
Z value is: 1
The type of x is:  <class 'bool'>
```

#### NOTE:

- In mathematical expression by default.
```python            
                True=1 
                False=0
```

### Summary of Boolean datatypes:

| Boolean type | value    | Example program   | output    |Description  |
| :---:   | :---: | :--- | :--- | :---: |
| ```True``` | 1   | x=True <br>  print("X value is:",x) <br>   print(type(x))   |  X value is: True <br> <class 'bool'> |By default the value is 1 - True valid declaration |
| ```False```| 0    | x=False <br>  print("X value is:",x) <br>   print(type(x))   |  X value is: False <br> <class 'bool'>|By default the value is 0 - False valid declaration|
</details>
<details>
<summary>String Datatypes:</summary>

## String Datatypes - str():

- str() datatype is used to represent the string variables.
- In python we don't have concept of char/character like in c.
- It will consider all inside quotes as string.

```python
    'viki' # Single Quotes
    "siva"    # Double Quotes
    '''raja'''    # Triple Quotes
```

### Various ways of representing strings:

- **Single Quotes(' ')**
- **Double Quotes(" ")**
- **Triple quotes(""" """)/(''' ''')**

### Limitation of string implementation:

#### 1:Multi-line string literals:

- If the string are represented in single line then it is considered as string datatypes in python.
- If the string that needs to be implemented for multi-line then ```Single Quotes(' ')``` or ```Double Quotes(" ")``` is not possible it will throw Syntax error
- As to resolve this issue only ```Triple quotes (""" """)/(''' ''') ``` is possible to assign multi-line string for any variable.
- (i.e) Triple-quotes are used to define multi-line string literals.

#### [str_limitation.py](https://github.com/pknviki95/Python/tree/main/concepts/Datatypes/String_datatypes/scripts/str_limitation.py) - String variable Limitations for Multi-line string literals:

```python
#single/Double quotes:

sentence = '- If the string
            - If the string'

# Triple quotes

multi_line_sentence= '''- If the string                     
                        - If the string'''

print("single: ",sentence)
print("multi_line_sentence: ",multi_line_sentence)
```

#### error:

```python
pknviki95@pknviki95-Lenovo-ideapad-330:~/Learning/Python/concepts/Datatypes/String_datatypes/scripts$ py str_limitation.py 
File "/home/pknviki95/Learning/Python/concepts/Datatypes/String_datatypes/scripts/str_limitation.py", line 13
    sentence = '- If the string
            ^
SyntaxError: unterminated string literal (detected at line 13)
```

#### 2:Using various string quotes as special character:

- Using various single/double quotes as special character (i.e) usage of ```''``` or ```""``` inside a string can be done only by declaring the string variable in ```triple quotes``` or it will throw Syntax error.

#### [str_limitation.py](https://github.com/pknviki95/Python/tree/main/concepts/Datatypes/String_datatypes/scripts/str_limitation.py) - String variable Limitations for using various single/double quotes as special character:

```python
#single quotes
character= 'Hello all, Welcome to 'Learning''
print(character)

# Triple quotes to use Single/double quotes as special character 
character= ''' Hello all, Welcome to 'Learning' '''
print(character)
```
#### error:

```python
pknviki95@pknviki95-Lenovo-ideapad-330:~/Learning/Python/concepts/Datatypes/String_datatypes/scripts$ py str_limitation.py 
File "/home/pknviki95/Learning/Python/concepts/Datatypes/String_datatypes/scripts/str_limitation.py", line 25
    character= 'Hello all, Welcome to 'Learning''
                                    ^^^^^^^^
SyntaxError: invalid syntax
```

#### [str_type.py](https://github.com/pknviki95/Python/tree/main/concepts/Datatypes/String_datatypes/scripts/str_type.py) - To find the string type variable using type() function:

```python
x='viki'                        #single quotes
y="siva"                        #double quotes
z="""karthi"""                  #triple quotes

print("The type of single quotes x is: ",type(x))
print("The type of double quotes y is: ",type(y))
print("The type of triple quotes z is: ",type(z))
```
#### output:
```python
The type of single quotes x is:  <class 'str'>
The type of double quotes y is:  <class 'str'>
The type of triple quotes z is:  <class 'str'>
```

### Indexing:

- In Python, indexing refers to the process of accessing a specific element in a sequence, such as a string or list, using its position or index number.
- Indexing in Python starts at ```0```, which means that the first element in a sequence has an ```index of 0```, the second element has an ```index of 1```, and so on. 

```python
        variable[index number]
```

- Indexing can be performed only with the total index present in the string;if we ask for return value that exceeds existing index range it throws Index error.

#### [str_index_error.py](https://github.com/pknviki95/Python/tree/main/concepts/Datatypes/String_datatypes/scripts/str_index_error.py) - To understand the Indexing range of string - Index error:

```python
sequence = 'vignesh'

# Index range exceeds the existing range 7 so it throws Index error 
print('sequence[10]',sequence[10])  
```

#### error

```python
Traceback (most recent call last):
File "/home/pknviki95/Learning/Python/concepts/Datatypes/String_datatypes/scripts/str_index_error.py", line 8, in <module>
    print('sequence[10]',sequence[10])
IndexError: string index out of range
```

### Types of Index:

#### Positive Index:

- Positive Index starts from first character of string. (i.e) ```0 to n```
- It consists of positive index numbers. 
- It starts from ```left to right (-->)```.
- first index value of string always starts with ```0```.

#### Negative Index:

- Positive Index starts from last character of string. (i.e) ```-n to -1```
- It consists of Negative index numbers. 
- It starts from ```right to left (<--)```.
- first index value of string always starts with ```-1```.

| **String**  |  **v**   |  **i** | **k** | **i** |
| :---:   | :---: | :---: | :---: | :---: |
| **Positive Index**  |  ```0```   |  ```1``` | ```2``` | ```3``` |
| **Negative Index**  |  ```-4```   |  ```-3``` | ```-2``` | ```-1``` |

#### [str_indexing.py](https://github.com/pknviki95/Python/tree/main/concepts/Datatypes/String_datatypes/scripts/str_indexing.py) - To find the index value of the string based on positive and negative index:

#### Positive Index:

```python
sequence = 'vignesh'

print('sequence[0]',sequence[0])
print('sequence[1]',sequence[1])
print('sequence[2]',sequence[2])
print('sequence[3]',sequence[3])
print('sequence[4]',sequence[4])
print('sequence[5]',sequence[5])
print('sequence[6]',sequence[6])
```
#### output:
```python
sequence[0] v
sequence[1] i
sequence[2] g
sequence[3] n
sequence[4] e
sequence[5] s
sequence[6] h
```

#### Negative Index:

```python
sequence = 'vignesh'

print('sequence[-1]',sequence[-1])
print('sequence[-2]',sequence[-2])
print('sequence[-3]',sequence[-3])
print('sequence[-4]',sequence[-4])
print('sequence[-5]',sequence[-5])
print('sequence[-6]',sequence[-6])
print('sequence[-7]',sequence[-7])
```
#### output:
```python
sequence[-1] h
sequence[-2] s
sequence[-3] e
sequence[-4] n
sequence[-5] g
sequence[-6] i
sequence[-7] v
```

### String Slicing(Working with Index): 

- Slicing is used to obtain sub-string from string by accessing index value of string.

```python
        variable[start index:end index:step] 

        # start index : starting index-value of string 
        # end index : ending index-value for string (i.e) len(str) 
        # step : range of sub-string from string 
```


#### [str_slicing.py](https://github.com/pknviki95/Python/tree/main/concepts/Datatypes/String_datatypes/scripts/str_slicing.py) - To obtain sub-string from string based on positive and negative index:

#### Positive Index slicing:

```python
sequence = 'vignesh'

#variable[start index:end index] 
print('Positive variable[start index:end index]: ',sequence[2:6]) 

#variable[:end index] - By default start index is index 0 so it is equivalent to variable[0:end index]
print('Positive variable[:end index]: ',sequence[:6])

#variable[start index:] - By default end index is last element index so it is equivalent to variable[start index:end index]
print('Positive variable[start index:]: ',sequence[2:])      

#variable[:] - Based on above default values it is equivalent to variable
print('Positive variable[:]: ',sequence[:])

#variable[start index:end index:step] - It returns from index 1->3->5 (start+2(step) till end index value)
print('Positive variable[start index:end index:step]: ',sequence[1:6:2])
```
#### output:
```python
Positive variable[start index:end index]:  gnes
Positive variable[:end index]:  vignes
Positive variable[start index:]:  gnesh
Positive variable[:]:  vignesh
Positive variable[start index:end index:step]:  ins
```

#### Negative Index slicing:

```python
sequence = 'vignesh'

#variable[start index:end index] - Here the start index/end index is equivalent negative index value of positive index
print('Negative variable[start index:end index]: ',sequence[-6:-2])  

#variable[:end index] - By default start index is index 0 equivalent negative index
print('Negative variable[:end index]: ',sequence[:-3])         

#variable[start index:] - Here the start index is equivalent negative index value of positive index
print('Negative variable[start index:]: ',sequence[-7:])   

#variable[start index:end index:step] - It returns from index 1->3->5 (start+3(step) till end index value)
print('Negative variable[start index:end index:step]: ',sequence[-7:-2:3]) 
```
#### output:
```python
Negative variable[start index:end index]:  igne
Negative variable[:end index]:  vign
Negative variable[start index:]:  vignesh
Negative variable[start index:end index:step]:  vn
```

### String Concatenation:

- String concatenation is the process of concatenating(joining) between strings using ```(+)``` operator.
- (i.e) Basic rules for concatenation is that argument that we use should be only between strings.

```python
            #string concatenation
            str + str 
```

#### [str_concantinate.py](https://github.com/pknviki95/Python/tree/main/concepts/Datatypes/String_datatypes/scripts/str_concantinate.py) -  concatenate two strings using + operator:

```python
string_1="Hello"
string_2="Good Morning!"

#String concatenation

final=string_1+'\t'+string_2                        #Hello+\t(tab space)+Good Morning!
print("final_concantinated string: ",final)
```
#### output:
```python
final_concantinated string:  Hello      Good Morning!
```

- String concatenation is applicable only if it is between string; if we are trying concatenation with string with other datatypes it throws Type error.

```python
            #Type error
            str+int
```

#### [str_concantinate_type_error.py](https://github.com/pknviki95/Python/tree/main/concepts/Datatypes/String_datatypes/scripts/str_concantinate_type_error.py) - concantinate strings with other datatype using + operator - Type error:

```python
string_1="Hello"
int_2=10

#String concatenation with other datatype

final=string_1+'\t'+int_2                   #Type error

print("final_concatenated string with other datatype : ",final)
```
#### error:

```python
Traceback (most recent call last):
File "/home/pknviki95/Learning/Python/concepts/Datatypes/String_datatypes/scripts/str_cat_type_error.py", line 16, in <module>
    final=string_1+'\t'+int_2                   #Type error
TypeError: can only concatenate str (not "int") to str
```

### String repeating:

- String repeating is the process of repeating concatenation(joining) of string using ```(*)``` operator
- (i.e) Basic rule is one argument should be by default string and the other integer type for number to perform repetitive.
- The order of usage can be random; it is also possible but make sure it satisfies basic rule of 1 str and 1 int 
- (i.e) ```[Number of repetitive] * str``` also possible
            
            #string repeating
            str * [Number of repetitive]
             
#### [str_repetative.py](https://github.com/pknviki95/Python/tree/main/concepts/Datatypes/String_datatypes/scripts/str_repetative.py) - concatenate string repetitively using * operator:

```python
string="viki"
repetative_count=4
print("string repetative: {}".format(string*repetative_count))              #str * [Number of repeatative]
```
#### output:
```python
string repetative: vikivikivikiviki
```

- If the basic rule is not followed and if both are repetative with str type then it throws type error
            
```python
            #type error
            str * str
```

#### [str_repetative_type_error.py](https://github.com/pknviki95/Python/tree/main/concepts/Datatypes/String_datatypes/scripts/str_repetative_type_error.py) -  concatenate two strings using * repetative operator - Type error:

```python
string_1="Hello"
string_2="Good Morning!"

final=string_1*string_2                    #Hello*Good Morning! 
print("final_concantinated string: ",final)
```
#### error:

```python
Traceback (most recent call last):
File "/home/pknviki95/Learning/Python/concepts/Datatypes/String_datatypes/scripts/str_repetative_type_error.py", line 14, in <module>
    final=string_1*string_2                    #Hello*Good Morning! 
TypeError: can't multiply sequence by non-int of type 'str'
```

### Summary of String datatypes:

| String types | Example program   | output    |
| :---:   |  :--- | :--- |
| ```String with single quotes``` | x='viki' <br>  print("X value is:",x) <br>   print(type(x))   |  X value is: viki <br> <class 'str'> |
| ```String with Double quotes``` | x="viki" <br>  print("X value is:",x) <br>   print(type(x))   |  X value is: viki <br> <class 'str'> |
| ```String with Triple quotes``` | x='''viki''' <br>  print("X value is:",x) <br>   print(type(x))   |  X value is: viki <br> <class 'str'> |

</details>
<details>
<summary>List datatypes:</summary>

## List datatypes - list():

- List is data type in python that can store values separated by ```,``` and enclosed within ```[ ]```.

```python
            List_variable=[element 1,element 2,...]
```

- List variable can contain duplicate elements with ordered preserved elements.
- Heterogeneous objects are allowed in list (i.e) it can hold int,str,list,dict,etc., elements within its collection enclosed in square bracket.
- List is Mutable object.

#### [list_type.py](https://github.com/pknviki95/Python/tree/main/concepts/Datatypes/List_datatypes/scripts/list_type.py) - To find the list type variable using type() function:

```python
list_variable =[1,'viki',[2,3],1]
print("The type of list_variable is: ",type(list_variable))
```
#### output:
```python
The type of list_variable is:  <class 'list'>
```

### Indexing:

- Elements of list can be accessed using indexing/slicing as list is ordered preserved

| **List**  |  **1**   |  **viki** | **[2,3]** | **1** |
| :---:   | :---: | :---: | :---: | :---: |
| **Positive Index**  |  ```0```   |  ```1``` | ```2``` | ```3``` |
| **Negative Index**  |  ```-4```   |  ```-3``` | ```-2``` | ```-1``` |

#### [list_indexing.py](https://github.com/pknviki95/Python/tree/main/concepts/Datatypes/List_datatypes/scripts/list_indexing.py) - To find the index value of the list based on positive and negative index

#### Positive Index:

```python
sequence = [1,'viki',[2,3],1]

print('sequence[0]',sequence[0])
print('sequence[1]',sequence[1])
print('sequence[2]',sequence[2])
print('sequence[3]',sequence[3])
```
#### output:
```python
sequence[0] 1
sequence[1] viki
sequence[2] [2, 3]
sequence[3] 1
```

#### Negative Index:

```python
sequence = [1,'viki',[2,3],1]

print('sequence[-1]',sequence[-1])
print('sequence[-2]',sequence[-2])
print('sequence[-3]',sequence[-3])
```

#### output:
```python
sequence[-1] 1
sequence[-2] [2, 3]
sequence[-3] viki
```

### Slicing:

- Sequence of list elements can be accessed using slicing

#### [list_slicing.py](https://github.com/pknviki95/Python/tree/main/concepts/Datatypes/List_datatypes/scripts/list_slicing.py) - To obtain elements from list based on positive and negative index:

#### Positive Index slicing:

```python
sequence = [1,'viki',[2,3],1,{1:'viki'},(1,3)]

#variable[start index:end index] 
print('Positive variable[start index:end index]: ',sequence[2:6]) 

#variable[:end index] - By default start index is index 0 so it is equivalent to variable[0:end index]
print('Positive variable[:end index]: ',sequence[:6])

#variable[start index:] - By default end index is last element index so it is equivalent to variable[start index:end index]
print('Positive variable[start index:]: ',sequence[2:])      

#variable[:] - Based on above default values it is equivalent to variable
print('Positive variable[:]: ',sequence[:])

#variable[start index:end index:step] - It returns from index 1->3->5 (start+2(step) till end index value)
print('Positive variable[start index:end index:step]: ',sequence[1:6:2])
```

#### output:
```c
Positive variable[start index:end index]:  [[2, 3], 1, {1: 'viki'}, (1, 3)]
Positive variable[:end index]:  [1, 'viki', [2, 3], 1, {1: 'viki'}, (1, 3)]
Positive variable[start index:]:  [[2, 3], 1, {1: 'viki'}, (1, 3)]
Positive variable[:]:  [1, 'viki', [2, 3], 1, {1: 'viki'}, (1, 3)]
Positive variable[start index:end index:step]:  ['viki', 1, (1, 3)]
```

#### Negative Index slicing:

```python
sequence = [1,'viki',[2,3],1,{1:'viki'},(1,3)]

#variable[start index:end index] - Here the start index/end index is equivalent negative index value of positive index
print('Negative variable[start index:end index]: ',sequence[-6:-2])  

#variable[:end index] - By default start index is index 0 equivalent negative index
print('Negative variable[:end index]: ',sequence[:-3])         

#variable[start index:] - Here the start index is equivalent negative index value of positive index
print('Negative variable[start index:]: ',sequence[-7:])        

#variable[start index:end index:step] - It returns from index 1->3->5 (start+3(step) till end index value)
print('Negative variable[start index:end index:step]: ',sequence[-7:-2:3])
```
#### output:

```python
Negative variable[start index:end index]:  [1, 'viki', [2, 3], 1]
Negative variable[:end index]:  [1, 'viki', [2, 3]]
Negative variable[start index:]:  [1, 'viki', [2, 3], 1, {1: 'viki'}, (1, 3)]
Negative variable[start index:end index:step]:  [1, 1]
```
</details>
<details>
<summary>Tuple datatypes:</summary>

## Tuple datatypes - tuple():


- Tuple is data type in python that can store values separated by ```,``` and enclosed within ```( )```

```python
            tuple_variable=(element 1,element 2,...)
```

- Tuple is read-only object version of list.
- Tuple variable can contain duplicate elements with ordered preserved elements.
- Heterogeneous objects are allowed in tuple (i.e) it can hold int,str,list,dict,etc., elements within its collection enclosed in () bracket.
- Tuple is immutable object - (i.e) Values of tuple object cannot be changed

#### [tuple_type.py](https://github.com/pknviki95/Python/tree/main/concepts/Datatypes/Tuple_datatypes/scripts/tuple_type.py) - To find the tuple variable using type() function:

```python
tuple_variable =(1,'viki',[2,3],1)
print("The type of tuple_variable is: ",type(tuple_variable))
```
#### output:
```python
The type of tuple_variable is:  <class 'tuple'>
```

### Indexing:

- Elements of tuple can be accessed using indexing/slicing as tuple is ordered preserved by it is only read-only changes to tuple object is not available as it is immutable

| **tuple**  |  **1**   |  **viki** | **[2,3]** | **1** |
| :---:   | :---: | :---: | :---: | :---: |
| **Positive Index**  |  ```0```   |  ```1``` | ```2``` | ```3``` |
| **Negative Index**  |  ```-4```   |  ```-3``` | ```-2``` | ```-1``` |

#### [tuple_indexing.py](https://github.com/pknviki95/Python/tree/main/concepts/Datatypes/Tuple_datatypes/scripts/tuple_indexing.py) - To find the index value of the tuple based on positive and negative index:

#### Positive Index:

```python
sequence = (1,'viki',[2,3],1)

print('sequence[0]',sequence[0])
print('sequence[1]',sequence[1])
print('sequence[2]',sequence[2])
print('sequence[3]',sequence[3])
```
#### output:
```python
sequence[0] 1
sequence[1] viki
sequence[2] [2, 3]
sequence[3] 1
```

#### Negative Index:

```python
sequence = (1,'viki',[2,3],1)

print('sequence[-1]',sequence[-1])
print('sequence[-2]',sequence[-2])
print('sequence[-3]',sequence[-3])
```

#### output:
```python
sequence[-1] 1
sequence[-2] [2, 3]
sequence[-3] viki
```

### Slicing:

- Sequence of tuple elements can be accessed using slicing.

#### [tuple_slicing.py](https://github.com/pknviki95/Python/tree/main/concepts/Datatypes/Tuple_datatypes/scripts/tuple_slicing.py) - To obtain elements from tuple based on positive and negative index:

#### Positive Index slicing:

```python
sequence = (1,'viki',[2,3],1,{1:'viki'},(1,3))

#variable[start index:end index] 
print('Positive variable[start index:end index]: ',sequence[2:6]) 

#variable[:end index] - By default start index is index 0 so it is equivalent to variable[0:end index]
print('Positive variable[:end index]: ',sequence[:6])

#variable[start index:] - By default end index is last element index so it is equivalent to variable[start index:end index]
print('Positive variable[start index:]: ',sequence[2:])      

#variable[:] - Based on above default values it is equivalent to variable
print('Positive variable[:]: ',sequence[:])

#variable[start index:end index:step] - It returns from index 1->3->5 (start+2(step) till end index value)
print('Positive variable[start index:end index:step]: ',sequence[1:6:2])
```

#### output:
```python
Positive variable[start index:end index]:  ([2, 3], 1, {1: 'viki'}, (1, 3))
Positive variable[:end index]:  (1, 'viki', [2, 3], 1, {1: 'viki'}, (1, 3))
Positive variable[start index:]:  ([2, 3], 1, {1: 'viki'}, (1, 3))
Positive variable[:]:  (1, 'viki', [2, 3], 1, {1: 'viki'}, (1, 3))
Positive variable[start index:end index:step]:  ('viki', 1, (1, 3))
```

#### Negative Index slicing:

```python
sequence = (1,'viki',[2,3],1,{1:'viki'},(1,3))

#variable[start index:end index] - Here the start index/end index is equivalent negative index value of positive index
print('Negative variable[start index:end index]: ',sequence[-6:-2])  

#variable[:end index] - By default start index is index 0 equivalent negative index
print('Negative variable[:end index]: ',sequence[:-3])         

#variable[start index:] - Here the start index is equivalent negative index value of positive index
print('Negative variable[start index:]: ',sequence[-7:])        

#variable[start index:end index:step] - It returns from index 1->3->5 (start+3(step) till end index value)
print('Negative variable[start index:end index:step]: ',sequence[-7:-2:3])
```
#### output:

```python
Negative variable[start index:end index]:  (1, 'viki', [2, 3], 1)
Negative variable[:end index]:  (1, 'viki', [2, 3])
Negative variable[start index:]:  (1, 'viki', [2, 3], 1, {1: 'viki'}, (1, 3))
Negative variable[start index:end index:step]:  (1, 1)
```

- Tuple is read-only immutable object is any changes are tried to made using attribute like list it throws error - Attribute error
- Based on below dir() function tuple doesn't have any write related operation only read related operations.
- If any attributes used apart from available one it throws attribute error

#### [tuple_attribute_error.py](https://github.com/pknviki95/Python/tree/main/concepts/Datatypes/Tuple_datatypes/scripts/tuple_attribute_error.py) - tuple is read-only immutable object is any changes are tried to made using attribute like list it throws error - Attribute error:

```python
tuple_variable=(1,2,3,4,'viki')


# Attribute error:
# If any attributes used apart from available one it throws attribute error
print(dir(tuple_variable))
tuple_variable.append(2)
```

#### dir() output:
```python
['__add__', '__class__', '__class_getitem__', '__contains__', '__delattr__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getitem__', '__getnewargs__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__iter__', '__le__', '__len__', '__lt__', '__mul__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__rmul__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', 'count', 'index']
```
#### error:

```python
Traceback (most recent call last):
File "/home/pknviki95/Learning/Python/concepts/Datatypes/Tuple_datatypes/scripts/tuple_attribute_error.py", line 13, in <module>
    tuple_variable.append(2)
AttributeError: 'tuple' object has no attribute 'append'
```

### Limitations:  

#### 1: Single valued tuple should ends with "," comma:

- By default all the single values of object is considered as single tuple object by Python virtual machine
- (i.e) consider assigning a integer value 10 

```python
            x=10 # equivalent to x=(10)
```
- Due to this above scenario all the single object elements inside tuple is considered to its equivalent datatypes
- To overcome come this scenario we need to tell the PVM that it is tuple variable/object by adding , after single tuple element

```python
            x=(10,)
```

#### [tuple_limitation.py](https://github.com/pknviki95/Python/tree/main/concepts/Datatypes/Tuple_datatypes/scripts/tuple_limitation.py) - Single value declaration with comma(",") to overcome above limitation:

#### multiple value declaration:

```python
tuple_multiple_variable =(1,2,'viki',[1,2])
print("The type of tuple_multiple_variable is: ",type(tuple_multiple_variable))
```

#### output:
```python
The type of tuple_multiple_variable is:  <class 'tuple'>
```
#### Single value declaration:

```python
tuple_single_variable_int =(1)
print("The type of tuple_single_variable_int is: ",type(tuple_single_variable_int))

tuple_single_variable_str =('viki')
print("The type of tuple_single_variable_str is: ",type(tuple_single_variable_str))

tuple_single_variable_list =([1,2])
print("The type of tuple_single_variable_list is: ",type(tuple_single_variable_list))

tuple_single_variable_bool =(True)
print("The type of tuple_single_variable_bool is: ",type(tuple_single_variable_bool))
```
#### output:
```python
The type of tuple_single_variable_int is:  <class 'int'>
The type of tuple_single_variable_str is:  <class 'str'>
The type of tuple_single_variable_list is:  <class 'list'>
The type of tuple_single_variable_bool is:  <class 'bool'>
```
#### Single value declaration with comma(",") to overcome above limitation:

```python
tuple_single_variable_int =(1,)
print("The type of tuple_single_variable_int with , is: ",type(tuple_single_variable_int))

tuple_single_variable_str =('viki',)
print("The type of tuple_single_variable_str with , is: ",type(tuple_single_variable_str))

tuple_single_variable_list =([1,2],)
print("The type of tuple_single_variable_list with , is: ",type(tuple_single_variable_list))

tuple_single_variable_bool =(True,)
print("The type of tuple_single_variable_bool with , is: ",type(tuple_single_variable_bool))
```

#### output:

```python
The type of tuple_single_variable_int with , is:  <class 'tuple'>
The type of tuple_single_variable_str with , is:  <class 'tuple'>
The type of tuple_single_variable_list with , is:  <class 'tuple'>
The type of tuple_single_variable_bool with , is:  <class 'tuple'>
```

- Declaration with comma(",") to overcome above limitation saying PVM to consider this single value as tuple element.

</details>
<details>
<summary>set datatypes:</summary>

## set datatypes - set():

- Set is data type in python that can store values separated by ```,``` and enclosed within ```{ }```.

```python
            set_variable={element 1,element 2,...}
```

- Set variable cannot contain duplicate elements.

#### [set_dup_unorder.py](https://github.com/pknviki95/Python/tree/main/concepts/Datatypes/Set_datatypes/scripts/set_dup_unorder.py) - To find the set variable return unordered value and neglecting of duplicate values:

```python
set_variable={1,2,3,4,'viki',(1,2),3,4}

# Neglecting Duplicate values and returningin un-ordered way:
print("unordered set_variable: {}".format(set_variable))
```

#### output:
```python
unordered set_variable: {1, 2, (1, 2), 3, 4, 'viki'} # Un-ordered value return for set
```

- Set variable un-ordered elements so indexing/Slicing operations cannot be performed.if tried indexing operation it throws type error.

#### [set_index_slice_type_error.py](https://github.com/pknviki95/Python/tree/main/concepts/Datatypes/Set_datatypes/scripts/set_index_slice_type_error.py) - Index/slice operation in set objects throws error as it is un-ordered datatype - Type error:

#### Indexing:
```python
set_variable={1,2,3,4,'viki',(1,2),3,4}

# Un-ordered value return for set if indexed throws error
print("unordered set_variable: {}".format(set_variable[1]))
```
#### slicing:

```python
set_variable={1,2,3,4,'viki',(1,2),3,4}

# Un-ordered value return for set if indexed throws error
print("unordered set_variable: {}".format(set_variable[1:2]))
```

#### error:
```python
Traceback (most recent call last):
File "/home/pknviki95/Learning/Python/concepts/Datatypes/Set_datatypes/scripts/set_index_type_error.py", line 11, in <module>
    print("unordered set_variable: {}".format(set_variable[1]))
TypeError: 'set' object is not subscriptable
```

- Set is mutable object - (i.e) Values of set object can be changed.

#### [set_type.py](https://github.com/pknviki95/Python/tree/main/concepts/Datatypes/Set_datatypes/scripts/set_type.py) - To find the set type variable using type() function:

```python
set_variable={1,2,3,4,'viki',(1,2),3,4}

print("unordered set_variable: {}".format(set_variable))
print("The type of set variable: {}".format(type(set_variable)))
```

#### output:
```python
unordered set_variable: {1, 2, (1, 2), 3, 4, 'viki'}  # Un-ordered value return for set
The type of set variable: <class 'set'>
```

### Limitations:

#### 1: Empty {} variable is considered as dictionary objects:

- By default The empty declaration of variable with {} is considered as Dictionary object. To tell PVM that it is set object we need to declare set(variable).

```python
            set_variable={}  # By default Dictionary object
            set(set_variable) # set object
```

#### [set_limitiation.py](https://github.com/pknviki95/Python/tree/main/concepts/Datatypes/Set_datatypes/scripts/set_limitiation.py) - To convert default empty dict to set object by declaring set() function:

#### without set () fun returns dict:
```python
# Empty variable with {} braces
set_variable={}
print("unordered set_variable type without set() function: {}".format(type(set_variable)))
```

#### output:
```python
unordered set_variable type without set() function: <class 'dict'>
```

#### with set () fun returns set:
```python
# Empty variable with {} braces
set_variable={}
print("unordered set_variable type with set() function: {}".format(type(set(set_variable))))
```
#### output:

```python
unordered set_variable type with set() function: <class 'set'>
```

#### 2: Declaring dict,list,set( Mutable objects) inside set variable it throws Type error -  unhashable type:

- Heterogeneous objects are allowed in set (i.e) it can hold int,str,tuple etc., elements within its collection enclosed in {} bracket.
- If any values like dict,list,set( Mutable objects) inside set variable it throws Type error -  unhashable type

#### [set_unhashable_type_error.py](https://github.com/pknviki95/Python/tree/main/concepts/Datatypes/Set_datatypes/scripts/set_unhashable_type_error.py)  - Declaring dict,list,set( Mutable objects) inside set variable it throws - Type error - unhashable type:

#### set with list elements:

```python
set_variable_list=set({[1,2]})
print(" The set variable with list elements: ",set_variable_list)
```

#### error:

```python
Traceback (most recent call last):
File "/home/pknviki95/Learning/Python/concepts/Datatypes/Set_datatypes/scripts/set_unhashable_type_error.py", line 9, in <module>
    set_variable_list={[1,2]}
TypeError: unhashable type: 'list'
```

#### set with dict elements:

```python
set_variable_dict=set({{1:'viki'}})
print(" The set variable with dict elements: ",set_variable_dict)
```
#### error:
```python
Traceback (most recent call last):
File "/home/pknviki95/Learning/Python/concepts/Datatypes/Set_datatypes/scripts/set_unhashable_type_error.py", line 12, in <module>
    set_variable_dict={{1:'viki'}}
TypeError: unhashable type: 'dict'
```

#### set with set elements:

```python
set_variable_set=set({{1,2}})
print(" The set variable with set elements: ",set_variable_set)
```

#### error:

```python
Traceback (most recent call last):
File "/home/pknviki95/Learning/Python/concepts/Datatypes/Set_datatypes/scripts/set_unhashable_type_error.py", line 15, in <module>
    set_variable_set={{1,2}}
TypeError: unhashable type: 'set'
```
</details>
<details>
<summary>Frozenset datatypes:</summary>

# Frozenset datatypes - frozenset():

- Frozenset datatypes is similar to Set data type in python that can store values separated by ```,``` and enclosed within ```{}```.but it should be assigned to ```frozenset(set_variable)```

```python
            set_variable={element 1,element 2,...}   # set variable
            frozenset(set_variable)                  # frozen set variable
```

- Frozenset variable cannot contain duplicate elements.
- Frozenset variable un-ordered elements so indexing/Slicing operations cannot be performed.if tried indexing operation it throws type error
- The Main difference between set is ```Mutable``` and Frozenset is ```Immutable``` 
- (i.e) "set objects values can be changed as it is mutable" but not for "frozen set as it is immutable"

#### [frozenset_type.py](https://github.com/pknviki95/Python/tree/main/concepts/Datatypes/Frozenset_datatypes/scripts/frozenset_type.py) - To find the frozenset type variable using type() function:

```python
set_variable={1,2,3,4,'viki',(1,2),3,4}

print("The type of set variable after frozenset: {}".format(type(set_variable)))

frozenset_variable=frozenset(set_variable)

# Un-ordered value return for set
print("unordered set_variable after frozenset: {}".format(frozenset_variable))

print("The type of set variable after frozenset: {}".format(type(frozenset_variable)))
```

#### output:
```python
The type of set variable after frozenset: <class 'set'>
unordered set_variable after frozenset: frozenset({1, 2, (1, 2), 3, 4, 'viki'})
The type of set variable after frozenset: <class 'frozenset'>
```

- Based on below dir() function frozenset doesn't have any write related operation only read related operations.
- If any attributes used apart from available one it throws attribute error.

#### [frozenset_attribute_error.py](https://github.com/pknviki95/Python/tree/main/concepts/Datatypes/Frozenset_datatypes/scripts/frozenset_attribute_error.py) - frozenset is read-only immutable object is any changes are tried to made using attribute like list it throws error - Attribute error:

#### dir() output:

```python
['__and__', '__class__', '__class_getitem__', '__contains__', '__delattr__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__iter__', '__le__', '__len__', '__lt__', '__ne__', '__new__', '__or__', '__rand__', '__reduce__', '__reduce_ex__', '__repr__', '__ror__', '__rsub__', '__rxor__', '__setattr__', '__sizeof__', '__str__', '__sub__', '__subclasshook__', '__xor__', 'copy', 'difference', 'intersection', 'isdisjoint', 'issubset', 'issuperset', 'symmetric_difference', 'union']
```

#### error:

```python
Traceback (most recent call last):
File "/home/pknviki95/Learning/Python/concepts/Datatypes/Frozen_set_datatypes/scripts/frozenset_attribute_error.py", line 18, in <module>
    frozenset_variable.add(3)
AttributeError: 'frozenset' object has no attribute 'add'
```

</details>
<details>
<summary>Dictionary datatypes:</summary>

## Dictionary datatypes - dict():

- The dict datatype is used to represent collection of elements in ```{key:value}``` pair.
- The dictionary datatype is un-ordered collection of key value pair elements (i.e) Indexing and slicing is not possible
- Dictionary is mutable (i.e) The value of dictionary can be edited or changed.

```python
        dictionary_variable={key_1:value_1, key_2:value_2, ...}
```


#### [dict_type.py](https://github.com/pknviki95/Python/tree/main/concepts/Datatypes/Dictionary_datatypes/scripts/dict_type.py) - To find the dictionary type variable using type() function:

```python
dictionary_variable = {1:'viki',2:'siva'}
print("The type of dictionary_variable is: ",type(dictionary_variable))
```
#### output:
```python
The type of dictionary_variable is:  <class 'dict'>
```

- Key and values can be added to dictionary by assigning of value to key for a given dictionary using below syntax.

```python
            dictionary_variable[key]=value 
```
                
#### [dict_add_value_key.py](https://github.com/pknviki95/Python/tree/main/concepts/Datatypes/Dictionary_datatypes/scripts/dict_add_value_key.py) - To add the value to key to empty dictionary or add key and value to dictionary:


```python
dictionary_variable = {1:'viki',2:'siva'}

# Adding key 3 and its vaue karthi to dictionary_variable 

#dictionary_variable[key]=value
dictionary_variable[3]='karthi'
                
print("The type of dictionary_variable is: ",dictionary_variable)
```

#### output:

```python
The type of dictionary_variable is:  {1: 'viki', 2: 'siva', 3: 'karthi'}
```

- Duplicate keys are not allowed but duplicate values are allowed.
- It doesn't throw error when duplicate key is used instead it updates the existing key to new value assigned to it.

#### [dict_dup_key_value.py](https://github.com/pknviki95/Python/tree/main/concepts/Datatypes/Dictionary_datatypes/scripts/dict_dup_key_value.py) - To verify the condition of duplicate key and value in dictionary:

#### Duplicate key:
```python
dictionary_variable={1:'viki',2:'guru'}

# Adding duplicate key to dictionary_variable
dictionary_variable[2]='karthi'

print("dictionary_variable after adding duplicate key: ",dictionary_variable)
```  

#### output:
```python
dictionary_variable after adding duplicate key:  {1: 'viki', 2: 'karthi'}
```

#### Duplicate value:

```c
dictionary_variable={1:'viki',2:'guru'}

# Adding duplicate value to dictionary_variable
dictionary_variable[1]='karthi'
dictionary_variable[2]='karthi'
dictionary_variable[3]='karthi'

print("dictionary_variable after adding duplicate value: ",dictionary_variable)
```

#### output:
```python
dictionary_variable after adding duplicate value:  {1: 'karthi', 2: 'karthi', 3: 'karthi'}
```
</details>
<details>
<summary>Range datatypes:</summary>

## Range datatypes - range():

- Range Datatype is Sequence of numbers (i.e) number in range.
- Range can be accessed using index value (i.e) Indexing/Slicing is possible

```python
        range_variable=range(number)

        # number - sequence of number from 0 to n-1
```

- Range can be accessed based on specific range values - Slicing.
        
```python
    range_variable=range(begin number,end number,step)

        # begin number - sequence of number to start
        # end number - sequence of number to end end=n-1
        # step - sequence of number in specific steps
```

#### [range_type.py](https://github.com/pknviki95/Python/tree/main/concepts/Datatypes/Range_datatypes/scripts/range_type.py) - To find the range variable using type() function:

```python
range_variable=range(10)
print("The type of range_variable : ",type(range_variable))
```

#### output:

```python
The type of range_variable :  <class 'range'>
```

### Indexing:

- Elements of range can be accessed using indexing/slicing as range is ordered preserved.

#### [range_indexing.py](https://github.com/pknviki95/Python/tree/main/concepts/Datatypes/Range_datatypes/scripts/range_indexing.py) - To find the index value of the range based on positive and negative index

```python
            range_variable[index]
```

#### Positive Index:

```python
sequence = range(4)

print('sequence[0]',sequence[0])
print('sequence[1]',sequence[1])
print('sequence[2]',sequence[2])
print('sequence[3]',sequence[3])
```
#### output:

```python
sequence[0] 0
sequence[1] 1
sequence[2] 2
sequence[3] 3
```

#### Negative Index:

```python
sequence = range(4)

print('sequence[-1]',sequence[-1])
print('sequence[-2]',sequence[-2])
print('sequence[-3]',sequence[-3])
print('sequence[-4]',sequence[-4])
```

#### output:

```python
sequence[-1] 3
sequence[-2] 2
sequence[-3] 1
sequence[-4] 0
```

### Slicing:

- Sequence of range elements can be accessed using slicing.

```python
        range_variable[start index, end index, step]

            # start index - By default it is 0 ; This can be changes based on requirement
            # end index - Last index value len(variable)-1
            # step  - Sequence of number in specific index steps
```

#### [range_slicing.py](https://github.com/pknviki95/Python/tree/main/concepts/Datatypes/Range_datatypes/scripts/range_slicing.py) - To find the index value of the range based on positive and negative index using slicing operation:

#### Positive Index slicing:

```python
sequence = range(10)

#variable[start index:end index] 
print('Positive variable[start index:end index]: ',sequence[2:6]) 

#variable[:end index] - By default start index is index 0 so it is equivalent to variable[0:end index]
print('Positive variable[:end index]: ',sequence[:6])

#variable[start index:] - By default end index is last element index so it is equivalent to variable[start index:end index]
print('Positive variable[start index:]: ',sequence[2:])      

#variable[:] - Based on above default values it is equivalent to variable
print('Positive variable[:]: ',sequence[:])

#variable[start index:end index:step] - It returns from index 1->3->5 (start+2(step) till end index value)
print('Positive variable[start index:end index:step]: ',sequence[1:6:2])
```

#### output:
```python
Positive variable[start index:end index]:  range(2, 6)
Positive variable[:end index]:  range(0, 6)
Positive variable[start index:]:  range(2, 10)
Positive variable[:]:  range(0, 10)
Positive variable[start index:end index:step]:  range(1, 6, 2)
```

#### Negative Index slicing:

```python
sequence = range(10)

#variable[start index:end index] - Here the start index/end index is equivalent negative index value of positive index
print('Negative variable[start index:end index]: ',sequence[-6:-2])  

#variable[:end index] - By default start index is index 0 equivalent negative index
print('Negative variable[:end index]: ',sequence[:-3])         

#variable[start index:] - Here the start index is equivalent negative index value of positive index
print('Negative variable[start index:]: ',sequence[-7:])        

#variable[start index:end index:step] - It returns from index 1->3->5 (start+3(step) till end index value)
print('Negative variable[start index:end index:step]: ',sequence[-7:-2:3])
```

#### output:
```python
Negative variable[start index:end index]:  range(4, 8)
Negative variable[:end index]:  range(0, 7)
Negative variable[start index:]:  range(3, 10)
Negative variable[start index:end index:step]:  range(3, 8, 3)
```

- Range Datatype is immutable (i.e) Its values cannot be Updated or changed.

#### [range_type_error.py](https://github.com/pknviki95/Python/tree/main/concepts/Datatypes/Range_datatypes/scripts/range_type_error.py) - range values cannot be changed as it is immutable if tried to change it throws error - Type error:


```python
sequence = range(4)

# Assigning value to range variable - Type error
sequence[0]=10 

print('sequence[0]',sequence[0])
```

#### error:

```python
Traceback (most recent call last):
File "/home/pknviki95/Learning/Python/concepts/Datatypes/Range_datatypes/scripts/range_type_error.py", line 9, in <module>
    sequence[0]=10 
TypeError: 'range' object does not support item assignment
```
</details>
<details>
<summary>Bytes Datatypes:</summary>

## Bytes Datatypes - bytes():

- Python bytes are a sequence of integers in the range of ```0-255```. 
- Bytes are an immutable sequence data type, meaning once a bytes object is created, it cannot be changed.
- They are ordered sequence (i.e) Indexing and slicing operation are possible.

```python
            list_variable=[element_1,element_2,...]
            bytes_variable=bytes(list_variable)
```


#### [bytes_type.py](https://github.com/pknviki95/Python/tree/main/concepts/Datatypes/Bytes_datatypes/scripts/bytes_type.py) - To find the bytes type variable using type() function:

```python
# sequence of numbers range from 0-255

list_variable=[1,2,3,65,66]

# bytes() for using bytes objects
bytes_variable=bytes(list_variable)

print("bytes_variable: ",bytes_variable)
print("The type of bytes_variable : ",type(bytes_variable))
```

#### output:

```python
bytes_variable:  b'\x01\x02\x03AB'
The type of bytes_variable :  <class 'bytes'>
```

### Indexing:

- Elements of bytes can be accessed using indexing/slicing as bytes is ordered preserved.

#### [bytes_indexing.py](https://github.com/pknviki95/Python/tree/main/concepts/Datatypes/Bytes_datatypes/scripts/bytes_indexing.py) - To find the index value of the bytes based on positive and negative index:

#### Positive Index:

```python
sequence = [65,66,67,68]
bytes_variable=bytes(sequence)

print(bytes_variable)

print('bytes_variable[0]',bytes_variable[0])
print('bytes_variable[1]',bytes_variable[1])
print('bytes_variable[2]',bytes_variable[2])
print('bytes_variable[3]',bytes_variable[3])
```
#### output:
```python
b'ABCD'
bytes_variable[0] 65
bytes_variable[1] 66
bytes_variable[2] 67
bytes_variable[3] 68
```
#### Negative Index:

```python
sequence = [65,66,67,68]
bytes_variable=bytes(sequence)

print('bytes_variable[-1]',bytes_variable[-1])
print('bytes_variable[-2]',bytes_variable[-2])
print('bytes_variable[-3]',bytes_variable[-3])
print('bytes_variable[-4]',bytes_variable[-4])
```
#### output:

```python
bytes_variable[-1] 68
bytes_variable[-2] 67
bytes_variable[-3] 66
bytes_variable[-4] 65
```

### Slicing:

- Sequence of bytes elements can be accessed using slicing.

#### [bytes_slicing.py](https://github.com/pknviki95/Python/tree/main/concepts/Datatypes/Bytes_datatypes/scripts/bytes_slicing.py) - To access the sequence of bytes based on positive and negative index usig slicing operation:

#### Positive Index slicing:

```python
sequence = [65,66,67,68,69,1,2,3]
bytes_variable=bytes(sequence)


#variable[start index:end index] 
print('Positive variable[start index:end index]: ',bytes_variable[2:6]) 

#variable[:end index] - By default start index is index 0 so it is equivalent to variable[0:end index]
print('Positive variable[:end index]: ',bytes_variable[:6])

#variable[start index:] - By default end index is last element index so it is equivalent to variable[start index:end index]
print('Positive variable[start index:]: ',bytes_variable[2:])      

#variable[:] - Based on above default values it is equivalent to variable
print('Positive variable[:]: ',bytes_variable[:])

#variable[start index:end index:step] - It returns from index 1->3->5 (start+2(step) till end index value)
print('Positive variable[start index:end index:step]: ',bytes_variable[1:6:2])
```
#### output:
```python
Positive variable[start index:end index]:  b'CDE\x01'
Positive variable[:end index]:  b'ABCDE\x01'
Positive variable[start index:]:  b'CDE\x01\x02\x03'
Positive variable[:]:  b'ABCDE\x01\x02\x03'
Positive variable[start index:end index:step]:  b'BD\x01'
```

#### Negative Index slicing:

```python
sequence = [65,66,67,68,69,1,2,3]
bytes_variable=bytes(sequence)

#variable[start index:end index] - Here the start index/end index is equivalent negative index value of positive index
print('Negative variable[start index:end index]: ',bytes_variable[-6:-2])  

#variable[:end index] - By default start index is index 0 equivalent negative index
print('Negative variable[:end index]: ',bytes_variable[:-3])         

#variable[start index:] - Here the start index is equivalent negative index value of positive index
print('Negative variable[start index:]: ',bytes_variable[-7:])        

#variable[start index:end index:step] - It returns from index 1->3->5 (start+3(step) till end index value)
print('Negative variable[start index:end index:step]: ',bytes_variable[-7:-2:3])
```
#### output:

```python
Negative variable[start index:end index]:  b'CDE\x01'
Negative variable[:end index]:  b'ABCDE'
Negative variable[start index:]:  b'BCDE\x01\x02\x03'
Negative variable[start index:end index:step]:  b'BE'
```

#### [bytes_256_value_error.py](https://github.com/pknviki95/Python/tree/main/concepts/Datatypes/Bytes_datatypes/scripts/bytes_256_value_error.py) - Bytes type support sequence of elements from range 0-255 if it exceeds it throws error - Value error:

```python
# sequence of numbers exceeds range from 0-255 - value error

list_variable=[1,2,3,65,66,256]

# bytes() for using bytes objects
bytes_variable=bytes(list_variable)

print("bytes_variable: ",bytes_variable)
```

#### error:
```python
Traceback (most recent call last):
File "/home/pknviki95/Learning/Python/concepts/Datatypes/Bytes_datatypes/scripts/bytes_256_value_error.py", line 12, in <module>
    bytes_variable=bytes(list_variable)
ValueError: bytes must be in range(0, 256)
```

#### [bytes_type_error.py](https://github.com/pknviki95/Python/tree/main/concepts/Datatypes/Bytes_datatypes/scripts/bytes_type_error.py) - Bytes type cannot be updated or changed as it is immutable if done it throws error- Type error :

```python
sequence = [65,66,67,68]
bytes_variable=bytes(sequence)

# Assigning value to bytes variable throws Type error
bytes_variable[2]=60
print(bytes_variable)
```

#### error:

```python
Traceback (most recent call last):
File "/home/pknviki95/Learning/Python/concepts/Datatypes/Bytes_datatypes/scripts/bytes_type_error.py", line 10, in <module>
    bytes_variable[2]=60
TypeError: 'bytes' object does not support item assignment
```

#### NOTE: 
- Above Type error is neglected by using the bytearray() datatype as it is Mutable object - [Bytearray datatypes](https://github.com/pknviki95/Python/tree/main/concepts/Datatypes/Bytearray_datatypes)

</details>
<details>
<summary>ByteArray Datatypes:</summary>

## ByteArray Datatypes - bytearray():

- Python bytearray are a sequence of integers in the range of 0-255. it is similar to bytes 
- Bytearray are an mutable sequence data type, meaning once a bytes object is created, it can be changed.
- (i.e) unlike bytes object the changes can be made on sequence using bytearray() object
- They are ordered sequence (i.e) Indexing and slicing operation are possible.

```python
                list_variable=[element_1,element_2,...]
                bytearrray_variable=bytearray(list_variable)
```

#### [bytearray_type.py](https://github.com/pknviki95/Python/tree/main/concepts/Datatypes/Bytearray_datatypes/scripts/bytearray_type.py) - To find the bytearray type variable using type() function:

```python
# sequence of numbers range from 0-255

list_variable=[1,2,3,65,66]

# bytearray() for using bytearray objects
bytearray_variable=bytearray(list_variable)

print("bytearray_variable: ",bytearray_variable)
print("The type of bytearray_variable : ",type(bytearray_variable))
```

#### output:

```python
bytearray_variable:  bytearray(b'\x01\x02\x03AB')
The type of bytearray_variable :  <class 'bytearray'>
```

### Indexing:

- Elements of bytes can be accessed using indexing/slicing as bytes is ordered preserved.

#### [bytearray_indexing.py](https://github.com/pknviki95/Python/tree/main/concepts/Datatypes/Bytearray_datatypes/scripts/bytearray_indexing.py) - To find the index value of the bytearray based on positive and negative index:

#### Positive Index:

```python
sequence = [65,66,67,68]
bytearray_variable=bytearray(sequence)

print(bytearray_variable)

print('bytearray_variable[0]',bytearray_variable[0])
print('bytearray_variable[1]',bytearray_variable[1])
print('bytearray_variable[2]',bytearray_variable[2])
print('bytearray_variable[3]',bytearray_variable[3])
```
#### output:
```python
b'ABCD'
bytes_variable[0] 65
bytes_variable[1] 66
bytes_variable[2] 67
bytes_variable[3] 68
```
#### Negative Index:

```python
sequence = [65,66,67,68]
bytearray_variable=bytearray(sequence)

print('bytearray_variable[-1]',bytearray_variable[-1])
print('bytearray_variable[-2]',bytearray_variable[-2])
print('bytearray_variable[-3]',bytearray_variable[-3])
print('bytearray_variable[-4]',bytearray_variable[-4])
```
#### output:

```python
bytes_variable[-1] 68
bytes_variable[-2] 67
bytes_variable[-3] 66
bytes_variable[-4] 65
```

### Slicing:

- Sequence of bytes elements can be accessed using slicing.

#### [bytearray_slicing.py](https://github.com/pknviki95/Python/tree/main/concepts/Datatypes/Bytearray_datatypes/scripts/bytearray_slicing.py) - To access the sequence of bytes based on positive and negative index using slicing operation:

#### Positive Index slicing:

```python
sequence = [65,66,67,68,69,1,2,3]

bytearray_variable=bytearray(sequence)

#variable[start index:end index] 

print('Positive variable[start index:end index]: ',bytearray_variable[2:6]) 

#variable[:end index] - By default start index is index 0 so it is equivalent to variable[0:end index]

print('Positive variable[:end index]: ',bytearray_variable[:6])

#variable[start index:] - By default end index is last element index so it is equivalent to variable[start index:end index]

print('Positive variable[start index:]: ',bytearray_variable[2:])      

#variable[:] - Based on above default values it is equivalent to variable

print('Positive variable[:]: ',bytearray_variable[:])

#variable[start index:end index:step] - It returns from index 1->3->5 (start+2(step) till end index value)

print('Positive variable[start index:end index:step]: ',bytearray_variable[1:6:2])
```
#### output:
```python
Positive variable[start index:end index]:  bytearray(b'CDE\x01')
Positive variable[:end index]:  bytearray(b'ABCDE\x01')
Positive variable[start index:]:  bytearray(b'CDE\x01\x02\x03')
Positive variable[:]:  bytearray(b'ABCDE\x01\x02\x03')
Positive variable[start index:end index:step]:  bytearray(b'BD\x01')
```


#### Negative Index slicing:

```python
sequence = [65,66,67,68,69,1,2,3]
bytearray_variable=bytearray(sequence)

#variable[start index:end index] - Here the start index/end index is equivalent negative index value of positive index

print('Negative variable[start index:end index]: ',bytearray_variable[-6:-2])  

#variable[:end index] - By default start index is index 0 equivalent negative index

print('Negative variable[:end index]: ',bytearray_variable[:-3])         

#variable[start index:] - Here the start index is equivalent negative index value of positive index

print('Negative variable[start index:]: ',bytearray_variable[-7:])        

#variable[start index:end index:step] - It returns from index 1->3->5 (start+3(step) till end index value)
print('Negative variable[start index:end index:step]: ',bytearray_variable[-7:-2:3])
```
#### output:

```python
Negative variable[start index:end index]:  bytearray(b'CDE\x01')
Negative variable[:end index]:  bytearray(b'ABCDE')
Negative variable[start index:]:  bytearray(b'BCDE\x01\x02\x03')
Negative variable[start index:end index:step]:  bytearray(b'BE')
```

#### [bytearray_256_value_error.py](https://github.com/pknviki95/Python/tree/main/concepts/Datatypes/Bytearray_datatypes/scripts/bytearray_256_value_error.py) - Bytearray type support sequence of elements from range 0-255 if it exceeds it throws error - Value error:

```python
# sequence of numbers exceeds range from 0-255 - value error

list_variable=[1,2,3,65,66,256]

# bytes() for using bytes objects

bytearray_variable=bytearray(list_variable)

print("bytearray_variable: ",bytearray_variable)
```

#### error:
```python
Traceback (most recent call last):
File "/home/pknviki95/Learning/Python/concepts/Datatypes/Bytearray_datatypes/scripts/bytearray_256_value_error.py", line 12, in <module>
    bytearray_variable=bytearray(list_variable)
ValueError: byte must be in range(0, 256)
```

#### [bytearray_assigning.py](https://github.com/pknviki95/Python/tree/main/concepts/Datatypes/Bytearray_datatypes/scripts/bytearray_assigning.py) - Bytearray type can be updated or changed as it is mutable:

```python
sequence = [65,66,67,68]

bytearray_variable=bytearray(sequence)

print("bytearray_variable before assigning: ",bytearray_variable)

# Assigning value to bytearray variable is possible as it is Mutable object

bytearray_variable[2]=1

print("bytearray_variable after assigning: ",bytearray_variable)
```

#### output:
```python
bytearray_variable before assigning:  bytearray(b'ABCD')
bytearray_variable after assigning:  bytearray(b'AB\x01D')
```
</details>
<details>
<summary>None datatypes:</summary>

## None datatypes - None:

- None is a special data type in Python that represents the absence of a value or a null value. 
- It is an object of its own datatype, the NoneType.

```python
            None_variable=None
 ```

- None is mostly used in scenario where a object needs to be assigned and keep an address reserved or future use.

#### [none_type.py](https://github.com/pknviki95/Python/tree/main/cconcepts/Datatypes/NONE_datatypes/scripts/none_type.py) - To find the none type variable using type() function:
```python
none_variable=None
none_variable_1=None

# Id of the None variable remain same as it is pointing to same object value

print("The identity of none_variable: ",id(none_variable))

print("The identity of none_variable_1: ",id(none_variable_1))

print("The Type of none_variable: ",type(none_variable))

```
#### output:

 ```python
The identity of none_variable:  94141827290080
The identity of none_variable_1:  94141827290080
The Type of none_variable:  <class 'NoneType'>
 ```
</details>
<details>
<summary>Differences between Datatypes based on its characteristics:</summary>

### Differences between Datatypes based on its characteristics:

| **Datatypes**  |  ```Ordered```   |  ```Un-ordered``` | ```Mutable``` | ```Immutable``` | ```Duplicates``` | ```Indexing/Slicing``` |
| :---:   | :---: | :---: | :---: | :---: | :---: | :---: | 
| ```Integer```  |  :x:  |  :heavy_check_mark: | :x: | :heavy_check_mark: | :x: | :x: |
| ```Float```  |  :x:  |  :heavy_check_mark: | :x: | :heavy_check_mark: | :x: | :x: |
| ```complex```  |  :x:  |  :heavy_check_mark: | :x: | :heavy_check_mark: | :x: | :x: |
| ```boolean```  |  :x:  |  :heavy_check_mark: | :x: | :heavy_check_mark: | :x: | :x: |
| ```string```  |  :x:  |  :x: | :x: | :heavy_check_mark: | :x: | :heavy_check_mark:
| ```list```  |  :heavy_check_mark:  |  :x: | :heavy_check_mark: | :x: | :heavy_check_mark: |:heavy_check_mark: |
| ```tuple```  |  :heavy_check_mark:  |  :x: | :x: | :heavy_check_mark: | :heavy_check_mark: |:heavy_check_mark: |
| ```set```    | :x:  |  :heavy_check_mark: | :heavy_check_mark: | :x: | :x: | :x: |
| ```frozenset```  | :x:  |  :heavy_check_mark: | :x: | :heavy_check_mark: | :x: | :x: |
| ```dictionary```  |  :x: |  :heavy_check_mark:  | :heavy_check_mark: | :x: | :heavy_check_mark: ```- for values``` <br> :x: ```- for key```| :x: |
| ```range```  |  :heavy_check_mark:  |  :x: | :x: | :heavy_check_mark: | :x: | :heavy_check_mark: |
| ```bytes```  |  :heavy_check_mark:  |  :x: | :x: | :heavy_check_mark: | :heavy_check_mark: |:heavy_check_mark: |
| ```Byte array```  |  :heavy_check_mark:  |  :x: | :heavy_check_mark: | :x: | :heavy_check_mark: |:heavy_check_mark: |
