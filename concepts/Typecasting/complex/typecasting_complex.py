'''
complex()

- complex() function is used to convert other datatypes to complex type value.**

            complex(real variable,imaginary variable)

'''

# integer to complex value with real variable:
#---------------------------------------------

# Program: To convert integer datatypes to complex value using complex() for real value:

integer_value=10

#complex value by including real_value+0j
print("integer converted to complex real value: {}".format(complex(integer_value))) 

# integer to complex value with real variable and imaginary variable:
#--------------------------------------------------------------------

# Program: To convert integer datatypes to complex value using complex() for real value and imaginary value:

integer_real_value=10
integer_img_value=20

#complex value by including real_value+img_valuej
print("integer converted to complex real value and imaginary value: {}".format(complex(integer_real_value,integer_img_value)))

# float to complex value with real variable:
#--------------------------------------------

# Program: To convert float datatypes to complex value using complex() for real value:
             
float_value=10.5

#complex value by including real_value+0j
print("float converted to complex real value: {}".format(complex(float_value))) 

# float to complex value with real variable and imaginary variable:
#-----------------------------------------------------------------

### Program: To convert float datatypes to complex value using complex() for real value and imaginary value:

float_real_value=10.5
float_img_value=20.8

#complex value by including real_value+img_valuej
print("float converted to complex real value and imaginary value: {}".format(complex(float_real_value,float_img_value)))

# Boolean to complex value with real variable:
# -----------------------------------------------

# Program: To convert Boolean datatypes to complex value using complex() for real value:

bool_value=True

#complex value by including real_value+0j
print("bool converted to complex real value: {}".format(complex(bool_value)))

# Boolean to complex value with real variable and imaginary variable:
#-----------------------------------------------------------------

### Program: To convert float datatypes to complex value using complex() for real value and imaginary value:

bool_real_value=False
bool_img_value=True

#complex value by including real_value+img_valuej
print("bool converted to complex real value and imaginary value: {}".format(complex(bool_real_value,bool_img_value)))

# String to complex value with real variable:
# -----------------------------------------------

# program: To convert string datatypes to complex value using complex() for real value with base-10 :

string_value='15'

#complex value by including real_value+0j
print("str converted to complex real value: {}".format(complex(string_value))) 
