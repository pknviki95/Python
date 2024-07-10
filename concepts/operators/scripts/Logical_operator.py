'''
Logical operator:

- **Logical operator is used to combine conditional statements using and,or,not**
- **Incase of "and";If only every condition passed is satisfied then it return True ; If even one condition doesn't satisfy then it returns False**
- **Incase of "or"; Even if any one condition passed it returns True; returns False if all the conditions failed**
- **"not" return complement value of each other**

'''

### Boolean Types:

### and:

# Return True if both condition passes:
# Return False even if one condition fails:

print("Both True: ",True and True)                  # True
print("1st True and 2nd False: ",True and False)    # False
print("1st False and 2nd True: ",False and True)    # False
print("Both False: ",False and False)               # False

### or:

# Return True if at least one condition passes:
# Return False if all condition fails:

print("Both True: ",True or True)               # True
print("1st True or 2nd False: ",True or False) # True
print("1st False or 2nd True: ",False or True) # True
print("Both False: ",False or False)            # False

### not:

# Return False if condition True
# Return True if condition False

print("not True: ",not True)                # False
print("not False: ",not False)              # True


### Non-Boolean Types:

###  and:
'''
- In Non-boolean Types if the 1st argument condition is False; It return 1st argument value
- If the 1st argument condition is True; It return 2nd argument value
'''
# 1st argument non-empty - True

x=10
y=20

print("Non-boolean and 1st argument True returns 2nd argument value: ",x and y)

# 1st argument empty - False

x=''
y='viki'

print("Non-boolean and 1st argument False returns 1st argument value: ",x and y)

### or:

'''
- In Non-boolean Types if the 1st argument condition is False; It return 2nd argument value
- If the 1st argument condition is True; It return 1st argument value
'''
# 1st argument non-empty - True

x=10
y=20

print("Non-boolean or 1st argument True returns 1st argument value: ",x or y)

# 1st argument empty - False

x=''
y='viki'

print("Non-boolean or 1st argument False returns 2nd argument value: ",x or y)