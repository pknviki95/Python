Reserved words:
--------------- 

- It is a reserved words which should not be used as a variable name 
- There are 36 reserved words in python 

List of keywords in python:
---------------------------

        ['False', 'None', 'True', '__peg_parser__', 'and', 'as', 'assert', 'async', 'await', 'break', 'class', 'continue', 'def', 'del', 'elif', 'else', 'except', 'finally', 'for', 'from', 'global', 'if', 'import', 'in', 'is', 'lambda', 'nonlocal', 'not', 'or', 'pass', 'raise', 'return', 'try', 'while', 'with', 'yield'] 

Objects of keywords Module:
----------------------------

        kwlist
        iskeyword(keyword)

kwlist:
-------
- To list all the objects in keyword module

 Program: To list all the objects in Keyword:
 --------------------------------------------

        import keyword
        
        #keyword.kwlist - List all theobjects of keyword module

        print("Find the list of keywords in python : ",keyword.kwlist)

-----------------------------------------------------------------

len(keyword.kwlist):
--------------------
- To find the totalnumber of keywords

Program: To find the total number of keywords:
----------------------------------------------

        import keyword

        #len(keyword.kwlist) - To find the total number of keywords

        print("Total number of keywords : {}".format(len(keyword.kwlist)))
iskeyword(keyword):
-------------------

- To find the given parameter is keyword or not
- It returns the boolean result of parameter if it is keyword or not.

 Program: To find the given parameter is keyword or not:
 -------------------------------------------------------



        import keyword

        input_keyword=input("Enter the keyword: ")

        # keyword.iskeyword(parameter) -> It returns the boolean result of parameter if it is keyword or not.
        
        print("The keyword is : {}".format(keyword.iskeyword(input_keyword)))      

-----------------------------------------------------------------



