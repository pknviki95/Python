'''
Limititaions:

- By default The empty declaration of variable with {} is considered as Dictionary object. To tell PVM that it is set object we need to declare set(variable)**

                set_variable={}  => By default Dictionary object
                set(set_variable) => set object

'''

# Empty varibale with {} braces
 
set_variable={}

# without set () fun returns dict
print("unordered set_variable type without set() function: {}".format(type(set_variable)))

# with set () fun returns set
print("unordered set_variable type with set() function: {}".format(type(set(set_variable))))