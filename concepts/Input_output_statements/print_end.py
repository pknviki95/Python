'''
end attribute:

- end specifies values to print at the end. 
- By default end attribute is \n (line feed).
- print() function always has end attribute print(end='\n')
- (i.e) print() is equivalent to print(end='\n')

            print(end='\n')
'''

# Default end '\n':

print("Hello")

# print() equivalent to print(end='\n')

print()
print("GoodMorning!!!")

# end can be changed using end='<value>'

# Empty end attribute:

print("Hello",end='')               

# end attribute ('\t'):

print("GoodMorning!!!",end='\t')
print("How are you")