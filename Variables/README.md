Identifiers: 
------------

- Identifiers refers to naming in python  

- It can be 

		Variable name 

		Class name 

		Method name 

Name types:
-----------
- Variable
		
		X=10 

- class
		
		class test:

- function/method 

		def function_name():

Variables: 
---------
  

- Variable are used to store values in reserved memory location. 

- No explicit declaration of data types is needed for variable 

	(i.e) int x; -> This is not required 

	Hence python is Dynamically typed programming 

		x=10 -> it automatically take x as integer 

		Y=4.5 -> float 

		Z=5+4j -> complex 


Naming Rules: 
-------------

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
