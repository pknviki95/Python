'''
for loop:

- for loop is used for iterating over a sequence.
- Iterating sequences  such as a list, a tuple, a dictionary, a set, or a string.
- The execution of iteration takes place based on the number of elements in sequence.

syntax:


for variable in sequence:
    statement

'''
#### String iteration:

string_variable='ramnad'

for iter in string_variable:
    print("string_variable elements: ",iter)

#### List iteration:

list_variable=[1,2,3,'viki',{1:'viki'}]

for iter in list_variable:
    print("list_variable elements: ",iter)

#### Tuple iteration:

tuple_variable=(1,2,3,'viki')

for iter in tuple_variable:
    print("tuple_variable elements: ",iter)

#### Set iteration:

set_variable={1,2,3,'viki'}

for iter in set_variable:
    print("set_variable elements: ",iter)

#### Dictionary iteration:

dict_variable={1:'viki',2:'raja',3:'bengaluru'}

for iter_key,iter_values in dict_variable.items():
    print("dict_variable key element: " ,iter_key)
    print("dict_variable value element: " ,iter_values)

#### Range iteration:

range_variable=4
for iter in range(0,range_variable):
    print("range_variable elements: ",iter)