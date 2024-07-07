# bytes() - Bytes Datatypes:

## bytes():

- Python bytes are a **sequence of integers in the range of 0-255**. 
- Bytes are an **immutable sequence data type**, meaning once a bytes object is created, it cannot be changed.
- **They are ordered sequence (i.e) Indexing and slicing operation are possible.**

                list_variable=[element_1,eement_2,...]
                bytes_variable=bytes(list_variable)


### [bytes_type.py](https://github.com/pknviki95/Python/tree/main/concepts/Datatypes/Bytes_datatypes/scripts/bytes_type.py) - To find the bytes type variable using type() function:

                # sequence of numbers range from 0-255

                list_variable=[1,2,3,65,66]

                # bytes() for using bytes objects
                bytes_variable=bytes(list_variable)

                print("bytes_variable: ",bytes_variable)
                print("The type of bytes_variable : ",type(bytes_variable))

#### output:

                bytes_variable:  b'\x01\x02\x03AB'
                The type of bytes_variable :  <class 'bytes'>

## Indexing:

- **Elements of bytes can be accessed using indexing/slicing as bytes is ordered preserved**

### [bytes_indexing.py](https://github.com/pknviki95/Python/tree/main/concepts/Datatypes/Bytes_datatypes/scripts/bytes_indexing.py) - To find the index value of the bytes based on positive and negative index:

### Positive Index

                sequence = [65,66,67,68]
                bytes_variable=bytes(sequence)

                print(bytes_variable)

                print('bytes_variable[0]',bytes_variable[0])
                print('bytes_variable[1]',bytes_variable[1])
                print('bytes_variable[2]',bytes_variable[2])
                print('bytes_variable[3]',bytes_variable[3])
#### output:
                b'ABCD'
                bytes_variable[0] 65
                bytes_variable[1] 66
                bytes_variable[2] 67
                bytes_variable[3] 68
### Negative Index

                sequence = [65,66,67,68]
                bytes_variable=bytes(sequence)

                print('bytes_variable[-1]',bytes_variable[-1])
                print('bytes_variable[-2]',bytes_variable[-2])
                print('bytes_variable[-3]',bytes_variable[-3])
                print('bytes_variable[-4]',bytes_variable[-4])
#### output:

                bytes_variable[-1] 68
                bytes_variable[-2] 67
                bytes_variable[-3] 66
                bytes_variable[-4] 65

## Slicing:

- **Sequence of bytes elements can be accessed using slicing**

### [bytes_slicing.py](https://github.com/pknviki95/Python/tree/main/concepts/Datatypes/Bytes_datatypes/scripts/bytes_slicing.py) - To access the sequence of bytes based on positive and negative index usig slicing operation:

### Positive Index slicing

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
#### output:
                Positive variable[start index:end index]:  b'CDE\x01'
                Positive variable[:end index]:  b'ABCDE\x01'
                Positive variable[start index:]:  b'CDE\x01\x02\x03'
                Positive variable[:]:  b'ABCDE\x01\x02\x03'
                Positive variable[start index:end index:step]:  b'BD\x01'

### Negative Index slicing

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
#### output:

                Negative variable[start index:end index]:  b'CDE\x01'
                Negative variable[:end index]:  b'ABCDE'
                Negative variable[start index:]:  b'BCDE\x01\x02\x03'
                Negative variable[start index:end index:step]:  b'BE'

### [bytes_256_value_error.py](https://github.com/pknviki95/Python/tree/main/concepts/Datatypes/Bytes_datatypes/scripts/bytes_256_value_error.py) - Bytes type support sequence of elements from range 0-255 if it exceeds it throws error - Value error:

                # sequence of numbers exceeds range from 0-255 - value error

                list_variable=[1,2,3,65,66,256]

                # bytes() for using bytes objects
                bytes_variable=bytes(list_variable)

                print("bytes_variable: ",bytes_variable)

#### error:
                Traceback (most recent call last):
                File "/home/pknviki95/Learning/Python/concepts/Datatypes/Bytes_datatypes/scripts/bytes_256_value_error.py", line 12, in <module>
                    bytes_variable=bytes(list_variable)
                ValueError: bytes must be in range(0, 256)

### [bytes_type_error.py](https://github.com/pknviki95/Python/tree/main/concepts/Datatypes/Bytes_datatypes/scripts/bytes_type_error.py) - Bytes type cannot be updaed or changed as it is immutable if done it throws error- Type error :

                sequence = [65,66,67,68]
                bytes_variable=bytes(sequence)

                # Assigning value to bytes variable throws Type error
                bytes_variable[2]=60
                print(bytes_variable)

#### error:

                Traceback (most recent call last):
                File "/home/pknviki95/Learning/Python/concepts/Datatypes/Bytes_datatypes/scripts/bytes_type_error.py", line 10, in <module>
                    bytes_variable[2]=60
                TypeError: 'bytes' object does not support item assignment

### NOTE: Above Type error is neglected by using the bytearray() datatype as it is Mutable object - [Bytearray_datatypes](https://github.com/pknviki95/Python/tree/main/concepts/Datatypes/Bytearray_datatypes)


