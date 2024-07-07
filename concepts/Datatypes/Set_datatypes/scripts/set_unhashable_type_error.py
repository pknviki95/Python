'''
Declaring dict,list,set( Mutable objects) inside set variable it throws Type error -  unhashable type:

- **Heterogeneous objects are allowed in set (i.e) it can hold int,str,tuple etc., elements within its collection enclosed in {} bracket.**
- If any values like dict,list,set( Mutable objects) inside set variable it throws Type error -  unhashable type

'''

# set with dict elements:

set_variable_list={[1,2]}
print(" The set variable with list elements: ",set_variable_list)

#set with dict elements:

set_variable_dict={{1:'viki'}}
print(" The set variable with dict elements: ",set_variable_dict)

# set with set elements:
set_variable_set={{1,2}}
print(" The set variable with set elements: ",set_variable_set)
