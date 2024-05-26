Program-01: Here is a sample line of code that can be executed in Python:
-------------------------------------------------------------------------
    
    print("Hello, World!")
    You can just as easily store a string as a variable and then print it to stdout:

    my_string = "Hello, World!"
    print(my_string)
    The above code will print Hello, World! on your screen. Try it yourself in the editor below!
---------------------------------------------------------------------------------------------------

            if __name__ == '__main__':
            print("Hello, World!")


Program-02: print arithmetic operation for python
-------------------------------------------------------------------------

    The provided code stub reads two integers from STDIN, a and b. Add code to print three lines where:

    The first line contains the sum of the two numbers.
    The second line contains the difference of the two numbers (first - second).
    The third line contains the product of the two numbers.

-----------------------------------------------------------------------------------------------------------------------

            if __name__ == '__main__':
                a = int(input())
                b = int(input())
                
                print(a+b)
                print(a-b)
                print(a*b)



Program-03: print Division arithmetic operation for python with integer Division and Float Division:
----------------------------------------------------------------------------------------------------
    
    The provided code stub reads two integers, a and b, from STDIN.

    Add logic to print two lines. The first line should contain the result of integer division,  a// b. The second line should contain the result of float division, a / b.

    No rounding or formatting is necessary.

    Example


    The result of the integer division 3//5=0.
    The result of the float division is 3/5-0.6.

-------------------------------------------------------------------------------------------------------------------------------------------

            if __name__ == '__main__':
                a = int(input())
                b = int(input())
                
                print(a//b)    #integer division
                print(float(a/b)) # float division


Program-04: print output based on the if-else condition :
----------------------------------------------------------------------------------------------------

    Given an integer,n , perform the following conditional actions:

    If n is odd, print Weird
    If n is even and in the inclusive range of 2 to 5, print Not Weird
    If n is even and in the inclusive range of 6 to 20, print Weird
    If n is even and greater than 20, print Not Weird

------------------------------------------------------------------------------------------------------------------------------------------------------

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


Program-05: print output based on the input with range() function:
----------------------------------------------------------------------------------------------------
    
    The included code stub will read an integer, , from STDIN.

    Without using any string methods, try to print the following:
    123...n

    Note that "..." represents the consecutive values in between.

    Example
    3
    Print the string 123.

--------------------------------------------------------------------------------------------------------------------------------------------

            if __name__ == '__main__':
                n = int(input())
                for i in range(1,n+1):      #range(n) (i.e) 0 to n-1 ; so added +1 to get the required range 
                    print(i,end='')         # print(end='') -> it determine the end of priniting by default it is '\n'

Program-06: print square value output based on the input with range() function:
----------------------------------------------------------------------------------------------------

    The provided code stub reads and integer,n , from STDIN. For all non-negative integers i<n, print i**2 .

    Example

    The list of non-negative integers that are less than n=3 is [0,1,2]. Print the square of each number on a separate line.

------------------------------------------------------------------------------------------------------------------------------------------------------

            if __name__ == '__main__':
                n = int(input())
                for i in range(0,n):        #loop using for for range fn
                    print(i**2)             # square value