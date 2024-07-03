'''
float():

- float() function is used **to convert other datatypes to float type value.**

            float(variable)
'''

# integer to float value:

integer_value=10

#float value by including decimal value
print("integer converted to float: {}".format(float(integer_value)))                  


# boolean to float value:

boolean_value=True

# float value as it returns its equivalent integer value with decimal point (i.e) True=1 and False=0
print("Boolean converted to float: {}".format(float(boolean_value)))   

# string to float value:

string_value='15'

# float value as it returns float value/integer value as it is in base-10
print("String converted to float: {}".format(float(string_value))) 