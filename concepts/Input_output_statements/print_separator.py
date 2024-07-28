'''
separator attribute:

- separator specifies how to separate the objects, if there is more than one. 
- By default separator  is ```' '```

            print(sep='')
'''


# Multiple objects input:

x,y,z=10,20,30

# Default separator '':

print("printing with default separator(''):",x,y,z)

# Separator can be changed using sep='<value>'

print("printing by changing default separator(','):",x,y,z,sep=',')