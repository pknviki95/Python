# list() - List datatypes:

- **List is data type in python that can store values separated by ',' and enclosed within '[]'.**

            List_variable=[element 1,element 2,...]

- List variable can contain **duplicate elements with ordered preserved elements**
- **Heterogeneous objects are allowed in list (i.e) it can hold int,str,list,dict,etc., elements within its collection enclosed in square bracket.**
- List is **Mutable object**

### [list_type.py](https://github.com/pknviki95/Python/tree/main/concepts/Datatypes/List_datatypes/scripts/list_type.py) - To find the list type variable using type() function:

                list_variable =[1,'viki',[2,3],1]
                print("The type of list_variable is: ",type(list_variable))
#### output:
                The type of list_variable is:  <class 'list'>

## Indexing:

- **Elements of list can be accessed using indexing/slicing as list is ordered preserved**

| **List**  |  **1**   |  **viki** | **[2,3]** | **1** |
| :---:   | :---: | :---: | :---: | :---: |
| **Positive Index**  |  **0**   |  **1** | **2** | **3** |
| **Negative Index**  |  **-4**   |  -**3** | **-2** | **-1** |

### [list_indexing.py](https://github.com/pknviki95/Python/tree/main/concepts/Datatypes/List_datatypes/scripts/list_indexing.py) - To find the index value of the list based on positive and negative index

### Positive Index

            sequence = [1,'viki',[2,3],1]

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

            sequence = [1,'viki',[2,3],1]

            print('sequence[-1]',sequence[-1])
            print('sequence[-2]',sequence[-2])
            print('sequence[-3]',sequence[-3])

#### output:
            sequence[-1] 1
            sequence[-2] [2, 3]
            sequence[-3] viki

## Slicing:

- **Sequence of list elements can be accessed using slicing**

### [list_slicing.py](https://github.com/pknviki95/Python/tree/main/concepts/Datatypes/List_datatypes/scripts/list_slicing.py) - To obtain elements from list based on positive and negative index:

### Positive Index slicing:

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

#### output:
            Positive variable[start index:end index]:  [[2, 3], 1, {1: 'viki'}, (1, 3)]
            Positive variable[:end index]:  [1, 'viki', [2, 3], 1, {1: 'viki'}, (1, 3)]
            Positive variable[start index:]:  [[2, 3], 1, {1: 'viki'}, (1, 3)]
            Positive variable[:]:  [1, 'viki', [2, 3], 1, {1: 'viki'}, (1, 3)]
            Positive variable[start index:end index:step]:  ['viki', 1, (1, 3)]

### Negative Index slicing:

                sequence = [1,'viki',[2,3],1,{1:'viki'},(1,3)]
                
                #variable[start index:end index] - Here the start index/end index is equivalent negative index value of positive index
                print('Negative variable[start index:end index]: ',sequence[-6:-2])  

                #variable[:end index] - By default start index is index 0 equivalent negative index
                print('Negative variable[:end index]: ',sequence[:-3])         

                #variable[start index:] - Here the start index is equivalent negative index value of positive index
                print('Negative variable[start index:]: ',sequence[-7:])        

                #variable[start index:end index:step] - It returns from index 1->3->5 (start+3(step) till end index value)
                print('Negative variable[start index:end index:step]: ',sequence[-7:-2:3])
#### output:

            Negative variable[start index:end index]:  [1, 'viki', [2, 3], 1]
            Negative variable[:end index]:  [1, 'viki', [2, 3]]
            Negative variable[start index:]:  [1, 'viki', [2, 3], 1, {1: 'viki'}, (1, 3)]
            Negative variable[start index:end index:step]:  [1, 1]