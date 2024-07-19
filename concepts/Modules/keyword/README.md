# Keyword() - Keyword module:

- keywords are predefined identifiers/words.
- keywords should not be used as a variable name.
- There are 36 keywords in python.
- Keywords() module to perform. operations related to keywords.
```python
            import keyword
            keyword.methods() 
```

### Limitations:

- Contains only alphabet symbols.
- All contains lower case symbols/identifiers except boolean keywords
        
     ```True``` ```False``` ```None```

- If the Reserved words are assigned case-insensitive it throws Name error

#### [keyword_nameerror.py](https://github.com/pknviki95/Python/tree/main/concepts/Modules/keyword/keyword_nameerror.py) - If the keywords are not declared in proper case sensitive it throws error- Name error:

```python

x=false

# Python case sensitive ; if keyword declared with wrong case it throws Nameerror

print("Keyword with wrong case throws error: ",x)
```
#### error:

```python
Traceback (most recent call last):
  File "/home/pknviki95/Learning/Python/concepts/Modules/keyword/keyword_nameerror.py", line 5, in <module>
    x=false
NameError: name 'false' is not defined. Did you mean: 'False'?
```

#### [keyword_dir.py](https://github.com/pknviki95/Python/tree/main/concepts/Modules/keyword/keyword_dir.py) - To get the list of methods and attributes from keyword module using dir() function:
```python
import keyword

# dir(keyword) - list all attributes of keyword

print("List of attributes in keyword module: ",dir(keyword))
```
#### output:
```python
List of attributes in keyword module:  ['__all__', '__builtins__', '__cached__', '__doc__', '__file__', '__loader__', '__name__', '__package__', '__spec__', 'iskeyword', 'issoftkeyword', 'kwlist', 'softkwlist']
```
### Methods of keywords Module:

- **keyword.kwlist**
- **len(keyword.kwlist)**
- **keyword.iskeyword(keyword)**

#### keyword.kwlist:

- To list all the keyword using keyword module.

#### [keyword_kwlist.py](https://github.com/pknviki95/Python/tree/main/concepts/Modules/keyword/keyword_kwlist.py) - To list all the objects in Keyword:

```python
import keyword
        
#keyword.kwlist - List all the keyword using keyword module

print("Find the list of keywords in python : ",keyword.kwlist)
```
#### output:
```python
Find the list of keywords in python :  ['False', 'None', 'True', 'and', 'as', 'assert', 'async', 'await', 'break', 'class', 'continue', 'def', 'del', 'elif', 'else', 'except', 'finally', 'for', 'from', 'global', 'if', 'import', 'in', 'is', 'lambda', 'nonlocal', 'not', 'or', 'pass', 'raise', 'return', 'try', 'while', 'with', 'yield']
```                
#### len(keyword.kwlist):

- To find the total number of keywords.

#### [keyword_len.py](https://github.com/pknviki95/Python/tree/main/concepts/Modules/keyword/keyword_len.py) -  To find the total number of keywords:

```python
import keyword

#len(keyword.kwlist) - To find the total number of keywords
        
print("Total number of keywords : {}".format(len(keyword.kwlist)))
```
#### output:
```python
Total number of keywords : 35
```
#### keyword.iskeyword(keyword):

- To find the given parameter is keyword or not.
- It returns the boolean result of parameter if it is keyword or not.

#### [keyword_iskeyword.py](https://github.com/pknviki95/Python/tree/main/concepts/Modules/keyword/keyword_iskeyword.py) - To find the given parameter is keyword or not:

```python
import keyword

input_keyword=input("Enter the keyword: ")

# keyword.iskeyword(parameter)          # It returns the boolean result of parameter if it is keyword or not.

print("The keyword is : {}".format(keyword.iskeyword(input_keyword))) 
```     

#### input:
```python
Enter the keyword: true
```
#### output:
```python
The keyword is : False
```

### Summary of keyword Module:

| **Keyword Module/attributes** | **uses** |
| :---| :--- |
| **```keyword.kwlist```** | Lists the keyword list|
| **```keyword.iskeyword(argument)```** | checks is the argument passed is keyword or not | 
