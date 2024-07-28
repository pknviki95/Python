'''
command-line arguments sys.argv value outside the index range passed throws error - Index error:

'''

import sys

### command line arguments:

### argument values stored as list of elements in argv variable 

print("sys.argv variable values: ",sys.argv)


### Accessing individual element using indexing in argv variable.

print("sys.argv[0] variable values: ",sys.argv[0])
print("sys.argv[1] variable values: ",sys.argv[1])
print("sys.argv[2] variable values: ",sys.argv[2])

### Accessing individual element outside index in argv variable throws error: Index error.

print("sys.argv[2] variable values: ",sys.argv[10])