# Keyword() - Keyword module:

- keywords are **predefined identifiers/words**
- keywords should not be used as a **variable name.**
- There are **36 keywords** in python
- **Keywords() module to perform operations related to keywords.**

                import keyword
                keyword.keyword_objects()      
## Limitations:

- Contains only **alphabet symbols**
- All contains **lower case symbols/identifiers except boolean keywords**
        **True False None**
- If the Reserved words are assigned case-insensitive it throws **Name error**

#### error:

        Traceback (most recent call last):
        File "/home/pknviki95/pknviki/study/python/Python/concepts/Datatypes/Boolean_datatypes/Boolean_type.py", line 5, in <module>
            x=false
        NameError: name 'false' is not defined
        
## Objects of keywords Module:

- **keyword.kwlist**
- **len(keyword.kwlist)**
- **keyword.iskeyword(keyword)**

## keyword.kwlist:

- **To list all the objects in keyword module**

### [keyword_kwlist.py](https://github.com/pknviki95/Python/tree/main/concepts/Modules/keyword/keyword_kwlist.py) - To list all the objects in Keyword:

        import keyword
        
        #keyword.kwlist - List all the objects of keyword module

        print("Find the list of keywords in python : ",keyword.kwlist)
#### output:

                Find the list of keywords in python :  ['False', 'None', 'True', 'and', 'as', 'assert', 'async', 'await', 'break', 'class', 'continue', 'def', 'del', 'elif', 'else', 'except', 'finally', 'for', 'from', 'global', 'if', 'import', 'in', 'is', 'lambda', 'nonlocal', 'not', 'or', 'pass', 'raise', 'return', 'try', 'while', 'with', 'yield']
## len(keyword.kwlist):

- **To find the total number of keywords**

### [keyword_len.py](https://github.com/pknviki95/Python/tree/main/concepts/Modules/keyword/keyword_len.py) -  To find the total number of keywords:

        import keyword

        #len(keyword.kwlist) - To find the total number of keywords
        
        print("Total number of keywords : {}".format(len(keyword.kwlist)))
#### output:
        Total number of keywords : 35
## keyword.iskeyword(keyword):

- To find the **given parameter is keyword or not**
- It returns **the boolean result of parameter if it is keyword or not**.

### [keyword_iskeyword.py](https://github.com/pknviki95/Python/tree/main/concepts/Modules/keyword/keyword_iskeyword.py) - To find the given parameter is keyword or not:

        import keyword
        input_keyword=input("Enter the keyword: ")
        # keyword.iskeyword(parameter)          # It returns the boolean result of parameter if it is keyword or not.
        print("The keyword is : {}".format(keyword.iskeyword(input_keyword)))      
#### output:
        Enter the keyword: true
        The keyword is : False



