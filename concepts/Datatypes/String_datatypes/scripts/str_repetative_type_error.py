'''
- Basic rule is one argument should be **by default string and the other integer type for number to perform repetative**
- If the basic rule is not followed and if both are repetative with str type then it throws type error

            #type error
            str * str 
'''

# Program: concantinate two strings using * repetative operator - Type error:

string_1="Hello"
string_2="Good Morning!"

final=string_1*string_2                    #Hello*Good Morning! 
print("final_concantinated string: ",final)