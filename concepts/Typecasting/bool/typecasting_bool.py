'''
bool():

- bool() function is used to convert other datatypes to bool type value.

            bool(variable)

'''
# Integer to bool value:
#------------------------

# Program : To convert integer datatypes to boolean value using bool()

integer_non_zero_value=10
integer_zero_value=0

# Non-zero integer value return True boolean value
print("integer non_zero value converted to boolean  : {}".format(bool(integer_non_zero_value)))

# zero integer value return False boolean value
print("integer zero value converted to boolean : {}".format(bool(integer_zero_value)))

# Float to bool value:
#------------------------

# Program : To convert Float datatypes to boolean value using bool()

float_non_zero_value=0.123
float_zero_value=0.0

# Non-zero float value return True boolean value
print("float non_zero value converted to boolean  : {}".format(bool(float_non_zero_value)))

# zero float value return False boolean value
print("float zero value converted to boolean : {}".format(bool(float_zero_value)))

# complex to bool value:
#------------------------

# Program : To convert complex datatypes to boolean value using bool()

complex_non_zero_value=123+0j
complex_zero_value=0+0j

# Non-zero complex value in either real and imaginary part return True boolean value
print("complex non_zero value converted to boolean  : {}".format(bool(complex_non_zero_value)))

# zero complex value in both real and imaginary part return False boolean value
print("complex zero value converted to boolean : {}".format(bool(complex_zero_value)))

# String to bool value:
#------------------------

# Program : To convert String datatypes to boolean value using bool()

str_non_empty_value='Hello'
str_empty_value=''

# Non-empty string value return True boolean value
print("string non_empty value converted to boolean  : {}".format(bool(str_non_empty_value)))

# zero complex value in both real and imaginary part return False boolean value
print("string empty value converted to boolean : {}".format(bool(str_empty_value)))