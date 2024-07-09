# dict() - Dictionary datatypes:

- The dict datatype is used to represent **collection of elements in "{key:value}" pair** 
- The dictionary datatype is **un-ordered collection of key value pair elements (i.e) Indexing and slicing is not possible** 
- **Dictionary is mutable (i.e) The value of dictionary can be edited or changed**

                dictionary_variable={key_1:value_1, key_2:value_2, ...}


### [dict_type.py](https://github.com/pknviki95/Python/tree/main/concepts/Datatypes/Dictionary_datatypes/scripts/dict_type.py) - To find the dictionary type variable using type() function:

                dictionary_variable = {1:'viki',2:'siva'}
                print("The type of dictionary_variable is: ",type(dictionary_variable))

#### output:
                The type of dictionary_variable is:  <class 'dict'>

- **Key and values can be added to dictionary by assigning of value to key for a given dictionary using below syntax.**

                dictionary_variable[key]=value 
                
### [dict_add_value_key.py](https://github.com/pknviki95/Python/tree/main/concepts/Datatypes/Dictionary_datatypes/scripts/dict_add_value_key.py) - To add the value to key to empty dictionary or add key and value to dictionary:


                dictionary_variable = {1:'viki',2:'siva'}

                # Adding key 3 and its vaue karthi to dictionary_variable 

                #dictionary_variable[key]=value
                dictionary_variable[3]='karthi'
                                
                print("The type of dictionary_variable is: ",dictionary_variable)

#### output:

                The type of dictionary_variable is:  {1: 'viki', 2: 'siva', 3: 'karthi'}

- **Duplicate keys are not allowed but duplicate values are allowed** 
- **It doesn't throw error when duplicate key is used instead it updates the existing key to new value assigned to it**

### [dict_dup_key_value.py](https://github.com/pknviki95/Python/tree/main/concepts/Datatypes/Dictionary_datatypes/scripts/dict_dup_key_value.py) - To verify the condition of duplicate key and value in dictionary:

### Duplicate key:
                dictionary_variable={1:'viki',2:'guru'}

                # Adding duplicate key to dictionary_variable
                dictionary_variable[2]='karthi'
                
                print("dictionary_variable after adding duplicate key: ",dictionary_variable)  

#### output:
                dictionary_variable after adding duplicate key:  {1: 'viki', 2: 'karthi'}

### Duplicate value:

                dictionary_variable={1:'viki',2:'guru'}

                # Adding duplicate value to dictionary_variable
                dictionary_variable[1]='karthi'
                dictionary_variable[2]='karthi'
                dictionary_variable[3]='karthi'

                print("dictionary_variable after adding duplicate value: ",dictionary_variable)

#### output:
                dictionary_variable after adding duplicate value:  {1: 'karthi', 2: 'karthi', 3: 'karthi'}