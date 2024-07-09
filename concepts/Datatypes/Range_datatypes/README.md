# range() - Range datatypes:

- Range Datatype is **Sequence of numbers (i.e) number in range** 
- Range can be accessed using **index value (i.e) Indexing/Slicing is possible** 

        range_variable=range(number)

            # number - sequence of number from 0 to n-1

- Range can be accessed based on **specific range values - Slicing**.
        
        range_variable=range(begin number,end number,step)

            # begin number - sequence of number to start
            # end number - sequence of number to end end=n-1
            # step - sequence of number in specific steps

### [range_type.py](https://github.com/pknviki95/Python/tree/main/concepts/Datatypes/Range_datatypes/scripts/range_type.py) - To find the range variable using type() function:

                range_variable=range(10)
                print("The type of range_variable : ",type(range_variable))

#### output:

                The type of range_variable :  <class 'range'>

## Indexing:

- **Elements of range can be accessed using indexing/slicing as range is ordered preserved**

### [range_indexing.py](https://github.com/pknviki95/Python/tree/main/concepts/Datatypes/Range_datatypes/scripts/range_indexing.py) - To find the index value of the range based on positive and negative index

                range_variable[index]

### Positive Index:

                sequence = range(4)

                print('sequence[0]',sequence[0])
                print('sequence[1]',sequence[1])
                print('sequence[2]',sequence[2])
                print('sequence[3]',sequence[3])
#### output:

                sequence[0] 0
                sequence[1] 1
                sequence[2] 2
                sequence[3] 3

### Negative Index:

                sequence = range(4)

                print('sequence[-1]',sequence[-1])
                print('sequence[-2]',sequence[-2])
                print('sequence[-3]',sequence[-3])
                print('sequence[-4]',sequence[-4])

#### output:

                sequence[-1] 3
                sequence[-2] 2
                sequence[-3] 1
                sequence[-4] 0

## Slicing:

- **Sequence of range elements can be accessed using slicing**

                range_variable[start index, end index, step]

                    # start index - By default it is 0 ; This can be changes based on requirement
                    # end index - Last index value len(variable)-1
                    # step  - Sequence of number in specific index steps

### [range_slicing.py](https://github.com/pknviki95/Python/tree/main/concepts/Datatypes/Range_datatypes/scripts/range_slicing.py) - To find the index value of the range based on positive and negative index using slicing operation:

### Positive Index slicing:

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

#### output:
                Positive variable[start index:end index]:  range(2, 6)
                Positive variable[:end index]:  range(0, 6)
                Positive variable[start index:]:  range(2, 10)
                Positive variable[:]:  range(0, 10)
                Positive variable[start index:end index:step]:  range(1, 6, 2)

### Negative Index slicing:

                sequence = range(10)

                #variable[start index:end index] - Here the start index/end index is equivalent negative index value of positive index
                print('Negative variable[start index:end index]: ',sequence[-6:-2])  

                #variable[:end index] - By default start index is index 0 equivalent negative index
                print('Negative variable[:end index]: ',sequence[:-3])         

                #variable[start index:] - Here the start index is equivalent negative index value of positive index
                print('Negative variable[start index:]: ',sequence[-7:])        

                #variable[start index:end index:step] - It returns from index 1->3->5 (start+3(step) till end index value)
                print('Negative variable[start index:end index:step]: ',sequence[-7:-2:3])

#### output:
                Negative variable[start index:end index]:  range(4, 8)
                Negative variable[:end index]:  range(0, 7)
                Negative variable[start index:]:  range(3, 10)
                Negative variable[start index:end index:step]:  range(3, 8, 3)

- Range Datatype is **immutable (i.e) Its values cannot be Updated or changed** 

### [range_type_error.py](https://github.com/pknviki95/Python/tree/main/concepts/Datatypes/Range_datatypes/scripts/range_type_error.py) - range values cannot be changed as it is immutable if tried to change it throws error - Type error:


                sequence = range(4)

                # Assigning value to range variable - Type error
                sequence[0]=10 

                print('sequence[0]',sequence[0])

#### error:

                Traceback (most recent call last):
                File "/home/pknviki95/Learning/Python/concepts/Datatypes/Range_datatypes/scripts/range_type_error.py", line 9, in <module>
                    sequence[0]=10 
                TypeError: 'range' object does not support item assignment