'''
importing of specific function and variable and using function/variable not imported causes error - Name error:

'''


# importing only add_fn from dmath module

from module_dmath import add_fn

sum_value=module_dmath.add_fn(3,2)

print("module_dmath.add_fn(): ",sum_value)

# using function that is not imported throws - Name error

diff_value=module_dmath.diff_fn(3,2)

print("module_dmath.diff_fn(): ",diff_value)