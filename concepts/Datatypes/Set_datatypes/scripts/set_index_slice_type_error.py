'''

- Set variable **un-ordered elements so indexing/Slicing operations cannot be performed.if tried indexing operation it throws type error**
- Index operation in set objects throws error asit is un-ordered datatype - Type error:

'''
# Indexing

set_variable={1,2,3,4,'viki',(1,2),3,4}

# Un-ordered value return for set if indexed throes error
print("unordered set_variable: {}".format(set_variable[1]))

# slicing:

set_variable={1,2,3,4,'viki',(1,2),3,4}

# Un-ordered value return for set if indexed throes error
print("unordered set_variable: {}".format(set_variable[1:2]))