'''
Bytearray type can be updaed or changed as it is mutable:
'''

sequence = [65,66,67,68]
bytearray_variable=bytearray(sequence)
print("bytearray_variable before assigning: ",bytearray_variable)

# Assigning value to bytearray variable is possible as it is Mutable object
bytearray_variable[2]=1
print("bytearray_variable after assigning: ",bytearray_variable)