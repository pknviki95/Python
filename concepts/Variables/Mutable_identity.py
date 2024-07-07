'''
Mutable object:

- Mutable objects are those that **allow you to change their value or data in place without affecting the object's identity**
- **Even if any changes is made on objects the identity of objects doesn't change**
- Muttable objects are as below

		List
		Set
		Dictionary
		Bytearray
		Array

'''

# List object:

# id vaue of initial object declaration
list_variable_1=[1,2,3,4,'viki']
print("id value of list_variable_1: {}".format(id(list_variable_1)))

# id value of second list object with different name declaration with same value
list_variable_2=[1,2,3,4,'viki']
print("id value of list_variable_2: {}".format(id(list_variable_2)))

# id value of list object with different name declaration with same value
list_variable_after=[1,2,3,4,'guru']
print("id value of list_variable_after: {}".format(id(list_variable_after)))

# Dictionary object:

# id vaue of initial object declaration 
dictionary_variable_1={1:'viki',2:'Raj','Vijay':30}
print("id value of dictionary_variable_1  : {} ".format(id(dictionary_variable_1)))

# id value of second Dictionary object with different name declaration with same value
dictionary_variable_2={1:'viki',2:'Raj','Vijay':30}
print("id value of dictionary_variable_2  : {} ".format(id(dictionary_variable_2)))

# id value of Dictionary object with different name declaration with same value
dictionary_variable_after={1:'viki',2:'Raj','Vijay':30,3:'guru'}
print("id value of dictionary_variable_after  : {} ".format(id(dictionary_variable_after)))

# set object

# id vaue of initial object declaration 
set_variable_1={1,2,3,4,'viki'}
print("value of set_variable_1  : {}".format(id(set_variable_1)))

# id value of second set object with different name declaration with same value
set_variable_2={1,2,3,4,'viki'}
print("value of set_variable_2  : {}".format(id(set_variable_2)))

# id value of set object with different name declaration with same value
set_variable_after={1,2,3,4,'viki',5}
print("value of set_variable_after  : {}".format(id(set_variable_after)))