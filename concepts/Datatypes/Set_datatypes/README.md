# set() - set datatypes:

- **Set is data type in python that can store values separated by ',' and enclosed within '{}'.**

            set_variable={element 1,element 2,...}

- Set variable cannot contain **duplicate elements**

### [set_dup_unorder.py](https://github.com/pknviki95/Python/tree/main/concepts/Datatypes/Set_datatypes/scripts/set_dup_unorder.py) - To find the set variable return unordered value and neglecting of duplicate values:

                set_variable={1,2,3,4,'viki',(1,2),3,4}

                # Neglecting Duplicate values and returningin un-ordered way:
                print("unordered set_variable: {}".format(set_variable))

#### output:
                unordered set_variable: {1, 2, (1, 2), 3, 4, 'viki'} # Un-ordered value return for set

- Set variable **un-ordered elements so indexing/Slicing operations cannot be performed.if tried indexing operation it throws type error**

### [set_index_slice_type_error.py](https://github.com/pknviki95/Python/tree/main/concepts/Datatypes/Set_datatypes/scripts/set_index_slice_type_error.py) - Index/slice operation in set objects throws error as it is un-ordered datatype - Type error:

### Indexing:
                set_variable={1,2,3,4,'viki',(1,2),3,4}

                # Un-ordered value return for set if indexed throws error
                print("unordered set_variable: {}".format(set_variable[1]))
#### slicing:

                set_variable={1,2,3,4,'viki',(1,2),3,4}

                # Un-ordered value return for set if indexed throws error
                print("unordered set_variable: {}".format(set_variable[1:2]))

#### error:
                Traceback (most recent call last):
                File "/home/pknviki95/Learning/Python/concepts/Datatypes/Set_datatypes/scripts/set_index_type_error.py", line 11, in <module>
                    print("unordered set_variable: {}".format(set_variable[1]))
                TypeError: 'set' object is not subscriptable

- Set is **mutable object - (i.e) Values of set object can be changed**

### [set_type.py](https://github.com/pknviki95/Python/tree/main/concepts/Datatypes/Set_datatypes/scripts/set_type.py) - To find the set type variable using type() function:

                set_variable={1,2,3,4,'viki',(1,2),3,4}

                print("unordered set_variable: {}".format(set_variable))
                print("The type of set variable: {}".format(type(set_variable)))

#### output:
                unordered set_variable: {1, 2, (1, 2), 3, 4, 'viki'}  # Un-ordered value return for set
                The type of set variable: <class 'set'>

## Limititaions:

### 1: Empty {} variable is considered as dictionary objects:

- **By default The empty declaration of variable with {} is considered as Dictionary object. To tell PVM that it is set object we need to declare set(variable)**

                set_variable={}  => By default Dictionary object
                set(set_variable) => set object

### [set_limitiation.py](https://github.com/pknviki95/Python/tree/main/concepts/Datatypes/Set_datatypes/scripts/set_limitiation.py) - To convert default empty dict to set object by declaring set() function:

#### without set () fun returns dict:
                # Empty varibale with {} braces
                set_variable={}
                print("unordered set_variable type without set() function: {}".format(type(set_variable)))

#### output:
                unordered set_variable type without set() function: <class 'dict'>

#### with set () fun returns set:
                # Empty varibale with {} braces
                set_variable={}
                print("unordered set_variable type with set() function: {}".format(type(set(set_variable))))
#### output:

                unordered set_variable type with set() function: <class 'set'>

### 2: Declaring dict,list,set( Mutable objects) inside set variable it throws Type error -  unhashable type:

- **Heterogeneous objects are allowed in set (i.e) it can hold int,str,tuple etc., elements within its collection enclosed in {} bracket.**
- If any values like dict,list,set( Mutable objects) inside set variable it throws Type error -  unhashable type

### [set_unhashable_type_error.py](https://github.com/pknviki95/Python/tree/main/concepts/Datatypes/Set_datatypes/scripts/set_unhashable_type_error.py)  - Declaring dict,list,set( Mutable objects) inside set variable it throws - Type error - unhashable type:

#### set with list elements:

                set_variable_list={[1,2]}
                print(" The set variable with list elements: ",set_variable_list)

#### error:

                Traceback (most recent call last):
                File "/home/pknviki95/Learning/Python/concepts/Datatypes/Set_datatypes/scripts/set_unhashable_type_error.py", line 9, in <module>
                    set_variable_list={[1,2]}
                TypeError: unhashable type: 'list'

#### set with dict elements:

                set_variable_dict={{1:'viki'}}
                print(" The set variable with dict elements: ",set_variable_dict)

#### error:

                Traceback (most recent call last):
                File "/home/pknviki95/Learning/Python/concepts/Datatypes/Set_datatypes/scripts/set_unhashable_type_error.py", line 12, in <module>
                    set_variable_dict={{1:'viki'}}
                TypeError: unhashable type: 'dict'

#### set with set elements:

                set_variable_set={{1,2}}
                print(" The set variable with set elements: ",set_variable_set)

#### error:

                Traceback (most recent call last):
                File "/home/pknviki95/Learning/Python/concepts/Datatypes/Set_datatypes/scripts/set_unhashable_type_error.py", line 15, in <module>
                    set_variable_set={{1,2}}
                TypeError: unhashable type: 'set'
