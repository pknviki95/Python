'''
- **If the basic rule as above if any string is not defined in integral with base-10 it will throw value error**
**(i.e) value should be decimal/float values ; oct,bin,hex values are not possible to typecast**
'''

string_value='0B111'

#complex value as it returns value error as it is not in base-10
print("String without base-10 converted to complex real value: {}".format(complex(string_value)))