'''
- **Importing specific function/variable declared in module using "from" keyword**
- **function that is imported returns value**
- **function that is not imported throws - Name error**
'''


# importing only add_fn from dmath module

from module_dmath import add_fn

# using function that is imported returns value

sum_value=add_fn(3,2)

print("add_fn(): ",sum_value)

# using function that is not imported throws - Name error

diff_value=diff_fn(3,2)

print("diff_fn(): ",diff_value)