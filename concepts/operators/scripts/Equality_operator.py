'''
- **Equality operators are used to validate if the given two values are equal(==) and equal or not (!=)**

'''

### Integer value:

x=10
y=20

### Equal to(==):

Equal_to=x==y
print("x is equal to y: ",Equal_to)

### Not Equal to(!=):

not_Equal_to=x!=y
print("x is not equal to y: ",not_Equal_to)

### string value:

x='viki'
y='guru'

Equal_to=x==y
print("x is equal to y: ",Equal_to)

### Not Equal to(!=):

not_Equal_to=x!=y
print("x is not equal to y: ",not_Equal_to)

### Boolean value:

x=True
y=False

Equal_to=x==y
print("x is equal to y: ",Equal_to)

### Not Equal to(!=):

not_Equal_to=x!=y
print("x is not equal to y: ",not_Equal_to)

# Multiple Equality operations:

# All values return True

x=10==20==30==40
print("x value is : ",x)

# Atleast 1 values false return false

y=10==20==30==40!=50
print("y value is : ",y)