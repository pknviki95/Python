## w3 resources programs:

### Basic-1:

#### Program-01: [P01_print_multistring_escape.py](https://github.com/pknviki95/Python/tree/main/practices/w3_resources/Basic-1/P01_print_multistring_escape.py) - Write a  Python program to print the following string in a specific format using Escape characters.
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

#### Program-4: [P04_math_area_circle.py](https://github.com/pknviki95/Python/tree/main/practices/w3_resources/Basic-1/P04_math_area_circle.py) - Write a Python program that calculates the area of a circle based on the radius entered by the user.
```
Sample Output :
r = 1.1
Area = 3.8013271108436504
```
```python
from math import pi 

radius_input=eval(input("Enter radius of the circle: "))

# Area of circle = πr^2

area_of_circle=pi*(radius_input**2)

print("Area of circle= ",area_of_circle)
```
#### input:
```python
Enter radius of the circle: 1.1
```
#### output:
```python
Area of circle=  3.8013271108436504
```
#### Explanation:
- ```math module``` used to perform mathematical operations ; ```pi``` is the variable of math module.
- ```Area of circle = πr^2``` to perform equivalent python programmatically ```pi*(radius_input**2)```.
- pi value is ```3.141592653589793```
- ```(radius_input**2)``` square value of radius_input.
- ```3.141592653589793 * (1.1**2)``` - Equivalent mathematical expression fro area of circle

#### Program-06: [P06_gen_userinput_list_tuple.py](https://github.com/pknviki95/Python/tree/main/practices/w3_resources/Basic-1/P06_gen_userinput_list_tuple.py) - Write a Python program that accepts a sequence of comma-separated numbers from the user and generates a list and a tuple of those numbers.
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

#### Program-8: [P08_print_1st_last_list_element.py](https://github.com/pknviki95/Python/tree/main/practices/w3_resources/Basic-1/P08_print_1st_last_list_element.py) - Write a Python program to display the first and last colors from the following list.
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


