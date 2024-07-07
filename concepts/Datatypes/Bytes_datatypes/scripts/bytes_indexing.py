'''
## Indexing:

- **Elements of bytes can be accessed using indexing/slicing as list is ordered preserved**

'''

### Positive Index

sequence = [65,66,67,68]
bytes_variable=bytes(sequence)

print(bytes_variable)

print('bytes_variable[0]',bytes_variable[0])
print('bytes_variable[1]',bytes_variable[1])
print('bytes_variable[2]',bytes_variable[2])
print('bytes_variable[3]',bytes_variable[3])

### Negative Index

print('bytes_variable[-1]',bytes_variable[-1])
print('bytes_variable[-2]',bytes_variable[-2])
print('bytes_variable[-3]',bytes_variable[-3])
print('bytes_variable[-4]',bytes_variable[-4])