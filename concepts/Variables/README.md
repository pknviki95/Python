# Identifiers: 

- Identifiers refers to naming in python  
- It can be 

		Variable name 

		Class name 

		Method name 

## Name types:

- Variable
		
		X=10 

- class
		
		class test:

- function/method 

		def function_name():

## Variables: 

- Variable are used to store values in reserved memory location. 

- No explicit declaration of data types is needed for variable 

	(i.e) int x; -> This is not required 

	Hence python is Dynamically typed programming 

		x=10 -> it automatically take x as integer 

		Y=4.5 -> float 

		Z=5+4j -> complex 


## Naming Rules: 

- Variable length can be of anything.
	
	 	q
	 	xyz
	 	qewfev 

- Identifier names should start with an alphabet or underscore(_) followed by zero or more letters, underscores and digits
	
	 	x=10 -> correct
	 	_x=10 -> correct
	 	x_=10 -> correct
	 	_12=10 -> correct
	 	@xyz=10 -> Incorrect 

- No other special characters are allowed. 

- Identifier names are case sensitive. 
	
		x=10
		print(X) -> Returns NONE as it is case sensitive

- Reserved words should not be used as a variable 

		class,sum, ->  36 reserved words in python

- Spaces should not be there 
	
	 	x yz=10 -> Incorrect


## Examples of variable with different dataypes declaration:

### Integer Datatype

		integer_variable=10
		print("value of integer variable  : {} ; type of variable  : {}".format(integer_variable,type(integer_variable)))

### String Datatype

		string_variable='viki'
		print("value of string variable  : {} ; type of variable  : {}".format(string_variable,type(string_variable)))

### Boolean Dataype

		Boolean_variable=True
		print("value of Boolean variable  : {} ; type of variable  : {}".format(Boolean_variable,type(Boolean_variable)))

### List Dataype

		list_variable=[1,2,3,4,'viki']
		print("value of list_variable  : {} ; type of variable  : {}".format(list_variable,type(list_variable)))

### Tuple Dataype

		tuple_variable=(1,2,3,4,'viki')
		print("value of tuple_variable  : {} ; type of variable  : {}".format(tuple_variable,type(tuple_variable)))

### Dictionary Dataype

		dictionary_variable={1:'viki',2:'Raj','Vijay':30}
		print("value of dictionary_variable  : {} ; type of variable  : {}".format(dictionary_variable,type(dictionary_variable)))

### Set Dataype

		set_variable={1,2,3,4,'viki'}
		print("value of set_variable  : {} ; type of variable  : {}".format(set_variable,type(set_variable)))