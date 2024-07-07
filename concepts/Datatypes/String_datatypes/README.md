# str() - string datatypes

- str() datatype is used to represent the **string variables**
- In python we dont have concept of **char/character** like in c.It will consider all inside quotes as **string**.

            'viki',"siva", '''raja'''

## Various ways of representing strings:

- **Single Quotes(' ')**
- **Double Quotes(" ")**
- **Triple quotes(""" """)/(''' ''')**

## Limitation of string implementation:

### 1:Multi-line string literals:

- If the string are represented in singleline then it is considered as string datatypes in python
- If the string that needs to be implemented for multi-line then **Single Quotes(' ')** or **Double Quotes(" ")** is not possible it will throw Syntax error
- As to resolve this issue only **Triple quotes """ """/''' '''** is possible to assign multi-line string for any variable 
- (i.e) Triple-quotes are used to define multi-line string literals

### [str_limitation.py](https://github.com/pknviki95/Python/tree/main/concepts/Datatypes/String_datatypes/scripts/str_limitation.py) - String variable Limitaions for Multi-line string literals:

            #single/Double quotes:

            sentence = '- If the string
                        - If the string'

            # Triple quotes

            multi_line_sentence= '''- If the string                     
                                    - If the string'''

            print("single: ",sentence)
            print("multi_line_sentence: ",multi_line_sentence)

### error:

            pknviki95@pknviki95-Lenovo-ideapad-330:~/Learning/Python/concepts/Datatypes/String_datatypes/scripts$ py str_limitation.py 
            File "/home/pknviki95/Learning/Python/concepts/Datatypes/String_datatypes/scripts/str_limitation.py", line 13
                sentence = '- If the string
                        ^
            SyntaxError: unterminated string literal (detected at line 13)

### 2:Using various string quotes as special character:

- Using various **single/double quotes as special character** (i.e) usage of '' or "" inside a string can be done only by declaing the string variable in **triple quotes** or it will throw Syntax error

### [str_limitation.py](https://github.com/pknviki95/Python/tree/main/concepts/Datatypes/String_datatypes/scripts/str_limitation.py) - String variable Limitaions for using various single/double quotes as special character:

            #single quotes
            character= 'Hello all, Welcome to 'Learning''
            print(character)

            # Triple quotes to use Single/double quotes as special character 
            character= ''' Hello all, Welcome to 'Learning' '''
            print(character)
#### error:

            pknviki95@pknviki95-Lenovo-ideapad-330:~/Learning/Python/concepts/Datatypes/String_datatypes/scripts$ py str_limitation.py 
            File "/home/pknviki95/Learning/Python/concepts/Datatypes/String_datatypes/scripts/str_limitation.py", line 25
                character= 'Hello all, Welcome to 'Learning''
                                                ^^^^^^^^
            SyntaxError: invalid syntax

### [str_type.py](https://github.com/pknviki95/Python/tree/main/concepts/Datatypes/String_datatypes/scripts/str_type.py) - To find the string type variable using type() function:

            x='viki'                        #single quotes
            y="siva"                        #double quotes
            z="""karthi"""                  #triple quotes

            print("The type of single quotes x is: ",type(x))
            print("The type of double quotes y is: ",type(y))
            print("The type of triple quotes z is: ",type(z))
#### output:
            The type of single quotes x is:  <class 'str'>
            The type of double quotes y is:  <class 'str'>
            The type of triple quotes z is:  <class 'str'>

## Indexing:

- In Python, indexing refers to the **process of accessing a specific element in a sequence, such as a string or list, using its position or index number**.
- Indexing in Python starts at **0**, which means that the **first element in a sequence has an index of 0, the second element has an index of 1, and so on**. 

            variable[index number]

- **Indexing can be peroformed only with the total index present in the string;if we ask for return value that exceeds existing index range it throws Index error**

### [str_index_error.py](https://github.com/pknviki95/Python/tree/main/concepts/Datatypes/String_datatypes/scripts/str_index_error.py) - To understand the Indexing range of string - Index error:

            sequence = 'vignesh'

            # Index range exceeds the existing range 7 so it throws Index error 
            print('sequence[10]',sequence[10])  

#### error

            Traceback (most recent call last):
            File "/home/pknviki95/Learning/Python/concepts/Datatypes/String_datatypes/scripts/str_index_error.py", line 8, in <module>
                print('sequence[10]',sequence[10])
            IndexError: string index out of range

## Types of Index

### Positive Index:

- Positive Index starts from **first character of string** (i.e) 0 to n
- It consists of **positive index numbers** 
- It starts from **left to right (-->)**
- first index value of string always starts with **0**

### Negative Index:

- Positive Index starts from **last character of string** (i.e) -n to -1
- It consists of **Negative index numbers** 
- It starts from **right to left (<--)**
- first index value of string always starts with **-1**

| **String**  |  **v**   |  **i** | **k** | **i** |
| :---:   | :---: | :---: | :---: | :---: |
| **Positive Index**  |  **0**   |  **1** | **2** | **3** |
| **Negative Index**  |  **-4**   |  -**3** | **-2** | **-1** |

### [str_indexing.py](https://github.com/pknviki95/Python/tree/main/concepts/Datatypes/String_datatypes/scripts/str_indexing.py) - To find the index value of the string based on positive and negative index

### Positive Index

            sequence = 'vignesh'

            print('sequence[0]',sequence[0])
            print('sequence[1]',sequence[1])
            print('sequence[2]',sequence[2])
            print('sequence[3]',sequence[3])
            print('sequence[4]',sequence[4])
            print('sequence[5]',sequence[5])
            print('sequence[6]',sequence[6])
#### output:
            sequence[0] v
            sequence[1] i
            sequence[2] g
            sequence[3] n
            sequence[4] e
            sequence[5] s
            sequence[6] h

### Negative Index

            sequence = 'vignesh'

            print('sequence[-1]',sequence[-1])
            print('sequence[-2]',sequence[-2])
            print('sequence[-3]',sequence[-3])
            print('sequence[-4]',sequence[-4])
            print('sequence[-5]',sequence[-5])
            print('sequence[-6]',sequence[-6])
            print('sequence[-7]',sequence[-7])
#### output:
            sequence[-1] h
            sequence[-2] s
            sequence[-3] e
            sequence[-4] n
            sequence[-5] g
            sequence[-6] i
            sequence[-7] v

## String Slicing(Working with Index): 

- Slicing is used **to obtain sub-string from string by accessing index value of string**.

            variable[start index:end index:step] 

            start index : starting index-value of string 
            end index : ending index-value for string (i.e) len(str) 
            step : range of sub-string from string 


### [str_slicing.py](https://github.com/pknviki95/Python/tree/main/concepts/Datatypes/String_datatypes/scripts/str_slicing.py) - To obtain sub-string from string based on positive and negative index:

### Positive Index slicing

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
#### output:
            Positive variable[start index:end index]:  gnes
            Positive variable[:end index]:  vignes
            Positive variable[start index:]:  gnesh
            Positive variable[:]:  vignesh
            Positive variable[start index:end index:step]:  ins

### Negative Index slicing

            sequence = 'vignesh'

            #variable[start index:end index] - Here the start index/end index is equivalent negative index value of positive index
            print('Negative variable[start index:end index]: ',sequence[-6:-2])  

            #variable[:end index] - By default start index is index 0 equivalent negative index
            print('Negative variable[:end index]: ',sequence[:-3])         

            #variable[start index:] - Here the start index is equivalent negative index value of positive index
            print('Negative variable[start index:]: ',sequence[-7:])   

            #variable[start index:end index:step] - It returns from index 1->3->5 (start+3(step) till end index value)
            print('Negative variable[start index:end index:step]: ',sequence[-7:-2:3]) 
#### output:
            Negative variable[start index:end index]:  igne
            Negative variable[:end index]:  vign
            Negative variable[start index:]:  vignesh
            Negative variable[start index:end index:step]:  vn

## String Concatination:

- String concatination is the **process of concatinating(joining) between strings using (+) operator**
- (i.e) Basic rules for concatination is that argument that we use should be only between **strings**

            #string concatination
            str + str 

### [str_concantinate.py](https://github.com/pknviki95/Python/tree/main/concepts/Datatypes/String_datatypes/scripts/str_concantinate.py) -  concantinate two strings using + operator:

            string_1="Hello"
            string_2="Good Morning!"

            #String concatination

            final=string_1+'\t'+string_2                        #Hello+\t(tab space)+Good Morning!
            print("final_concantinated string: ",final)
#### output:
            final_concantinated string:  Hello      Good Morning!

- String concatination is applicable only if it is between string; if we are triying **concatination with string with other datatypes it throws Type error**

            #Type error
            str+int

### [str_concantinate_type_error.py](https://github.com/pknviki95/Python/tree/main/concepts/Datatypes/String_datatypes/scripts/str_concantinate_type_error.py) - concantinate strings with other datatype using + operator - Type error:

            string_1="Hello"
            int_2=10

            #String concatination with other datatype

            final=string_1+'\t'+int_2                   #Type error

            print("final_concantinated string with other datatype : ",final)
#### error:

            Traceback (most recent call last):
            File "/home/pknviki95/Learning/Python/concepts/Datatypes/String_datatypes/scripts/str_cat_type_error.py", line 16, in <module>
                final=string_1+'\t'+int_2                   #Type error
            TypeError: can only concatenate str (not "int") to str

## String repetating:

- String repetating is the **process of repeating conconcatination(joining) of string using (*) operator**
- (i.e) Basic rule is one argument should be **by default string and the other integer type for number to perform repetative**
- The order of usage can be random; it is also possible but make sure it satisfies basic rule of 1 str and 1 int **(i.e) [Number of repeatative] * str also possible**
            
            #string repetating
            str * [Number of repeatative]
             
### [str_repetative.py](https://github.com/pknviki95/Python/tree/main/concepts/Datatypes/String_datatypes/scripts/str_repetative.py) - concantinate string repetatively using * operator:

            string="viki"
            repetative_count=4
            print("string repetative: {}".format(string*repetative_count))              #str * [Number of repeatative]
#### output:
            string repetative: vikivikivikiviki

- **If the basic rule is not followed and if both are repetative with str type then it throws type error**
            
            #type error
            str * str

### [str_repetative_type_error.py](https://github.com/pknviki95/Python/tree/main/concepts/Datatypes/String_datatypes/scripts/str_repetative_type_error.py) -  concantinate two strings using * repetative operator - Type error:

            string_1="Hello"
            string_2="Good Morning!"

            final=string_1*string_2                    #Hello*Good Morning! 
            print("final_concantinated string: ",final)
#### error:

            Traceback (most recent call last):
            File "/home/pknviki95/Learning/Python/concepts/Datatypes/String_datatypes/scripts/str_repetative_type_error.py", line 14, in <module>
                final=string_1*string_2                    #Hello*Good Morning! 
            TypeError: can't multiply sequence by non-int of type 'str'