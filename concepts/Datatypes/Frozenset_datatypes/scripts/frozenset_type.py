'''
# frozenset() - Frozen set datatypes:

- **Frozen set datatypes is similar to Set data type in python that can store values separated by ',' and enclosed within '{}'. but it should be assigned to frozenset(set_variable)**

            set_variable={element 1,element 2,...}   # set variable
            frozenset(set_variable)                  # frozen set variable

- Frozen Set variable cannot contain **duplicate elements**
- Frozen Set variable **un-ordered elements so indexing/Slicing operations cannot be performed.if tried indexing operation it throws type error**
- **The Main difference between "set" and "frozenset" is set is "Mutable" and Frozenset is "Immutable"**
- **(i.e) set objects values can be changes but not for frozen set as it is immutable**


'''

set_variable={1,2,3,4,'viki',(1,2),3,4}

print("The type of set variable after frozenset: {}".format(type(set_variable)))

frozenset_variable=frozenset(set_variable)

# Un-ordered value return for set
print("unordered set_variable after frozenset: {}".format(frozenset_variable))

print("The type of set variable after frozenset: {}".format(type(frozenset_variable)))