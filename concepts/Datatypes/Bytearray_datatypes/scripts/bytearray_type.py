'''
bytearray() -  ByteArray Datatypes:

- Python bytearray are a **sequence of integers in the range of 0-255**. it is similar to bytes 
- Bytearray are an **mutable sequence data type**, meaning once a bytes object is created, it can be changed.
- **(i.e) unlike bytes object the changes can be made on sequence using bytearray() object**
- **They are ordered sequence (i.e) Indexig and slicing operation are possible.**

                list_variable=[element_1,element_2,...]
                bytearrray_variable=bytearray(list_variable)

'''

# sequence of numbers range from 0-255

list_variable=[1,2,3,65,66]

# bytearray() for using bytearray objects
bytearray_variable=bytearray(list_variable)

print("bytearray_variable: ",bytearray_variable)
print("The type of bytearray_variable : ",type(bytearray_variable))