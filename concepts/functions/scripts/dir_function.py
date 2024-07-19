'''
## dir():

- The dir() function returns all properties and methods of the specified object, without the values.

- This function will return all the properties and methods, even built-in properties which are default for all object.

                    dir(object)
'''


import math

# dir() function returns list of attributes and other methods related to that objects

print("Attributes of math module using dir() function: ",dir(math))
