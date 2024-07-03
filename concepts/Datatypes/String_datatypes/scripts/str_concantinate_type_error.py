'''
- String concatination is applicable only if it is between string; if we are triying concatination with string with other datatypes it throws Type error

        #Type error
        str+int

'''

# Program: concantinate strings with other datatype using + operator - Type error:

string_1="Hello"
int_2=10

#String concatination with other datatype

final=string_1+'\t'+int_2                   #Type error

print("final_concantinated string with other datatype : ",final)