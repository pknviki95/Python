'''
- Tuple is read-only immutable object is any changes are tried to made using attribute like list it throws error - Attribute error:

'''

tuple_variable=(1,2,3,4,'viki')


# Attribute error:
# Based on above dir() function tuple doesn't have any write related operation only read related operations.
# If any attributes used apart from available one it throws attribute error
print(dir(tuple_variable))
tuple_variable.append(3)
