'''
## Identity operator:

- **Identity operators returns boolean values by verifying the identity values of objects.**

    - **Identity operator is**
    - **Identity operator isnot**

### Identity operator is:

- **Returns "True" is both identity values point to the same objects; else it returns "False".** 

### Identity operator isnot:

- **Returns "True" is both identity values doesn't point to the same objects; else it returns "False".** 

'''

### Identity operator is:


x=10
y=10

print(f"identity of x= {id(x)}")
print(f"identity of y= {id(y)}")

# Is same identity - Returns True

print("x is y",x is y)

x=10
y=20

print(f"identity of x= {id(x)}")
print(f"identity of y= {id(y)}")

# is Different identity - Returns False

print("x is y",x is y)

### Identity operator isnot:

### isnot same identity - Returns False

x=10
y=10

print(f"identity of x= {id(x)}")
print(f"identity of y= {id(y)}")

# isnot same identity - Returns False

print("x is y",x is y)

### isnot Different identity - Returns True

x=10
y=20

print(f"identity of x= {id(x)}")
print(f"identity of y= {id(y)}")

# isnot Different identity - Returns True

print("x is y",x is y)