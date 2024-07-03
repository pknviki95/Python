# int() - Integer datatypes

- Integers – No limit to the value of integers
- By default Python takes integer as decimal value
                
            1,1234

### Program: To find the integer type variable using type() function:

            x=11 
            print("X value is:",x)   
            print("The type of x is: ",type(x))

## Different types of integer Numbers forms:
 
| Integer type | value    | Description  |
| :---:   | :---: | :---: |
| **Decimal form (base-10)** | 0-9   | By default all the number are in decimal form (0-9) |
| **Binary form (base-2)** | 0 and 1   | The binary form has **0b/0B** as the prefix |
| **Octal form (base-8)** | 0-7   | The octal form has **0o/0O** as the prefix | 
| **Hexadecimal form (base-16)** | 0-9 and A-F   | The Hexa decimal form has  **0x/0X** as a prefix | 

## Various integral form to decimal conversion:

NOTE: By default Python takes all the integer value as ***decimal value***

| Integer type | value    | Conversion formula    | Final output|
| :---:   | :---: | :---: | :---: |
| **Binary to decimal** | A=0b1111   | (1111)<sub>2</sub> => (2<sup>3</sup>+2<sup>2</sup>+2<sup>1</sup>+2<sup>0</sup>) = (8 * 1 + 4 * 1 + 2 * 1 + 1 * 1)   | 15 |
| **Octal to decimal** | A=0o1234   | (1234)<sub>8</sub> => (8<sup>3</sup>+8<sup>2</sup>+8<sup>1</sup>+8<sup>0</sup>) = (512 * 1 + 64 * 2 + 8 * 3 + 1 * 4)   | 668 |
| **Hexadecimal to decimal** | A=0xFACE | (FACE)<sub>16</sub> => (16<sup>3</sup>+16<sup>2</sup>+16<sup>1</sup>+16<sup>0</sup>) = ( 4096 * 15 + 256 * 10 + 16 * 12 + 1 * 14 )| 64206 | 

## Base Conversion in-built function:

- The in-built base conversion helps to convert from one base to other base integer form
- These functions are applicable only for integer type
- Three types

    - **bin()**
    - **hex()**
    - **oct()**

## bin():

- To convert other functions to **binary form (base-2)**

### Program: To convert decimal form to binary form using bin() function:

#### decimal to binary:

                    dec_bin=53
                    print("The binary form of dec_bin : ",bin(dec_bin))

### Program: To convert octal form to binary form using bin() function:

#### octal to binary:

                oct_bin=0o123
                print("The binary form of oct_bin : ",bin(oct_bin))

### Program: To convert hexadecimal form to binary form using bin() function:

#### hexadecimal to binary:

                hex_bin=0xface
                print("The binary form of hex_bin : ",bin(hex_bin))

## hex():

- To convert other functions to **hexadecimal form (base-16)**

### Program: To convert decimal form to hexadecimal form using hex() function:

#### decimal to hexadecimal:

                dec_hex=123
                print("The Hexadecimal form of dec_hex : ",hex(dec_hex))

### Program: To convert octal form to hexadecimal form using hex() function:

#### octal to hexadecimal:

                oct_hex=0o123
                print("The Hexadecimal form of oct_hex : ",hex(oct_hex))

### Program: To convert binary form to hexadecimal form using hex() function:

#### binary to hexadecimal:

                bin_hex=0b1111101011001110
                print("The Hexadecimal form of bin_hex : ",hex(bin_hex))

## oct(): 

- To convert other functions to **octal form (base-8)**
 
### Program: To convert decimal form to octal form using oct() function:

#### decimal to octal:

                dec_oct=123
                print("The octal form of dec_oct : ",oct(dec_oct))

### Program: To convert binary form to octal form using oct() function:

#### binary to octal:

                bin_oct=0b1111101011001110
                print("The octal form of bin_oct : ",oct(bin_oct))

### Program: To convert hexadecimal form to octal form using oct() function:

#### hexadecimal to octal:

                hex_oct=0x123
                print("The octal form of hex_oct : ",oct(hex_oct))


 

 


 

 

  




