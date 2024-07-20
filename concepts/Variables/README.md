# Identifiers: 

- Identifiers refers to naming in python.  
- It can be 

	- **Variable name**
	- **Class name**
	- **Method name**

### Types of identifiers:

#### Variable/objects:
		
```python
X=10 
```

#### class:
		
```python
class test:
```

#### function/method: 

```python
def function_name():
```
### Variables/objects: 

- Variable are used to store values in reserved memory location. 

- No explicit declaration of data types is needed for variable 

```c
int x;  // This is not required 
```
- Hence python is Dynamically typed programming 

```python
x=10  # it automatically take x as integer 

Y=4.5 # float 

Z=5+4j # complex 
```

### Naming Rules of variable: 

- Variable length can be of anything.
	
```python
q=10
xyz='viki'
qewfev=2+4j 
```

- Identifier names should start with an alphabet or underscore(_) followed by zero or more letters, underscores and digits.

|**Variable Declaration** | **correct/Incorrect**| Description |
|:---	| :---|:---|
|```x=10``` | correct | Integer variable x assigned to value x| 
|```_x=10``` | correct| underscore(_) can be used as start of variable name|
|```x_=10``` | correct| underscore(_) can be used as end of variable name|
|```_12=10``` | correct|underscore(_) can be used as start of numbered variable name|
|```@xyz=10``` | Incorrect| special characters are not allowed as start of variable name except underscore(_) |
| ```x yz=10``` | Incorrect | Spaces are not allowed in between variable names|
| ```class = 10``` | Incorrect| Reserved words are ot allowed|

- No other special characters are allowed. 

- Identifier names are case sensitive. 
	
```python
x=10
# Returns NONE as it is case sensitive
print(X) 
``` 
- Reserved words should not be used as a variable.
```python
# 36 reserved words in python
class = 10
sum =20
```
- Spaces are not allowed.
```python
# Incorrect
x yz=10 
```

### Reserved words:
 
- Reserved words are predefined identifiers/words
- It is a reserved words which should not be used as a variable name
- There are 36 reserved words in python 

### List of Reserved words in python:

| Types     | Reserved                                             |
|:--- | :--- |
| **Boolean**   | ```True```  ```False```  ```None``` |
| **Operator**  | ```and``` ```or```  ```not```  ```is``` ```in``` |
| **loops** | ```while```  ```for```  ```break```  ```continue```  ```return```   ```yield``` |
| **conditions**   | ```if``` ```else```  ```elif``` |
| **exceptions**   | ```try```  ```except```  ```finally```  ```raise```  ```assert``` |
| **Modules**   | ```import```  ```from```  ```as```  ```class```  ```def``` ```pass``` |
| **variables**   | ```global```  ```nonlocal```  ```lambda```  ```del```  ```with``` |

### Examples of variable with different datatype declaration:

#### [variables.py](https://github.com/pknviki95/Python/tree/main/concepts/Variables/variables.py) - Examples of variable with different datatypes declaration:

#### Integer Datatype:

```python
integer_variable=10
print("value of integer variable  : {} ; type of variable  : {}".format(integer_variable,type(integer_variable)))
```
#### output:
```python
value of integer variable  : 10 ; type of variable  : <class 'int'>
```

#### String Datatype:

```python
string_variable='viki'
print("value of string variable  : {} ; type of variable  : {}".format(string_variable,type(string_variable)))
```
#### output:
```python
value of string variable  : viki ; type of variable  : <class 'str'>
```

#### Boolean Datatype:

```python
Boolean_variable=True
print("value of Boolean variable  : {} ; type of variable  : {}".format(Boolean_variable,type(Boolean_variable)))
```
#### output:
```python
value of Boolean variable  : True ; type of variable  : <class 'bool'>
```

#### List Datatype:

```python
list_variable=[1,2,3,4,'viki']
print("value of list_variable  : {} ; type of variable  : {}".format(list_variable,type(list_variable)))
```
#### output:
```python
value of list_variable  : [1, 2, 3, 4, 'viki'] ; type of variable  : <class 'list'>
```

#### Tuple Datatype:

```python
tuple_variable=(1,2,3,4,'viki')
print("value of tuple_variable  : {} ; type of variable  : {}".format(tuple_variable,type(tuple_variable)))
```
#### output:
```python
value of tuple_variable  : (1, 2, 3, 4, 'viki') ; type of variable  : <class 'tuple'>
```

#### Dictionary Datatype:

```python
dictionary_variable={1:'viki',2:'Raj','Vijay':30}
print("value of dictionary_variable  : {} ; type of variable  : {}".format(dictionary_variable,type(dictionary_variable)))
```
#### output:
```python
value of dictionary_variable  : {1: 'viki', 2: 'Raj', 'Vijay': 30} ; type of variable  : <class 'dict'>
```

#### Set Datatype:

```python
set_variable={1,2,3,4,'viki'}
print("value of set_variable  : {} ; type of variable  : {}".format(set_variable,type(set_variable)))
```
#### output:

```python
value of set_variable  : {1, 2, 3, 4, 'viki'} ; type of variable  : <class 'set'>
```


### Immutable and Mutable Objects:

#### Mutable object:

- Mutable objects are those that allow you to change their value or data in place without affecting the object's identity.
- Even if any changes is made on objects the identity of objects doesn't change.
- Mutable objects are as below
	- **List**
	- **Set**
	- **Dictionary**
	- **Bytearray**
	- **Array**

#### [Mutable_identity.py](https://github.com/pknviki95/Python/tree/main/concepts/Variables/Mutable_identity.py) - To find the identity of Mutable objects using id() function:

#### List object:

```python
# id value of initial object declaration
list_variable_1=[1,2,3,4,'viki']
print("id value of list_variable_1: {}".format(id(list_variable_1)))

# id value of second list object with different name declaration with same value
list_variable_2=[1,2,3,4,'viki']
print("id value of list_variable_2: {}".format(id(list_variable_2)))

# id value of list object with different name declaration with same value
list_variable_after=[1,2,3,4,'guru']
print("id value of list_variable_after: {}".format(id(list_variable_after)))
```
#### output:
```python
id value of list_variable_1: 140225086531072
id value of list_variable_2: 140225086608128
id value of list_variable_after: 140225086847424
```
#### Dictionary object:

```python
# id value of initial object declaration 
dictionary_variable_1={1:'viki',2:'Raj','Vijay':30}
print("id value of dictionary_variable_1  : {} ".format(id(dictionary_variable_1)))

# id value of second Dictionary object with different name declaration with same value
dictionary_variable_2={1:'viki',2:'Raj','Vijay':30}
print("id value of dictionary_variable_2  : {} ".format(id(dictionary_variable_2)))

# id value of Dictionary object with different name declaration with same value
dictionary_variable_after={1:'viki',2:'Raj','Vijay':30,3:'guru'}
print("id value of dictionary_variable_after  : {} ".format(id(dictionary_variable_after)))
```
#### output:
```python
id value of dictionary_variable_1  : 140225086531520 
id value of dictionary_variable_2  : 140225086531776 
id value of dictionary_variable_after  : 140225086531584
```
#### set object:

```python
# id vaue of initial object declaration 
set_variable_1={1,2,3,4,'viki'}
print("value of set_variable_1  : {}".format(id(set_variable_1)))

# id value of second set object with different name declaration with same value
set_variable_2={1,2,3,4,'viki'}
print("value of set_variable_2  : {}".format(id(set_variable_2)))

# id value of set object with different name declaration with same value
set_variable_after={1,2,3,4,'viki',5}
print("value of set_variable_after  : {}".format(id(set_variable_after)))
```
#### output:
```python
value of set_variable_1  : 140225086758400
value of set_variable_2  : 140225086760640
value of set_variable_after  : 140225086760416
```

#### What is happening in background on mutable object?

- In All above Scenario the address of the object/variable is different in all scenario referring to mutable objects. 
- (i.e) id changes if the change are made in values - Different id's for mutable objects even though their values are same.
- New objects are created for all declarations like the output below 

- In this scenario three objects are created where ```set_variable_1```,```set_variable_2``` with ```same value``` and ```set_variable_after``` with ```different value```		
- Same object value with different object name

	```set_variable_1``` ```{1,2,3,4,'viki'}```	```140225086758400```

	```set_variable_2``` ```{1,2,3,4,'viki'}``` ```140225086760640```			

- Different object name with Different value 

	```set_variable_after``` ```{1,2,3,4,'viki',5}``` ```140225086760416```

```
	All returns different identity as it is Mutable objects
```

- Even though the ```set_variable_1,set_variable_2``` have same value unlike the Immutable objects the Python virtual machine doesn't point to same identity of object instead it creates new objects for all.

#### Immutable object:

- Immutable objects are those that doesn't allow you to change their value or data in place.
- If any changes is made in the object then the identity of that object changes
- Immutable objects are as below
	- **Integer**
	- **Float**
	- **Strings**
	- **Boolean**
	- **Range**
	- **Frozenset**
	- **Tuples**
	- **Byte**

####  [Immutable_identity.py](https://github.com/pknviki95/Python/tree/main/concepts/Variables/Immutable_identity.py) - To find the identity of immutable objects using id() function:

#### Integer object:

```python
# id vaue of initial object declaration
integer_variable_1=10
print("id value of integer_variable_1  : {}".format(id(integer_variable_1)))

# id value of second Integer object with different name declaration with same value
integer_variable_2=10
print("id value of integer_variable_2: {}".format(id(integer_variable_2)))

# id value of Integer object with different name declaration with same value
integer_variable_1=11
print("id value of integer_variable_1 {}".format(id(integer_variable_1)))
```
#### output:
```python
value of integer_variable_1  : 139756882100752
id value of integer_variable_2: 139756882100752
id value of integer_variable_1 139756882100784
```

#### string object:

```python
# id vaue of initial object declaration
string_variable='viki'
print("value of string variable  : {}".format(id(string_variable)))

# id value of second String object with different name declaration with same value
string_variable_1='viki'
print("value of string variable_1  : {}".format(id(string_variable_1)))

# id value of string object with different name declaration with same value
string_variable_after='guru'
print("value of string variable_after  : {}".format(id(string_variable_after)))
```

#### output:
```python
value of string variable  : 139849127621488
value of string variable_1  : 139849127621488
value of string variable_after  : 139849127621808
```

#### Boolean object:

```python
# id vaue of initial object declaration
Boolean_variable=True
print("value of Boolean variable  : {}".format(id(Boolean_variable)))

# id value of second Boolean object with different name declaration with same value
Boolean_variable_1=True
print("value of Boolean variable_1  : {}".format(id(Boolean_variable_1)))

# id value of Boolean object with different name declaration with same value
Boolean_variable_after=False
print("value of Boolean variable_after  : {}".format(id(Boolean_variable_after)))
```
#### output:
```python
value of Boolean variable  : 94724538307616
value of Boolean variable_1  : 94724538307616
value of Boolean variable_after  : 94724538307584
```
#### Tuple object:

```python
# id vaue of initial object declaration
tuple_variable=(1,2,3,4,'viki')
print("value of tuple_variable  : {}".format(id(tuple_variable)))

# id value of second Tuple object with different name declaration with same value
tuple_variable_1=(1,2,3,4,'viki')
print("value of tuple_variable_1  : {}".format(id(tuple_variable_1)))

# id value of Tuple object with different name declaration with same value
tuple_variable_after=(1,2,3,4,'viki','guru')
print("value of tuple_variable_after  : {}".format(id(tuple_variable_after)))
```
#### output:
```python
value of tuple_variable  : 139849131587152
value of tuple_variable_1  : 139849131587152
value of tuple_variable_after  : 139849127464960
```

#### What is happening in background on Immutable object?

- In this scenario three objects are created where ```integer_variable_1```,```integer_variable_2``` with **same value** and ```integer_variable_after``` with ```different value```
			
- same object value with different object name

	```integer_variable_1``` ```10``` ```139756882100752```

	```integer_variable_2```				  ```10```	```139756882100752```			

- same object name with different value 

	```integer_variable_1``` ```11``` ```139756882100784```
```
	The Same value objects returns same identity as PVM points to same object

	Same object name with different value returns different identity 
```
- The ```integer_variable_1,"integer_variable_2``` object have same value. 
- Python virtual machine in background checks if value is assigned to any objects that are assigned already then it just points the new object to same object location which inturn same identity for Immutable objects.
- If the object name ```integer_variable_1``` assigned again with different value then new object with new identity is created since it is Immutable objects. 
- (i.e) Any objects with same value will be considered as same objects even though it has different object names by PVM.


### Difference Between Mutable and Immutable Data Type: Mutable vs Immutable

| S.no | Mutable | Immutable |
| :--- | :--- | :--- |
|Definition|	Data type whose values can be changed after creation.	|Data types whose values can’t be changed or altered.|
|Memory Location	| Retains the same memory location even after the content is modified.|	Any modification results in a new object and new memory location|
|Example	| List, Dictionaries, Set ,	Bytearray, Array| Integer, Float, Strings, Boolean, Frozenset, Tuples, Byte, Range |
|Performance|	It is memory-efficient, as no new objects are created for frequent changes.|	It might be faster in some scenarios as there’s no need to track changes.|
|Thread-Safety|	Not inherently thread-safe. Concurrent modification can lead to unpredictable results. |	They are inherently thread-safe due to their unchangeable nature.|
|Use-cases|	When you need to modify, add, or remove existing data frequently.	| When you want to ensure data remains consistent and unaltered.|

### Escape characters:

- An escape character is a character followed by a ```backslash (\)```. 
- It tells the Interpreter that this escape character (sequence) has a special meaning.


|Escape Character |	Meaning | Description |
| :---: | :---: | :---: |
|```\’```|	Single quote| It helps to use single quotes inside string |
|```\”```|	Double quote | It helps to use Double quotes inside string |
|```\``` | backslash | It helps to use backslash inside string |
|```\n``` 	|New line| It helps to print the string in new line |
|```\r```	|Carriage Return| It helps to move the changes to beginning of the same line |
|```\t```	|Horizontal tab| It helps to move the changes to tab (2 spaces) of the line |
|```\b```	|Backspace|  It helps to delete the changes one character back of the line |
|```\f```	|form feed| It helps to move to the next page |
|```\v```	|vertical tab| It helps to move the change to vertical tab.** |
|```\0```	|Null character|
|```\N{name}```	|Unicode Character Database named Lookup|
|```\uxxxxxxxx```|	Unicode Character with 16-bit hex value XXXX|
|```\Uxxxxxxxx```|	Unicode Character with 32-bit hex value XXXXXXXX|
|```\ooo```	|Character with octal value OOO|
|```\xhh```	|Character with hex value HH|

####  [escape_character.py](https://github.com/pknviki95/Python/tree/main/concepts/Variables/escape_character.py) - Escape character and its applications:

#### \’	- Single quote:

- It helps to use single quotes inside string.

```python
# \’	- Single quote:

# It helps to use single quotes inside string
print('Hello! \'Good Morning!!!\'')
```
#### output:
```python
Hello! 'Good Morning!!!'
```

#### \ "	- Double quote:

- It helps to use Double quotes inside string.

```python
# \"	- Double quote:

# It helps to use Double quotes inside string
print('Hello! \"Good Morning!!!\"')
```
#### output:
```python
Hello! "Good Morning!!!"
```

#### \	- backslash:

- It helps to use backslash inside string.
- Mainly used in declaring path as string.

```python
# \	- backslash

# It helps to use backslash inside string - Mostly on path usage

print('C:\\Program Files\\norton\\appx')
```
#### output:
```python
C:\Program Files\norton\appx
```

#### \n	- New line:

- It helps to print the string in new line.
				
```python
# \n	- New line
		
# It helps to print the change in new line
print('Hello!\nWelcome to India')
```
#### output:
				Hello!
				Welcome to India

#### \r	- Carriage Return:

- It helps to move the changes to beginning of the same line.
				
```python
# \r	- Carriage Return

# It helps to print the change in beginning of same line
print('Hello!\rWelcome to India')
```	
#### output:
```python
Welcome to India
```

#### \t	- Horizontal tab:

- It helps to move the change to horizontal tab (2 spaces) of same line.

```python
# \t	- Horizontal tab	

# It helps to move the change to horizontal tab (2 spaces) of same line
print('Hello!\tWelcome to India')
```
#### output:
```python
Hello!  Welcome to India
```

#### \b	- Backspace:		

-  It helps to remove the one character back ; perform backspace operation.
				
```python
# \b	- Backspace		

# It helps to remove the change; perform backspace operation
print('Hello!\bWelcome to India')
```
#### output:
```python
HelloWelcome to India
```

#### \v	- vertical tab:	
- It helps to move the change to vertical tab.

```python
# \v	- vertical tab	

# It helps to move the change to vertical tab.
print('Hello!\vWelcome to India')
```
#### output:
```python
Hello!
		Welcome to India
```

### comments:

- Comments can be used to explain Python code.
- Comments can be used to make the code more readable.
- Comments can be used to prevent execution when testing code.
 - ```#``` is used to comment the single line.
 - Python doesn't have explicit multi-line comment.          
                
```python
                # [single-line comment]
```

#### How to declare comments?:

- ``#`` is used to declare a comment so below print statement is not executed.

###  [comments.py](https://github.com/pknviki95/Python/tree/main/concepts/Variables/comments.py) - Comments declaration and its purpose:

```python
	# This is single-line comment

	# "#" is used to comment so below print operation doesn't execute

	# print("Hello!")
```

### Constants:

- Constants concepts is not applicable in python.
- Python doesn't support constants
- Every variable/objects in python can be declared and changed.
