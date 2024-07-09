# frozenset() - Frozenset datatypes:

- **Frozenset datatypes is similar to Set data type in python that can store values separated by ',' and enclosed within '{}'.but it should be assigned to frozenset(set_variable)**

            set_variable={element 1,element 2,...}   # set variable
            frozenset(set_variable)                  # frozen set variable

- Frozenset variable cannot contain **duplicate elements**
- Frozenset variable **un-ordered elements so indexing/Slicing operations cannot be performed.if tried indexing operation it throws type error**
- **The Main difference between "set" and "frozenset" is that set is "Mutable" and Frozenset is "Immutable"**
- **(i.e) "set objects values can be changed as it is mutable" but not for "frozen set as it is immutable"**

### [frozenset_type.py](https://github.com/pknviki95/Python/tree/main/concepts/Datatypes/Frozenset_datatypes/scripts/frozenset_type.py) - To find the frozenset type variable using type() function:

                set_variable={1,2,3,4,'viki',(1,2),3,4}

                print("The type of set variable after frozenset: {}".format(type(set_variable)))

                frozenset_variable=frozenset(set_variable)

                # Un-ordered value return for set
                print("unordered set_variable after frozenset: {}".format(frozenset_variable))

                print("The type of set variable after frozenset: {}".format(type(frozenset_variable)))

#### output:
                The type of set variable after frozenset: <class 'set'>
                unordered set_variable after frozenset: frozenset({1, 2, (1, 2), 3, 4, 'viki'})
                The type of set variable after frozenset: <class 'frozenset'>

- **Based on below dir() function frozenset doesn't have any write related operation only read related operations.**
- **If any attributes used apart from available one it throws attribute error**

### [frozenset_attribute_error.py](https://github.com/pknviki95/Python/tree/main/concepts/Datatypes/Frozenset_datatypes/scripts/frozenset_attribute_error.py) - frozenset is read-only immutable object is any changes are tried to made using attribute like list it throws error - Attribute error:

#### dir() output:

            ['__and__', '__class__', '__class_getitem__', '__contains__', '__delattr__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__iter__', '__le__', '__len__', '__lt__', '__ne__', '__new__', '__or__', '__rand__', '__reduce__', '__reduce_ex__', '__repr__', '__ror__', '__rsub__', '__rxor__', '__setattr__', '__sizeof__', '__str__', '__sub__', '__subclasshook__', '__xor__', 'copy', 'difference', 'intersection', 'isdisjoint', 'issubset', 'issuperset', 'symmetric_difference', 'union']

#### error:

                Traceback (most recent call last):
                File "/home/pknviki95/Learning/Python/concepts/Datatypes/Frozen_set_datatypes/scripts/frozenset_attribute_error.py", line 18, in <module>
                    frozenset_variable.add(3)
                AttributeError: 'frozenset' object has no attribute 'add'