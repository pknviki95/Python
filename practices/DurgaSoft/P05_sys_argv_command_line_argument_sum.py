'''
Program-05: Write a  program to get sum of given number passed as an arguments

            py <script> <sum of arguments>

'''

import sys

print("List elements of sys.argv variable: ", sys.argv)

print("length of sys.argv: ",len(sys.argv))

sum_value=0

for index_value in sys.argv[1:]:
    sum_value+=int(index_value)
print("sum of argv values {}'s output = {}".format(sys.argv[1:],sum_value))