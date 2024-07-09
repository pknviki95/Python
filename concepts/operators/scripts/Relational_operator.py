'''
Relational operator:

- Relational Operators in python helps to find the relation between values and return boolean result. 
- some of the relational operations are 
        - greater than(>),
        - greater than or equal to (>=), 
        - lesser than (<), 
        - less than or equal to(<=)

'''

### Integer value:

x=10
y=20

### greater than(>):

greater_than=x>y
print("x is greater than y: ",greater_than)

### greater than or equal to (>=):

greater_than_or_equal_to=x>=y
print("x is greater than or equal to y: ",greater_than_or_equal_to)

### lesser than (<): 

lesser_than=x<y
print("x is lesser than y: ",lesser_than)

### less than or equal to(<=):

lesser_than_or_equal_to=x<=y
print("x is lesser than or equal to y: ",lesser_than_or_equal_to)

'''
String value:

- **Relational operators can be performed in string values by changing into ordinal equivalent values then returns the booean results**
- **It compares first char of string and if it is equal and it switched to second and based on relation it returns boolean result**

'''

### string value:

x='viki'
y='guru'

### greater than(>):

greater_than=x>y                    # 118 > 103
print("x is greater than y: ",greater_than)

### greater than or equal to (>=):

greater_than_or_equal_to=x>=y           # 118 >= 103
print("x is greater than or equal to y: ",greater_than_or_equal_to)

### lesser than (<): 

lesser_than=x<y                         # 118 < 103
print("x is lesser than y: ",lesser_than)

### less than or equal to(<=):

lesser_than_or_equal_to=x<=y                # 118 <= 103 
print("x is lesser than or equal to y: ",lesser_than_or_equal_to)

'''
### 3: Boolean value:

- **Boolean values are converted to its equivalent integral value as True=1 and False=0 and it can perform Relational operator based on the above values**

'''
### Boolean value:

x=True
y=False

### greater than(>):

greater_than=x>y                    # 1 > 0
print("x is greater than y: ",greater_than)

### greater than or equal to (>=):

greater_than_or_equal_to=x>=y           # 1 >= 0
print("x is greater than or equal to y: ",greater_than_or_equal_to)

### lesser than (<): 

lesser_than=x<y                         # 1 < 0
print("x is lesser than y: ",lesser_than)

### less than or equal to(<=):

lesser_than_or_equal_to=x<=y                # 1 <= 0 
print("x is lesser than or equal to y: ",lesser_than_or_equal_to)

'''
### 4: Multiple relational operations:

- **Multiple relational operation can be performed for a values** 
- **It returns True boolean result if all the return values are True.** 
- **It returns False even if there is single false value**

'''
# All values return True

x=10<20<30<40
print("x value is : ",x)

# Atleast 1 values false return false

y=10<20<30<40>50
print("y value is : ",y)