'''
- It throws Type error as second argument in complex() function should not be a string; only first argument of complex function supports string varibale**

            (i.e) complex('real variable')  

'''


# String to complex value with real variable and imaginary variable - Type error:
#--------------------------------------------------------------------------------

str_real_value='10.5'
str_img_value='20'

#complex value by including real_value+img_valuej - It throws Type error as second argument in complex() function should not be a string
print("str converted to complex real value and imaginary value: {}".format(complex(str_real_value,str_img_value)))