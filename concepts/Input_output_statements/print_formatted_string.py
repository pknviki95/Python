'''
print() with formatted string using % operator:

- print() function with formatted string is used to print output statements based on the type of variables.
- formatted string s are declared with ```%``` operator.

syntax:

        print("% formatted string" %[variable])

'''

integer_variable=29
float_variable=85.5
string_variable='viki'

# %i - Integer/decimal value ; %f - Default float value ; %s - string variable

print("I am %s, I am %i Years old, And I weigh about with default float %f" %(string_variable,integer_variable,float_variable))

# %i - Integer/decimal value ; %.[number of decimal point value]f - Default float value ; %s - string variable

print("I am %s, I am %i Years old, And I weigh about without default float %.2f" %(string_variable,integer_variable,float_variable))