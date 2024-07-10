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

## Number Datatypes: 

- Python supports the below standard data types: 

### Various types of Numbers Datatypes:

### Integer- int () 
    
- Integers – No limit to the value of integers
- By default Python takes integer as decimal value
                
            1,1234
### float- float ()

- floating point values in **scientific or exponential form**

            4.5,-4.6,-4+e18

### complex - complex ()

- complex numbers with real and imaginary numbers
            
            3+4j

|Number types | Example program   | output    |
| :---:   | :---: | :---: |
| **integer**  |  x=11 <br>  print("X value is:",x) <br>   print(type(x))   |  X value is: 11 <br> <class 'int'> |
| **float**    |  y=4.5  <br> print("Y value is:",y)  <br> print(type(y))   |   Y value is: 4.5 <br> <class 'float'> |
| **complex**  |     z=3+5j <br> print("Z value is:",z)  <br>print(type(z))               |   Z value is: (3+5j) <br> <class 'complex'>         |

## Boolean Datatypes:

- bool() is to **determine the given value is True or False**
- It can be determined **if the given input exists , condition is valid or etc.,**

            True,False

| Boolean type | value    | Example program   | output    |Description  |
| :---:   | :---: | :---: | :---: | :---: |
| **True** | 1   | x=True <br>  print("X value is:",x) <br>   print(type(x))   |  X value is: True <br> <class 'bool'> |By default the value is 1 - True valid declaration |
| **False**| 0    | x=False <br>  print("X value is:",x) <br>   print(type(x))   |  X value is: False <br> <class 'bool'>|By default the value is 0 - False valid declaration|

## String Datatypes:

- str() datatype is used to represent the **string variables**
- In python we don't have concept of **char/character** like in c.It will consider all inside quotes as **string**.

            'viki',"siva", '''raja'''

| String types | Example program   | output    |
| :---:   |  :---: | :---: |
| **String with single quotes** | x='viki' <br>  print("X value is:",x) <br>   print(type(x))   |  X value is: viki <br> <class 'str'> |
| **String with Double quotes** | x="viki" <br>  print("X value is:",x) <br>   print(type(x))   |  X value is: viki <br> <class 'str'> |
| **String with Triple quotes** | x='''viki''' <br>  print("X value is:",x) <br>   print(type(x))   |  X value is: viki <br> <class 'str'> |

## Differences between Datatypes based on its characteristics:

| **Datatypes**  |  **Ordered**   |  **Un-ordered** | **Mutable** | **Immutable** | **Duplicates** | **Indexing/Slicing** |
| :---:   | :---: | :---: | :---: | :---: | :---: | :---: | 
| **Integer**  |  :x:  |  :heavy_check_mark: | :x: | :heavy_check_mark: | :x: | :x: |
| **Float**  |  :x:  |  :heavy_check_mark: | :x: | :heavy_check_mark: | :x: | :x: |
| **complex**  |  :x:  |  :heavy_check_mark: | :x: | :heavy_check_mark: | :x: | :x: |
| **boolean**  |  :x:  |  :heavy_check_mark: | :x: | :heavy_check_mark: | :x: | :x: |
| **string**  |  :x:  |  :x: | :x: | :heavy_check_mark: | :x: | :heavy_check_mark:
| **list**  |  :heavy_check_mark:  |  :x: | :heavy_check_mark: | :x: | :heavy_check_mark: |:heavy_check_mark: |
| **tuple**  |  :heavy_check_mark:  |  :x: | :x: | :heavy_check_mark: | :heavy_check_mark: |:heavy_check_mark: |
| **set**    | :x:  |  :heavy_check_mark: | :heavy_check_mark: | :x: | :x: | :x: |
| **frozenset**  | :x:  |  :heavy_check_mark: | :x: | :heavy_check_mark: | :x: | :x: |
| **dictionary**  |  :x: |  :heavy_check_mark:  | :heavy_check_mark: | :x: | :heavy_check_mark: for values ; :x: for key| :x: |
| **range**  |  :heavy_check_mark:  |  :x: | :x: | :heavy_check_mark: | :x: | :heavy_check_mark: |
| **bytes**  |  :heavy_check_mark:  |  :x: | :x: | :heavy_check_mark: | :heavy_check_mark: |:heavy_check_mark: |
| **Byte array**  |  :heavy_check_mark:  |  :x: | :heavy_check_mark: | :x: | :heavy_check_mark: |:heavy_check_mark: |
