'''
bytes() -  Bytes Datatypes:

- Python bytes are a **sequence of integers in the range of 0-255**. 
- They are an **immutable sequence data type**, meaning once a bytes object is created, it cannot be changed.
- **They are ordered sequence (i.e) Indexig and slicing operation are possible.**

                list_variable=[element_1,eement_2,...]
                bytes_variable=bytes(list_variable)

'''

# sequence of numbers range from 0-255

list_variable=[1,2,3,65,66]

# bytes() for using bytes objects
bytes_variable=bytes(list_variable)

print("bytes_variable: ",bytes_variable)
print("The type of bytes_variable : ",type(bytes_variable))