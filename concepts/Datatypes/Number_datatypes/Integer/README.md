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
| **Hexadecimal form (base-16)** | 0-9 and A-F   | The Hexa decimal form has  **0x/0X** as a prefix | 

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

### decimal to binary:
### [bin_base_conversion.py](https://github.com/pknviki95/Python/tree/main/concepts/Datatypes/Number_datatypes/Integer/scripts/bin_base_conversion.py) - To convert decimal form to binary form using bin() function:

                    dec_bin=53
                    print("The binary form of dec_bin : ",bin(dec_bin))
#### output:
            The binary form of dec_bin :  0b110101

### octal to binary:
### [bin_base_conversion.py](https://github.com/pknviki95/Python/tree/main/concepts/Datatypes/Number_datatypes/Integer/scripts/bin_base_conversion.py) - To convert octal form to binary form using bin() function:

                oct_bin=0o123
                print("The binary form of oct_bin : ",bin(oct_bin))
#### output:
            The binary form of oct_bin :  0b1010011

### hexadecimal to binary:
### [bin_base_conversion.py](https://github.com/pknviki95/Python/tree/main/concepts/Datatypes/Number_datatypes/Integer/scripts/bin_base_conversion.py) - To convert hexadecimal form to binary form using bin() function:

                hex_bin=0xface
                print("The binary form of hex_bin : ",bin(hex_bin))
#### output:
            The binary form of hex_bin :  0b1111101011001110
## hex():

- To convert other functions to **hexadecimal form (base-16)**

### decimal to hexadecimal:

### [hex_base_conversion.py](https://github.com/pknviki95/Python/tree/main/concepts/Datatypes/Number_datatypes/Integer/scripts/hex_base_conversion.py) -  To convert decimal form to hexadecimal form using hex() function:

                dec_hex=123
                print("The Hexadecimal form of dec_hex : ",hex(dec_hex))

#### output:
            The Hexadecimal form of dec_hex :  0x7b

### octal to hexadecimal:

### [hex_base_conversion.py](https://github.com/pknviki95/Python/tree/main/concepts/Datatypes/Number_datatypes/Integer/scripts/hex_base_conversion.py) -  To convert octal form to hexadecimal form using hex() function:

                oct_hex=0o123
                print("The Hexadecimal form of oct_hex : ",hex(oct_hex))
#### output:
            The Hexadecimal form of oct_hex :  0x53

### binary to hexadecimal:

### [hex_base_conversion.py](https://github.com/pknviki95/Python/tree/main/concepts/Datatypes/Number_datatypes/Integer/scripts/hex_base_conversion.py) -  To convert binary form to hexadecimal form using hex() function:

                bin_hex=0b1111101011001110
                print("The Hexadecimal form of bin_hex : ",hex(bin_hex))
#### output:
            The Hexadecimal form of bin_hex :  0xface

## oct(): 

- To convert other functions to **octal form (base-8)**

### decimal to octal:

### [oct_base_conversion.py](https://github.com/pknviki95/Python/tree/main/concepts/Datatypes/Number_datatypes/Integer/scripts/oct_base_conversion.py) -  To convert decimal form to octal form using oct() function:

                dec_oct=123
                print("The octal form of dec_oct : ",oct(dec_oct))
#### output:
            The octal form of dec_oct :  0o173

### binary to octal:

### [oct_base_conversion.py](https://github.com/pknviki95/Python/tree/main/concepts/Datatypes/Number_datatypes/Integer/scripts/oct_base_conversion.py) -  To convert binary form to octal form using oct() function:

                bin_oct=0b1111101011001110
                print("The octal form of bin_oct : ",oct(bin_oct))
#### output:
            The octal form of hex_oct :  0o443

### hexadecimal to octal:

### [oct_base_conversion.py](https://github.com/pknviki95/Python/tree/main/concepts/Datatypes/Number_datatypes/Integer/scripts/oct_base_conversion.py) -  To convert hexadecimal form to octal form using oct() function:

                hex_oct=0x123
                print("The octal form of hex_oct : ",oct(hex_oct))
#### output:
            The octal form of bin_oct :  0o175316

 

 


 

 

  




