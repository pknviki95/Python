'''
int():

- int() function is used to convert other datatypes to integer type value.

            int(variable)
'''

# float to integer value:

float_value=10.998

#integer value by neglecting decimal value
print("float converted to int: {}".format(int(float_value)))                 


# boolean to integer value:

boolean_value=True

# Integer value as it returns its equivalent integer value (i.e) True=1 and False=0
print("Boolean converted to int: {}".format(int(boolean_value)))   

# string to integer value:

string_value='15'

# #Integer value as it returns integer value as it is in base-10
print("String converted to int: {}".format(int(string_value)))  