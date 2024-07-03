'''
- if any string is not defined in integral with base-10 it will throw value error
- Make sure it is always in base-10 (i.e) value should be decimal values ; oct,bin,hex,float values are not possible to typecast
'''



# string to integer value:

string_value='0B111'

#Integer value as it returns value error as it is not in base-10
print("String without base-10 converted to int: {}".format(int(string_value))) 