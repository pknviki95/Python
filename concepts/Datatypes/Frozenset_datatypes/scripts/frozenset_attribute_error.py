'''

- **The Main difference between "set" and "frozenset" is set is "Mutable" and Frozenset is "Immutable"**
- **(i.e) "set objects values can be changed as it is mutable" but not for "frozen set as it is immutable"**

'''


set_variable={1,2,3,4,'viki',(1,2),3,4}

frozenset_variable=frozenset(set_variable)

# Attribute error:
# Based on above dir() function frozenset doesn't have any write related operation only read related operations.
# If any attributes used apart from available one it throws attribute error

print(dir(frozenset_variable))
frozenset_variable.add(3)