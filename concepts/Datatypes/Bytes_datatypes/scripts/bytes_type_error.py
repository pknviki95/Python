'''
- Bytes are an **immutable sequence data type**, meaning once a bytes object is created, it cannot be changed.

'''


sequence = [65,66,67,68]
bytes_variable=bytes(sequence)

# Assigning value to bytes variable throws Type error
bytes_variable[2]=60
print(bytes_variable)