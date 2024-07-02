'''
Limitation of string implementation:

-  **Triple quotes(""" """)/(''' ''')** is possible to assign multi-line string literals for any variable
- Using various string quotes as special character (i.e) usage of '' or "" inside a string can be done only by declaing the string variable in triple quotes
'''

# String variable Limitaions for Multi-line string literals
# single/Double quotes:

sentence = '- If the string
            - If the string'

# Triple quotes

multi_line_sentence= '''- If the string                     
                        - If the string'''

print("single: {}",sentence)
print("multi_line_sentence: ",multi_line_sentence)


# String variable Limitaions for using various single/double quotes as special character

#single quotes

character= ' Hello all, Welcome to 'Learning' '
print(character)

# Triple quotes to use ingle/double quotes as special character
character= ''' Hello all, Welcome to 'Learning' '''
print(character)