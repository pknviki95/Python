'''
Program: Syntax error if updated with imaginary other base values(oct,hex,bin):
---------------------------------------------------------------------------------

- The imaginary value for complex number should be only decimal value if it is declared with other base values it throws syntax error

'''
#binary value

x=20+0b1111101011001110j 
print("X real value is:",x.real)   
print("X imaginary value is:",x.imag)

#octal value

x=20+0o123j 
print("X real value is:",x.real)   
print("X imaginary value is:",x.imag)

#hexadecimal value

x=20+0x123j 
print("X real value is:",x.real)   
print("X imaginary value is:",x.imag)



