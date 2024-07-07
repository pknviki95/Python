'''
## Indexing:

- **Elements of bytearray can be accessed using indexing/slicing as list is ordered preserved**

'''

### Positive Index

sequence = [65,66,67,68]
bytearray_variable=bytearray(sequence)

print(bytearray_variable)

print('bytearray_variable[0]',bytearray_variable[0])
print('bytearray_variable[1]',bytearray_variable[1])
print('bytearray_variable[2]',bytearray_variable[2])
print('bytearray_variable[3]',bytearray_variable[3])

### Negative Index

print('bytearray_variable[-1]',bytearray_variable[-1])
print('bytearray_variable[-2]',bytearray_variable[-2])
print('bytearray_variable[-3]',bytearray_variable[-3])
print('bytearray_variable[-4]',bytearray_variable[-4])