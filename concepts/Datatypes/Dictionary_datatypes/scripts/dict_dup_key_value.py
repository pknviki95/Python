'''
- **Duplicate keys are not allowed but duplicate values are allowed** 
- If the same key is taken with new value then it replaces the existing key value to new assigned value 

                dictionary_variable[key]=value

                # Duplicate key - Not allowed
                # Duplcate value - Allowed

'''

dictionary_variable={1:'viki',2:'guru'}

# Duplicate key:

dictionary_variable[2]='karthi'
print("dictionary_variable after adding duplicate key: ",dictionary_variable)   #{1: 'viki', 2: 'karthi'}

# Duplicate value:

dictionary_variable[1]='karthi'
dictionary_variable[3]='karthi'
print("dictionary_variable after adding duplicate value: ",dictionary_variable)   #{1: 'viki', 2: 'karthi'}