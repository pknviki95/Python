# Hackerrank Programs:

#### Program-01: [P01_print_helloworld.py](https://github.com/pknviki95/Python/tree/main/practices/hackerrank/Introduction/P01_print_helloworld.py) - Here is a sample line of code that can be executed in Python:
```    
print("Hello, World!")
You can just as easily store a string as a variable and then print it to stdout:

my_string = "Hello, World!"
print(my_string)
The above code will print Hello, World! on your screen. Try it yourself in the editor below!
```

```python
if __name__ == '__main__':
print("Hello, World!")
```
#### output:
```python
Hello, World!
```
#### Explanation:
- ```print("")``` function is used to print value that is passed on screen.
- ```"Hello, World!"``` - Passed inside function prints on screen. 
#### Program-02: [P02_arithmetic.py](https://github.com/pknviki95/Python/tree/main/practices/hackerrank/Introduction/P02_arithmetic.py) -print arithmetic operation for python
```
The provided code stub reads two integers from STDIN, a and b. Add code to print three lines where:

The first line contains the sum of the two numbers.
The second line contains the difference of the two numbers (first - second).
The third line contains the product of the two numbers.

```

```python
if __name__ == '__main__':
    a = int(input())
    b = int(input())
    
    print(a+b)
    print(a-b)
    print(a*b)
```
#### input:
```python
1
2
```
#### output:
```python
3
-1
2
```
#### Explanation:
- Arithmetic operators are used to perform arithmetic operations such as ```Addition(+)```,```Subtraction(-)```,```Multiplication(*)```.
- Variable ```"a"``` and ```"b"``` performs ```addition(a+b)```,```Subtraction(a-b)```,```Multiplication(a*b)``` and returns its arithmetic values.

#### Program-03: [P03_division.py](https://github.com/pknviki95/Python/tree/main/practices/hackerrank/Introduction/P03_division.py) - Print Division arithmetic operation for python with integer Division and Float Division:

```  
The provided code stub reads two integers, a and b, from STDIN.

Add logic to print two lines. The first line should contain the result of integer division,  a// b. The second line should contain the result of float division, a / b.

No rounding or formatting is necessary.

Example


The result of the integer division 3//5=0.
The result of the float division is 3/5-0.6.
```

```python
if __name__ == '__main__':
    a = int(input())
    b = int(input())
    
    print(a//b)    #integer division
    print(float(a/b)) # float division
```
#### input:
```python
1
3
```
#### output
```python
0
0.3333333333333333
```
#### Explanation:
- ```a//b``` - ```Floor division``` returns integer or float value based on input passed; return value without decimal point if both are integer input
- ```a/b``` - ```Division``` by default always return float value (i.e) with decimal value

#### Program-04: [P04_if_else_condition.py](https://github.com/pknviki95/Python/tree/main/practices/hackerrank/Introduction/P04_if_else_condition.py) - Print output based on the if-else condition :
```
Given an integer,n , perform the following conditional actions:

If n is odd, print Weird
If n is even and in the inclusive range of 2 to 5, print Not Weird
If n is even and in the inclusive range of 6 to 20, print Weird
If n is even and greater than 20, print Not Weird
```

```python
import math
import os
import random
import re
import sys



if __name__ == '__main__':
    n = int(input().strip())

if n%2!=0:                          #If n is odd, print Weird
    print("Weird")

if n%2==0 and n>=2 and n<=5:        #If n is even and in the inclusive range of 2 to 5, print Not Weird
    print("Not Weird")

if n%2==0 and n>=6 and n<=20:       #If n is even and in the inclusive range of 6 to 20, print Weird
    print("Weird")
    
if n%2==0 and n>20:                 #If n is even and greater than 20, print Not Weird
    print("Not Weird")
```
#### input:
```python
15
```
#### output
```python
Weird
```
#### Explanation:

**combination of logical operators and relational:**

- ```n%2==0``` - ```Modulo operator``` if reminder value is zero it is even number - print "Weird"
- ```n%2==0 and n>=2 and n<=5``` - If n is even ;n greater than or equal to 2 and  n lesser than and equal to 5 - print "Not Weird"  
- ```n%2==0 and n>=6 and n<=20``` - If n is even ;n greater than or equal to 6 and  n lesser than and equal to 20 - print "Weird"
- ```n%2==0 and n>20``` - If n is even ;n greater than 20 - print "Not Weird" 
#### Program-05: [P05_print_range.py](https://github.com/pknviki95/Python/tree/main/practices/hackerrank/Introduction/P05_print_range.py) - Print output based on the input with range() function:
```    
    The included code stub will read an integer, , from STDIN.

    Without using any string methods, try to print the following:
    123...n

    Note that "..." represents the consecutive values in between.

    Example
    3
    Print the string 123.
```

```python
if __name__ == '__main__':
    n = int(input())
    for i in range(1,n+1):      #range(n) (i.e) 0 to n-1 ; so added +1 to get the required range 
        print(i,end='')         # print(end='') -> it determine the end of priniting by default it is '\n'
```
#### input:
```python
5
```
#### output:
```python
12345
```
#### Explanation:
- ```range(1,n+1)``` - ranges of number from ```1 to n+1```
- ```print(end='')``` will print the values in same line 
- By default ```end=\n``` - newline in print() function.
#### Program-06: [P06_print_sqr_loop.py](https://github.com/pknviki95/Python/tree/main/practices/hackerrank/Introduction/P06_print_sqr_loop.py) - Print square value output based on the input with range() function:
```
    The provided code stub reads and integer,n , from STDIN. For all non-negative integers i<n, print i**2 .

    Example

    The list of non-negative integers that are less than n=3 is [0,1,2]. Print the square of each number on a separate line.
```

```python
if __name__ == '__main__':
    n = int(input())
    for i in range(0,n):        #loop using for for range fn
        print(i**2)             # square value
```
#### input:
```python
3
```
#### output:
```python
0
1
4
```
#### Explanation:
- Exponential operator in Arithmetic operation ```i**n``` is used to perform ```power values```
- ```i**2``` performs square for a given range of number from ```0-n```