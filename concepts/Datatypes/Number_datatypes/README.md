# Number datatypes:

- Python supports the below standard data types: 

## Various types of Numbers Datatypes:

- Number datatype are classified based on type of value we use

    - **Integer datatype**
    - **float datatype**
    - **complex datatype**

# int() - Integer datatypes

- Integers – No limit to the value of integers
- By default Python takes integer as decimal value
                
            1,1234

### [integer_type.py](https://github.com/pknviki95/Python/tree/main/concepts/Datatypes/Number_datatypes/Integer/scripts/integer_type.py) - To find the integer type variable using type() function:

            x=11 
            print("X value is:",x)   
            print("The type of x is: ",type(x))

## Different types of integer Numbers forms:
 
| Integer type | value    | Description  |
| :---:   | :---: | :--- |
| **Decimal form (base-10)** | 0-9   | By default all the number are in decimal form (0-9) |
| **Binary form (base-2)** | 0 and 1   | The binary form has **0b/0B** as the prefix |
| **Octal form (base-8)** | 0-7   | The octal form has **0o/0O** as the prefix | 
| **Hexadecimal form (base-16)** | 0-9 and A-F   | The Hexadecimal form has  **0x/0X** as a prefix | 

## Various integral form to decimal conversion:

### NOTE: 
- By default Python takes all the integer value as **decimal value**

| Integer type | value    | Conversion formula    | Final output|
| :---   | :---: | :---: | :--- |
| **Binary to decimal** | A=0b1111   | (1111)<sub>2</sub> => (2<sup>3</sup>+2<sup>2</sup>+2<sup>1</sup>+2<sup>0</sup>) = (8 * 1 + 4 * 1 + 2 * 1 + 1 * 1)   | 15 |
| **Octal to decimal** | A=0o1234   | (1234)<sub>8</sub> => (8<sup>3</sup>+8<sup>2</sup>+8<sup>1</sup>+8<sup>0</sup>) = (512 * 1 + 64 * 2 + 8 * 3 + 1 * 4)   | 668 |
| **Hexadecimal to decimal** | A=0xFACE | (FACE)<sub>16</sub> => (16<sup>3</sup>+16<sup>2</sup>+16<sup>1</sup>+16<sup>0</sup>) = ( 4096 * 15 + 256 * 10 + 16 * 12 + 1 * 14 )| 64206 | 

## Base Conversion in-built function:

- The in-built base conversion helps **to convert from one base to other base integer form**
- These functions are **applicable only for integer type**
- Three types

    - **bin()**
    - **hex()**
    - **oct()**

## bin():

- To convert other functions to **binary form (base-2)**

### [bin_base_conversion.py](https://github.com/pknviki95/Python/tree/main/concepts/Datatypes/Number_datatypes/Integer/scripts/bin_base_conversion.py) - To convert decimal/octal/hexadecimal form to binary form using bin() function:

### decimal to binary:
                    dec_bin=53
                    print("The binary form of dec_bin : ",bin(dec_bin))
#### output:
            The binary form of dec_bin :  0b110101

### octal to binary:

                oct_bin=0o123
                print("The binary form of oct_bin : ",bin(oct_bin))
#### output:
            The binary form of oct_bin :  0b1010011

### hexadecimal to binary:

                hex_bin=0xface
                print("The binary form of hex_bin : ",bin(hex_bin))
#### output:
            The binary form of hex_bin :  0b1111101011001110

## hex():

- To convert other functions to **hexadecimal form (base-16)**

### [hex_base_conversion.py](https://github.com/pknviki95/Python/tree/main/concepts/Datatypes/Number_datatypes/Integer/scripts/hex_base_conversion.py) -  To convert decimal/octal/binary form to hexadecimal form using hex() function:

### decimal to hexadecimal:

                dec_hex=123
                print("The Hexadecimal form of dec_hex : ",hex(dec_hex))

#### output:
            The Hexadecimal form of dec_hex :  0x7b

### octal to hexadecimal:

                oct_hex=0o123
                print("The Hexadecimal form of oct_hex : ",hex(oct_hex))
#### output:
            The Hexadecimal form of oct_hex :  0x53

### binary to hexadecimal:

                bin_hex=0b1111101011001110
                print("The Hexadecimal form of bin_hex : ",hex(bin_hex))
#### output:
            The Hexadecimal form of bin_hex :  0xface

## oct(): 

- To convert other functions to **octal form (base-8)**

### [oct_base_conversion.py](https://github.com/pknviki95/Python/tree/main/concepts/Datatypes/Number_datatypes/Integer/scripts/oct_base_conversion.py) -  To convert decimal/hexadecimal/binary form to octal form using oct() function:

### decimal to octal:

                dec_oct=123
                print("The octal form of dec_oct : ",oct(dec_oct))
#### output:
            The octal form of dec_oct :  0o173

### binary to octal:

                bin_oct=0b1111101011001110
                print("The octal form of bin_oct : ",oct(bin_oct))
#### output:
            The octal form of hex_oct :  0o443

### hexadecimal to octal:

                hex_oct=0x123
                print("The octal form of hex_oct : ",oct(hex_oct))
#### output:
            The octal form of bin_oct :  0o175316


# float() -float datatypes:

- Float, or "floating point number" is a number, **positive or negative, containing one or more decimals**
- Float can be represented with **Exponential form/Scientific Notation** with an "e" to indicate the power of 10.
            
            4.5 - positive float value
            4.6 - Negative float value
            -4.e18 - Exponential form/Scientific Notation (i.e) -4 . * 10^18

NOTE: 
    **Float type variable always returns value with decimal point i.e(5.0)**
    **Float type doesn't support base conversion function it is applicable only for integer type**

### [float_type.py](https://github.com/pknviki95/Python/tree/main/concepts/Datatypes/Number_datatypes/float/scripts/float_type.py) - Program-1 : To find the float type variable using type() function:

            x=11.5 
            print("X value is:",x)   
            print("The type of x is: ",type(x))
#### output:
            X value is: 11.5
            The type of x is:  <class 'float'>

### Program-2 : To find the exponential float type variable using type() function:

            y=4.e5
            print("Y value is:",y)   
            print("The type of y is: ",type(y))
#### output:
            Y value is: 400000.0
            The type of y is:  <class 'float'>

# complex() -complex datatypes:

- complex type is a number combination of  **real and imaginary part**
- complex can be represented with **real+imagj (i.e) 10+12j**
- Complex datatypes are mostly used in **mathematical operations,complex calculation etc.**

            complex_variable = real_variable+[imaginary_variable]j

#### NOTE:
- **imaginary part should always be j/J; if used anyother alphabet it throws error**

### [complex_img_j_error.py](https://github.com/pknviki95/Python/tree/main/concepts/Datatypes/Number_datatypes/complex/scripts/complex_img_j_error.py) - imaginary part should always be j/J if not it throws error - Syntax error:

            # if used anyother alphabet used in imaginary part it throws error

            x=11+12i
            print("X value is:",x)
#### error:
         File "/home/pknviki95/Learning/Python/concepts/Datatypes/Number_datatypes/complex/scripts/complex_img_j_error.py", line 1
            x=11+12i 
                  ^
         SyntaxError: invalid decimal literal

### [complex_type.py](https://github.com/pknviki95/Python/tree/main/concepts/Datatypes/Number_datatypes/complex/scripts/complex_type.py) - Program-1 : To find the complex type variable using type() function:

            x=11+12j 
            print("X value is:",x)   
            print("The type of x is: ",type(x))
#### output:
         X value is: (11+12j)
         The type of x is:  <class 'complex'>

### Program-2 : To display the real and imaginary part individually:

            x=11+12j 
            print("X real value is:",x.real)   
            print("X imaginary value is:",x.imag)
#### output:
         X real value is: 11.0
         X imaginary value is: 12.0

### [complex_arithmetic.py](https://github.com/pknviki95/Python/tree/main/concepts/Datatypes/Number_datatypes/complex/scripts/complex_arithmetic.py) - To perform arithmetic operation for complex numbers:

### Addition

            x=11+12j
            y=20+40j
            z=x+y 
            print("X+Y value is:",z)
#### output:
         X+Y value is: (31+52j)

### Multiplication

            x=11+12j
            y=20+40j
            z=x*y 
            print("X*Y value is:",z) 
#### output:
         X*Y value is: (-260+680j)

### Division

            x=11+12j
            y=20+40j
            z=x/y 
            print("X/Y value is:",z)
#### output:         
         X/Y value is: (0.35-0.1j)
## Limitation of complex number declaration:

- The real value of complex number can be a **decimal value,float value,octal,hexadecimal,binary values**
- **The imaginary value for complex number should be only decimal value if it is declared with other base values it throws syntax error**

| Example | description | Allowance |
| :---:   | :---: | :---: |
| **x=10+20j** | **decimal values on both real and imag** | **Allowed** |
| **x=10.5+20.5j** | **float values on both real and imag** |**Allowed** |
| **x=0x123+20j** | **hex values 0n real and decimal value on imaginary (same applies for other bases)**| **Allowed** |
| **x=20+0x123j** | **decimal value on real and hex value on imag** |**Not Allowed** |

### [complex_limitation.py](https://github.com/pknviki95/Python/tree/main/concepts/Datatypes/Number_datatypes/complex/scripts/complex_limitation.py) - if updated with imaginary other base values(oct,hex,bin) - Syntax error :

### binary value:

            x=20+0b1111101011001110j 
            print("X real value is:",x.real)   
            print("X imaginary value is:",x.imag)

### octal value:

            x=20+0o123j 
            print("X real value is:",x.real)   
            print("X imaginary value is:",x.imag)

### hexadecimal value:

            x=20+0x123j 
            print("X real value is:",x.real)   
            print("X imaginary value is:",x.imag)

#### error:

         File "/home/pknviki95/Learning/Python/concepts/Datatypes/Number_datatypes/complex/scripts/complex_limitation.py", line 10
            x=20+0b1111101011001110j 
                                 ^
         SyntaxError: invalid binary literal

 


 

 

  




