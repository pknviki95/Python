## w3 resources programs:

### Basic-1:

#### Program-01: [print_multistring_escape.py](https://github.com/pknviki95/Python/tree/main/practices/w3_resources/Basic-1/print_multistring_escape.py) - Write a  Python program to print the following string in a specific format using Escape characters.
```

Sample String : "Twinkle, twinkle, little star, How I wonder what you are! Up above the world so high, Like a diamond in the sky. Twinkle, twinkle, little star, How I wonder what you are"

Expected Output :

        Twinkle, twinkle, little star,
            How I wonder what you are! 
                Up above the world so high,   		
                Like a diamond in the sky. 
        Twinkle, twinkle, little star, 
            How I wonder what you are
```

```python
# sring print using escape character (\n,\t)

print("Twinkle, twinkle, little star, \n\tHow I wonder what you are! \n\tUp above the world so high, \n\tLike a diamond in the sky. \nTwinkle, twinkle, little star, \n\tHow I wonder what you are")
```
#### output:

```python
Twinkle, twinkle, little star, 
        How I wonder what you are! 
                Up above the world so high, 
                Like a diamond in the sky. 
Twinkle, twinkle, little star, 
        How I wonder what you are
```

#### Explanation:
- ```Escape characters (\)``` tells the interpreter that this character has a special meaning to perform specific operation.
- ```\n``` - New line to move the specific line to new line
- ```\t``` - It moves to 2 spaces in same line

#### Program-06: [gen_userinput_list_tuple.py](https://github.com/pknviki95/Python/tree/main/practices/w3_resources/Basic-1/gen_userinput_list_tuple.py) - Write a Python program that accepts a sequence of comma-separated numbers from the user and generates a list and a tuple of those numbers.
```
    Sample data : 3, 5, 7, 23

    Output :
    List : ['3', ' 5', ' 7', ' 23']
    Tuple : ('3', ' 5', ' 7', ' 23')
```

```python
comma_sep_numbers=input("Enter the sequence of comma-separated numbers : ")

# Converting user input to list using split():

user_list= comma_sep_numbers.split(',')

print("List: ",user_list)
print("Tuple: ",tuple(user_list))
```

#### output:

```python
Enter the sequence of comma-separated numbers : 3, 5, 7, 23
List:  ['3', ' 5', ' 7', ' 23']
Tuple:  ('3', ' 5', ' 7', ' 23')
```
#### Explanation:

- String input is converted to list using ```split()``` function.
- ```str.split(',')``` function separated string input  str ```3,5,7,23``` into list ```['3', ' 5', ' 7', ' 23']``` based on separator as comma(,).
- ```tuple(list_variable)``` typecast list value to tuple.

#### Program-8: [print_1st_last_list_element.py](https://github.com/pknviki95/Python/tree/main/practices/w3_resources/Basic-1/print_1st_last_list_element.py) - Write a Python program to display the first and last colors from the following list.
```
    color_list = ["Red","Green","White" ,"Black"]
```

```python
color_list = ["Red","Green","White" ,"Black"]

# Indexing on elements of list first element index is always 0 (positive indexing); Last element index is always -1 (Negative indexing)
print("The first color in color_list is {} and last colors in color_list is {}".format(color_list[0],color_list[-1]))
```

#### output:

```python
The first color in color_list is Red and last colors in color_list is Black
```
#### Explanation:

- Indexing is a process of accessing specific elements of the sequence.
- Indexing on elements of list first element index is always ```0 (positive indexing)```; Last element index is always ```-1 (Negative indexing)```
- ```variable[0]``` - first element ; ```variable[-1]``` - last element