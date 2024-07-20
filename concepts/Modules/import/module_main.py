'''
To Import modules declared and call its functions and variables inside other python file :

'''

#### To import module:

import module_dmath

#### To import functions from module:

# [module.name].[function name]

sum_value=module_dmath.add_fn(1,2)
print("module_dmath.add_fn(): ",sum_value)

diff_value=module_dmath.diff_fn(3,2)
print("module_dmath.diff_fn(): ",diff_value)

# [module.name].[variable name]
print("module_dmath.variable: ",module_dmath.string)