'''
set() - set datatypes:

- **Set is data type in python that can store values separated by ',' and enclosed within '{}'.**

            set_variable={element 1,element 2,...}

- Set variable cannot contain **duplicate elements**
- Set variable **un-ordered elements so indexing/Slicing operations cannot be performed.**
- **Heterogeneous objects are allowed in tuple (i.e) it can hold int,str,tuple etc., elements within its collection enclosed in {} bracket.**
- Set is **mutable object - (i.e) Values of set object can be changed**

'''

set_variable={1,2,3,4,'viki',(1,2),3,4}

# Un-ordered value return for set
print("unordered set_variable: {}".format(set_variable))
print("The type of set variable: {}".format(type(set_variable)))