'''
## Bitwise operator:

- **Bitwise operators are used to compare (binary) numbers**
- **Bitwise operators are applicable only for "int" and "bool" datatype**
- **If other datatypes are performed with Bitwise operation it returns type error.**
   
    - **Bitwise and (&)** 
    - **Bitwise or (|)** 
    - **Bitwise x-or (^)** 
    - **Bitwise complement (~)** 
    - **Bitwise left shift (<<)** 
    - **Bitwise Right shift (>>)** 

'''

x=10
y=40

## Bitwise and (&):

# Both 1/True return 1
# If any one 0 return 0

print("Bitwise and (&) for x and y: ",x&y)

## Bitwise or (|):

# Both 1/True return 1
# If at least 1 return 1
# If Both zero returns 0

print("Bitwise or (|) for x or y: ",x|y)

## Bitwise x-or (^):

# Both different return 1
# If both same returns 0

print("Bitwise x-or (^) for x x-or y: ",x^y)

## Bitwise complement(~):
## Positive complement value:

z=4

print("Bitwise complement (~) for Positive ~z: ",~z)

## Negative complement value:

z=-11

print("Bitwise complement (~) for Negative ~z: ",~z)


### Bitwise leftshift(<<):
### Positive value:
z=24
# shift left by 2 bits
print("Bitwise leftshift (<<) for Positive z: ",z<<2)

### Negative value:

z=-24
# shift left by 2 bits
print("Bitwise leftshift (<<) for Negative z: ",z<<2)

### Bitwise rightshift(>>):
### Positive value:
z=24
# shift right by 2 bits
print("Bitwise rightshift (>>) for Positive z: ",z>>2)



### Bitwise rightshift(>>):
### Negative value:
z=-24
# shift right by 2 bits
print("Bitwise rightshift (>>) for Negative z: ",z>>2)