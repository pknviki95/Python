# tuple() - Tuple datatypes:

- **Tuple is data type in python that can store values separated by ',' and enclosed within '()'.**

            tuple_variable=(element 1,element 2,...)

- Tuple is **read-only object version of list**
- Tuple variable can contain **duplicate elements with ordered preserved elements**
- **Heterogeneous objects are allowed in tuple (i.e) it can hold int,str,list,dict,etc., elements within its collection enclosed in () bracket.**
- Tuple is **immutable object - (i.e) Values of tuple object cannot be changed**

### [tuple_type.py](https://github.com/pknviki95/Python/tree/main/concepts/Datatypes/Tuple_datatypes/scripts/tuple_type.py) - To find the tuple variable using type() function:

                tuple_variable =(1,'viki',[2,3],1)
                print("The type of tuple_variable is: ",type(tuple_variable))
#### output:
                The type of tuple_variable is:  <class 'tuple'>

## Indexing:

- **Elements of tuple can be accessed using indexing/slicing as tuple is ordered preserved by it is only read-only changes to tuple object is not available as it is immutable**

| **tuple**  |  **1**   |  **viki** | **[2,3]** | **1** |
| :---:   | :---: | :---: | :---: | :---: |
| **Positive Index**  |  **0**   |  **1** | **2** | **3** |
| **Negative Index**  |  **-4**   |  -**3** | **-2** | **-1** |

### [tuple_indexing.py](https://github.com/pknviki95/Python/tree/main/concepts/Datatypes/Tuple_datatypes/scripts/tuple_indexing.py) - To find the index value of the tuple based on positive and negative index

### Positive Index

            sequence = (1,'viki',[2,3],1)

            print('sequence[0]',sequence[0])
            print('sequence[1]',sequence[1])
            print('sequence[2]',sequence[2])
            print('sequence[3]',sequence[3])
#### output:
            sequence[0] 1
            sequence[1] viki
            sequence[2] [2, 3]
            sequence[3] 1

### Negative Index

            sequence = (1,'viki',[2,3],1)

            print('sequence[-1]',sequence[-1])
            print('sequence[-2]',sequence[-2])
            print('sequence[-3]',sequence[-3])

#### output:
            sequence[-1] 1
            sequence[-2] [2, 3]
            sequence[-3] viki

## Slicing:

- **Sequence of tuple elements can be accessed using slicing**

### [tuple_slicing.py](https://github.com/pknviki95/Python/tree/main/concepts/Datatypes/Tuple_datatypes/scripts/tuple_slicing.py) - To obtain elements from tuple based on positive and negative index:

### Positive Index slicing:

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

#### output:
                Positive variable[start index:end index]:  ([2, 3], 1, {1: 'viki'}, (1, 3))
                Positive variable[:end index]:  (1, 'viki', [2, 3], 1, {1: 'viki'}, (1, 3))
                Positive variable[start index:]:  ([2, 3], 1, {1: 'viki'}, (1, 3))
                Positive variable[:]:  (1, 'viki', [2, 3], 1, {1: 'viki'}, (1, 3))
                Positive variable[start index:end index:step]:  ('viki', 1, (1, 3))

### Negative Index slicing:

                sequence = (1,'viki',[2,3],1,{1:'viki'},(1,3))

                #variable[start index:end index] - Here the start index/end index is equivalent negative index value of positive index
                print('Negative variable[start index:end index]: ',sequence[-6:-2])  

                #variable[:end index] - By default start index is index 0 equivalent negative index
                print('Negative variable[:end index]: ',sequence[:-3])         

                #variable[start index:] - Here the start index is equivalent negative index value of positive index
                print('Negative variable[start index:]: ',sequence[-7:])        

                #variable[start index:end index:step] - It returns from index 1->3->5 (start+3(step) till end index value)
                print('Negative variable[start index:end index:step]: ',sequence[-7:-2:3])
#### output:

                Negative variable[start index:end index]:  (1, 'viki', [2, 3], 1)
                Negative variable[:end index]:  (1, 'viki', [2, 3])
                Negative variable[start index:]:  (1, 'viki', [2, 3], 1, {1: 'viki'}, (1, 3))
                Negative variable[start index:end index:step]:  (1, 1)

- **Tuple is read-only immutable object is any changes are tried to made using attribute like list it throws error - Attribute error**
- **Based on below dir() function tuple doesn't have any write related operation only read related operations.**
- **If any attributes used apart from available one it throws attribute error**

### [tuple_attribute_error.py](https://github.com/pknviki95/Python/tree/main/concepts/Datatypes/Tuple_datatypes/scripts/tuple_attribute_error.py) - tuple is read-only immutable object is any changes are tried to made using attribute like list it throws error - Attribute error:

                tuple_variable=(1,2,3,4,'viki')


                # Attribute error:
                # If any attributes used apart from available one it throws attribute error
                print(dir(tuple_variable))
                tuple_variable.append(2)

#### dir() output:
                ['__add__', '__class__', '__class_getitem__', '__contains__', '__delattr__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getitem__', '__getnewargs__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__iter__', '__le__', '__len__', '__lt__', '__mul__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__rmul__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', 'count', 'index']
#### error:

                Traceback (most recent call last):
                File "/home/pknviki95/Learning/Python/concepts/Datatypes/Tuple_datatypes/scripts/tuple_attribute_error.py", line 13, in <module>
                    tuple_variable.append(2)
                AttributeError: 'tuple' object has no attribute 'append'

## Limititaions: 

### 1: Single valued tuple should ends with "," comma:

- By default all the single values of object is considered as single tuple object by Python virtual machine
- (i.e) consider assigning a integer value 10 

            x=10 is equivaluent to x=(10)
- Due to this above scenario all the single object elements inside tuple is considered to its equivalent datatypes
- To overcome come this scenario we need to tell the PVM that it is tuple varibale/object by adding , after single tuple element

            x=(10,)

### [tuple_limitation.py](https://github.com/pknviki95/Python/tree/main/concepts/Datatypes/Tuple_datatypes/scripts/tuple_limitation.py) - Single value declaration with comma(",") to overcome above limitation:

### multiple value declaration:

                tuple_multiple_variable =(1,2,'viki',[1,2])
                print("The type of tuple_multiple_variable is: ",type(tuple_multiple_variable))

#### output:
                The type of tuple_multiple_variable is:  <class 'tuple'>
### Single value declaration:

                tuple_single_variable_int =(1)
                print("The type of tuple_single_variable_int is: ",type(tuple_single_variable_int))

                tuple_single_variable_str =('viki')
                print("The type of tuple_single_variable_str is: ",type(tuple_single_variable_str))

                tuple_single_variable_list =([1,2])
                print("The type of tuple_single_variable_list is: ",type(tuple_single_variable_list))

                tuple_single_variable_bool =(True)
                print("The type of tuple_single_variable_bool is: ",type(tuple_single_variable_bool))
#### output:
                The type of tuple_single_variable_int is:  <class 'int'>
                The type of tuple_single_variable_str is:  <class 'str'>
                The type of tuple_single_variable_list is:  <class 'list'>
                The type of tuple_single_variable_bool is:  <class 'bool'>
### Single value declaration with comma(",") to overcome above limitation:

                tuple_single_variable_int =(1,)
                print("The type of tuple_single_variable_int with , is: ",type(tuple_single_variable_int))

                tuple_single_variable_str =('viki',)
                print("The type of tuple_single_variable_str with , is: ",type(tuple_single_variable_str))

                tuple_single_variable_list =([1,2],)
                print("The type of tuple_single_variable_list with , is: ",type(tuple_single_variable_list))

                tuple_single_variable_bool =(True,)
                print("The type of tuple_single_variable_bool with , is: ",type(tuple_single_variable_bool))

#### output:

                The type of tuple_single_variable_int with , is:  <class 'tuple'>
                The type of tuple_single_variable_str with , is:  <class 'tuple'>
                The type of tuple_single_variable_list with , is:  <class 'tuple'>
                The type of tuple_single_variable_bool with , is:  <class 'tuple'>

- **Declaration with comma(",") to overcome above limitation saying PVM to consider this single value as tuple element**