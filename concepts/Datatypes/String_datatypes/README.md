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
- As to resolve this issue only **Triple quotes(""" """)/(''' ''')** is possible to assign multi-line string for any variable (i.e) Triple-quotes are used to define multi-line string literals

### Program: String variable Limitaions for Multi-line string literals

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
--------------------------------------------------------------------------------------------------------------------------------------------------------
### 2:Using various string quotes as special character:

- Using various **single/double quotes as special character** (i.e) usage of '' or "" inside a string can be done only by declaing the string variable in **triple quotes** or it will throw Syntax error

### Program: String variable Limitaions for using various single/double quotes as special character

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
---------------------------------------------------------------------------------------------------------------------------------------------------------

### Program: To find the integer type variable using type() function:

            x='viki'                        #single quotes
            y="siva"                        #double quotes
            z="""karthi"""                  #triple quotes

            print("The type of single quotes x is: ",type(x))
            print("The type of double quotes y is: ",type(y))
            print("The type of triple quotes z is: ",type(z))
------------------------------------------------------------------------------------------------

## Indexing:

- In Python, indexing refers to the **process of accessing a specific element in a sequence, such as a string or list, using its position or index number**.
- Indexing in Python starts at **0**, which means that the **first element in a sequence has an index of 0, the second element has an index of 1, and so on**. 

            variable[index number]
- Indexing can be peroformed only with the total index present in the string;if we ask for return value that exceeds existing index range it throws Index error

### Program: To understand the Indexing range of string - Index error

            sequence = 'vignesh'
            print('sequence[10]',sequence[10])  # Index range exceeds the existing range 7 so it throws Index error 

#### error

            Traceback (most recent call last):
            File "/home/pknviki95/Learning/Python/concepts/Datatypes/String_datatypes/scripts/str_index_error.py", line 8, in <module>
                print('sequence[10]',sequence[10])
            IndexError: string index out of range
-----------------------------------------------------------------------------------------------------------------------------------------------

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
| :---:   | :---: | :---: | :---: | :---: |
| **Negative Index**  |  **-4**   |  -**3** | **-2** | **-1** |

### Program: To find the index value of the string based on positive and negative index

#### Positive Index

            sequence = 'vignesh'

            print('sequence[0]',sequence[0])
            print('sequence[1]',sequence[1])
            print('sequence[2]',sequence[2])
            print('sequence[3]',sequence[3])
            print('sequence[4]',sequence[4])
            print('sequence[5]',sequence[5])
            print('sequence[6]',sequence[6])

#### Negative Index

            sequence = 'vignesh'

            print('sequence[-1]',sequence[-1])
            print('sequence[-2]',sequence[-2])
            print('sequence[-3]',sequence[-3])
            print('sequence[-4]',sequence[-4])
            print('sequence[-5]',sequence[-5])
            print('sequence[-6]',sequence[-6])
            print('sequence[-7]',sequence[-7])
----------------------------------------------------------------------------------------------------------------------

## String Slicing: (Working with Index): 

- Slicing is used **to obtain sub-string from string by accessing index value of string**.

            variable[start index:end index:step] 

            start index : starting index-value of string 
            end index : ending index-value for string (i.e) end-1 
            step : range of sub-string from string 


### Program: To find the index value of the string based on positive and negative index

#### Positive Index slicing

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

#### Negative Index slicing

            sequence = 'vignesh'

            #variable[start index:end index] - Here the start index/end index is equivalent negative index value of positive index
            print('Negative variable[start index:end index]: ',sequence[-6:-2])  

            #variable[:end index] - By default start index is index 0 equivalent negative index
            print('Negative variable[:end index]: ',sequence[:-3])         

            #variable[start index:] - Here the start index is equivalent negative index value of positive index
            print('Negative variable[start index:]: ',sequence[-7:])   

            #variable[start index:end index:step] - It returns from index 1->3->5 (start+3(step) till end index value)
            print('Negative variable[start index:end index:step]: ',sequence[-7:-2:3]) 
---------------------------------------------------------------------------------------------------------------------------------------------------------