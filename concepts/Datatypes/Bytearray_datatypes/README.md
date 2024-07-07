# bytearray() -  ByteArray Datatypes:

- Python bytearray are a **sequence of integers in the range of 0-255**. it is similar to bytes 
- Bytearray are an **mutable sequence data type**, meaning once a bytes object is created, it can be changed.
- **(i.e) unlike bytes object the changes can be made on sequence using bytearray() object**
- **They are ordered sequence (i.e) Indexing and slicing operation are possible.**

                list_variable=[element_1,element_2,...]
                bytearrray_variable=bytearray(list_variable)

### [bytearray_type.py](https://github.com/pknviki95/Python/tree/main/concepts/Datatypes/Bytearray_datatypes/scripts/bytearray_type.py) - To find the bytearray type variable using type() function:

                # sequence of numbers range from 0-255

                list_variable=[1,2,3,65,66]

                # bytearray() for using bytearray objects
                bytearray_variable=bytearray(list_variable)

                print("bytearray_variable: ",bytearray_variable)
                print("The type of bytearray_variable : ",type(bytearray_variable))

#### output:

                bytearray_variable:  bytearray(b'\x01\x02\x03AB')
                The type of bytearray_variable :  <class 'bytearray'>

## Indexing:

- **Elements of bytes can be accessed using indexing/slicing as bytes is ordered preserved**

### [bytearray_indexing.py](https://github.com/pknviki95/Python/tree/main/concepts/Datatypes/Bytearray_datatypes/scripts/bytearray_indexing.py) - To find the index value of the bytearray based on positive and negative index:

### Positive Index

                sequence = [65,66,67,68]
                bytearray_variable=bytearray(sequence)

                print(bytearray_variable)

                print('bytearray_variable[0]',bytearray_variable[0])
                print('bytearray_variable[1]',bytearray_variable[1])
                print('bytearray_variable[2]',bytearray_variable[2])
                print('bytearray_variable[3]',bytearray_variable[3])
#### output:
                b'ABCD'
                bytes_variable[0] 65
                bytes_variable[1] 66
                bytes_variable[2] 67
                bytes_variable[3] 68
### Negative Index

                sequence = [65,66,67,68]
                bytearray_variable=bytearray(sequence)

                print('bytearray_variable[-1]',bytearray_variable[-1])
                print('bytearray_variable[-2]',bytearray_variable[-2])
                print('bytearray_variable[-3]',bytearray_variable[-3])
                print('bytearray_variable[-4]',bytearray_variable[-4])
#### output:

                bytes_variable[-1] 68
                bytes_variable[-2] 67
                bytes_variable[-3] 66
                bytes_variable[-4] 65

## Slicing:

- **Sequence of bytes elements can be accessed using slicing**

### [bytearray_slicing.py](https://github.com/pknviki95/Python/tree/main/concepts/Datatypes/Bytearray_datatypes/scripts/bytearray_slicing.py) - To access the sequence of bytes based on positive and negative index usig slicing operation:

### Positive Index slicing

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
#### output:
                Positive variable[start index:end index]:  bytearray(b'CDE\x01')
                Positive variable[:end index]:  bytearray(b'ABCDE\x01')
                Positive variable[start index:]:  bytearray(b'CDE\x01\x02\x03')
                Positive variable[:]:  bytearray(b'ABCDE\x01\x02\x03')
                Positive variable[start index:end index:step]:  bytearray(b'BD\x01')


### Negative Index slicing

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
#### output:

                Negative variable[start index:end index]:  bytearray(b'CDE\x01')
                Negative variable[:end index]:  bytearray(b'ABCDE')
                Negative variable[start index:]:  bytearray(b'BCDE\x01\x02\x03')
                Negative variable[start index:end index:step]:  bytearray(b'BE')

### [bytearray_256_value_error.py](https://github.com/pknviki95/Python/tree/main/concepts/Datatypes/Bytearray_datatypes/scripts/bytearray_256_value_error.py) - Bytearray type support sequence of elements from range 0-255 if it exceeds it throws error - Value error:

                # sequence of numbers exceeds range from 0-255 - value error

                list_variable=[1,2,3,65,66,256]

                # bytes() for using bytes objects
                bytearray_variable=bytearray(list_variable)

                print("bytearray_variable: ",bytearray_variable)

#### error:
                Traceback (most recent call last):
                File "/home/pknviki95/Learning/Python/concepts/Datatypes/Bytearray_datatypes/scripts/bytearray_256_value_error.py", line 12, in <module>
                    bytearray_variable=bytearray(list_variable)
                ValueError: byte must be in range(0, 256)

### [bytearray_assigning.py](https://github.com/pknviki95/Python/tree/main/concepts/Datatypes/Bytearray_datatypes/scripts/bytearray_assigning.py) - Bytearray type can be updaed or changed as it is mutable:

                sequence = [65,66,67,68]
                bytearray_variable=bytearray(sequence)
                print("bytearray_variable before assigning: ",bytearray_variable)

                # Assigning value to bytearray variable is possible as it is Mutable object
                bytearray_variable[2]=1
                print("bytearray_variable after assigning: ",bytearray_variable)

#### output:
                bytearray_variable before assigning:  bytearray(b'ABCD')
                bytearray_variable after assigning:  bytearray(b'AB\x01D')