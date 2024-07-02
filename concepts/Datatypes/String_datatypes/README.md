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
### error:

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