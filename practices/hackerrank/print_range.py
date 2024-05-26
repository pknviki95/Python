'''
The included code stub will read an integer, , from STDIN.

Without using any string methods, try to print the following:
123...n

Note that "..." represents the consecutive values in between.

Example
3
Print the string 123.

'''

if __name__ == '__main__':
    n = int(input())
    for i in range(1,n+1):      #range(n) (i.e) 0 to n-1 ; so added +1 to get the required range 
        print(i,end='')         # print(end='') -> it determine the end of priniting by default it is '\n'