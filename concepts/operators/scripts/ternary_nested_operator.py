'''
### Nesting of ternary operator:

- **Nested ternary operator can be performed for multiple operands scenario.**

### Syntax:
            [True value] if [condition] else [True value] if [condition] else [false value]
'''

a=30
b=20
c=60

# [True value] if [condition] else [True value] if [condition] else [false value]

final=a if a<b and a<c else b if b<a and b<c else c

print("Ternary operator value of final: ",final)