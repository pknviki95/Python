'''
del statement if used to delete elements of sequence for immutable objects it throws error - Type error:

'''

#### Mutable objects supports index deletion as it is Mutable:

list_variable=['viki',2,5,7]

# deleting mutable objects element using indexing 

del list_variable[1]
print("list_variable: ",list_variable)

#### Immutable objects does supports index deletion as it is immutable:

string_variable='viki'

# deleting Immutable objects element using indexing 
# throws error - Type error 

del string_variable[1]
print("string_variable: ",string_variable)