
'''
Immutable object:

- Immutable objects are those that **doesn't allow you to change their value or data in place**
- **If any changes is made in the object then the identity of that object chages**
- Immuttable objects are as below

		Integer
		Float
		Strings
		Boolean
		Frozenset
		Tuples
		Byte

'''
# Integer object:

# id vaue of initial object declaration
integer_variable_1=10
print("id value of integer_variable_1  : {}".format(id(integer_variable_1)))

# id value of second Integer object with different name declaration with same value
integer_variable_2=10
print("id value of integer_variable_2: {}".format(id(integer_variable_2)))

# id value of Integer object with different name declaration with same value
integer_variable_1=11
print("id value of integer_variable_1 {}".format(id(integer_variable_1)))

# string object:

# id vaue of initial object declaration
string_variable='viki'
print("value of string variable  : {}".format(id(string_variable)))

# id value of second String object with different name declaration with same value
string_variable_1='viki'
print("value of string variable_1  : {}".format(id(string_variable_1)))

# id value of string object with different name declaration with same value
string_variable_after='guru'
print("value of string variable_after  : {}".format(id(string_variable_after)))

# Boolean object:

# id vaue of initial object declaration
Boolean_variable=True
print("value of Boolean variable  : {}".format(id(Boolean_variable)))

# id value of second Boolean object with different name declaration with same value
Boolean_variable_1=True
print("value of Boolean variable_1  : {}".format(id(Boolean_variable_1)))

# id value of Boolean object with different name declaration with same value
Boolean_variable_after=False
print("value of Boolean variable_after  : {}".format(id(Boolean_variable_after)))

# Tuple object:

# id vaue of initial object declaration
tuple_variable=(1,2,3,4,'viki')
print("value of tuple_variable  : {}".format(id(tuple_variable)))

# id value of second Tuple object with different name declaration with same value
tuple_variable_1=(1,2,3,4,'viki')
print("value of tuple_variable_1  : {}".format(id(tuple_variable_1)))

# id value of Tuple object with different name declaration with same value
tuple_variable_after=(1,2,3,4,'viki','guru')
print("value of tuple_variable_after  : {}".format(id(tuple_variable_after)))