'''
complex to float value:

- complex value cannot be converted to float value as it has imaginary part to it so it throws type error
'''

# Program: To convert complex datatypes to float value using float()- Type error:

complex_value=10+20j

#Type error as complex to float value is not possible due to img part
print("complex converted to float: {}".format(float(complex_value)))