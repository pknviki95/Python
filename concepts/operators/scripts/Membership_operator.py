'''
## Membership operator:

- **Membership operator returns the boolean values of members/elements in sequence objects.**
    
    - **Membership operator in**
    - **Membership operator not in**


### Membership operator in:

- **Returns "True" if member/element present in sequence objects; else it returns "False".** 

### Membership operator not in:

- **Returns "True" if member/element not present in sequence objects; else it returns "False".** 

'''
### Membership operator in:

### String Sequence:

str_sequence="I am Vignesh"

print(" member present in str_sequence: ",'V' in str_sequence)

# Python is case-sensitive so it return false

print(" member present in str_sequence: ",'v' in str_sequence)

### List Sequence:

list_sequence=[1,2,5,'viki',2.5]

print(" member present in list_sequence: ",1 in list_sequence)

# Python is case-sensitive so it return false

print(" member present in list_sequence: ",'Viki' in list_sequence)

### Tuple Sequence:

tuple_sequence=(1,2,5,'viki',2.5)

print(" member present in tuple_sequence: ",8 in tuple_sequence)

# Python is case-sensitive so it return false

print(" member present in tuple_sequence: ",'viki' in tuple_sequence)

### Set Sequence:

Set_sequence={1,2,5,'viki',2.5}

print(" member present in Set_sequence: ",8 in Set_sequence)

# Python is case-sensitive so it return false

print(" member present in Set_sequence: ",'Viki' in Set_sequence)

### Dictionary Sequence:

dict_sequence={1:2,5:'viki',7:2.5}

print(" member present in dict_sequence: ",1 in dict_sequence)

# Python is case-sensitive so it return false
# By default in looks for key values in dictionary
print(" member present in dict_sequence: ",'viki' in dict_sequence)

### Membership operator not in:

### String Sequence:

str_sequence="I am Vignesh"

print(" member present not in str_sequence: ",'V' not in str_sequence)

# Python is case-sensitive so it return false

print(" member present not in str_sequence: ",'v' not in str_sequence)

### List Sequence:

list_sequence=[1,2,5,'viki',2.5]

print(" member present not in list_sequence: ",1 not in list_sequence)

# Python is case-sensitive so it return false

print(" member present not in list_sequence: ",'Viki' not in list_sequence)

### Tuple Sequence:

tuple_sequence=(1,2,5,'viki',2.5)

print(" member present not in tuple_sequence: ",8 not in tuple_sequence)

# Python is case-sensitive so it return false

print(" member present not in tuple_sequence: ",'viki' not in tuple_sequence)

### Set Sequence:

Set_sequence={1,2,5,'viki',2.5}

print(" member present not in Set_sequence: ",8 not in Set_sequence)

# Python is case-sensitive so it return false

print(" member present not in Set_sequence: ",'Viki' not in Set_sequence)

### Dictionary Sequence:

dict_sequence={1:2,5:'viki',7:2.5}

print(" member present not in dict_sequence: ",1 not in dict_sequence)

# Python is case-sensitive so it return false
# By default in looks for key values in dictionary
print(" member present not in dict_sequence: ",'viki' not in dict_sequence)