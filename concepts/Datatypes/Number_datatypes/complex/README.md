# complex() -complex datatypes:

- complex type is a number combination of  **real and imaginary part**
- complex can be represented with **real+imagj (i.e) 10+12j**
- Complex datatypes are mostly used in **mathematical operations,complex calculation etc.**

            complex_variable = real_variable+[imaginary_variable]j

#### NOTE:
- **imaginary part should always be j/J; if used anyother alphabet it throws error**

### [complex_img_j_error.py](https://github.com/pknviki95/Python/tree/main/concepts/Datatypes/Number_datatypes/complex/scripts/complex_img_j_error.py) - imaginary part should always be j/J if not it throws error - Syntax error:

            # if used anyother alphabet used in imaginary part it throws error

            x=11+12i
            print("X value is:",x)
#### error:
         File "/home/pknviki95/Learning/Python/concepts/Datatypes/Number_datatypes/complex/scripts/complex_img_j_error.py", line 1
            x=11+12i 
                  ^
         SyntaxError: invalid decimal literal
### [complex_type.py](https://github.com/pknviki95/Python/tree/main/concepts/Datatypes/Number_datatypes/complex/scripts/complex_type.py) - To find the complex type variable using type() function:

            x=11+12j 
            print("X value is:",x)   
            print("The type of x is: ",type(x))
#### output:
         X value is: (11+12j)
         The type of x is:  <class 'complex'>
### [complex_type.py](https://github.com/pknviki95/Python/tree/main/concepts/Datatypes/Number_datatypes/complex/scripts/complex_type.py) - To display the real and imaginary part individually:

            x=11+12j 
            print("X real value is:",x.real)   
            print("X imaginary value is:",x.imag)
#### output:
         X real value is: 11.0
         X imaginary value is: 12.0

### [complex_arithmetic.py](https://github.com/pknviki95/Python/tree/main/concepts/Datatypes/Number_datatypes/complex/scripts/complex_arithmetic.py) - To perform arithmetic operation for complex numbers:

### Addition

            x=11+12j
            y=20+40j
            z=x+y 
            print("X+Y value is:",z)
#### output:
         X+Y value is: (31+52j)

### Multiplication

            x=11+12j
            y=20+40j
            z=x*y 
            print("X*Y value is:",z) 
#### output:
         X*Y value is: (-260+680j)

### Division

            x=11+12j
            y=20+40j
            z=x/y 
            print("X/Y value is:",z)
#### output:         
         X/Y value is: (0.35-0.1j)
## Limitation of complex number declaration:

- The real value of complex number can be a **decimal value,float value,octal,hexadecimal,binary values**
- **The imaginary value for complex number should be only decimal value if it is declared with other base values it throws syntax error**

| Example | description | Allowance |
| :---:   | :---: | :---: |
| **x=10+20j** | **decimal values on both real and imag** | **Allowed** |
| **x=10.5+20.5j** | **float values on both real and imag** |**Allowed** |
| **x=0x123+20j** | **hex values 0n real and decimal value on imaginary (same applies for other bases)**| **Allowed** |
| **x=20+0x123j** | **decimal value on real and hex value on imag** |**Not Allowed** |

### [complex_limitation.py](https://github.com/pknviki95/Python/tree/main/concepts/Datatypes/Number_datatypes/complex/scripts/complex_limitation.py) - if updated with imaginary other base values(oct,hex,bin) - Syntax error :

### binary value:

            x=20+0b1111101011001110j 
            print("X real value is:",x.real)   
            print("X imaginary value is:",x.imag)

### octal value:

            x=20+0o123j 
            print("X real value is:",x.real)   
            print("X imaginary value is:",x.imag)

### hexadecimal value:

            x=20+0x123j 
            print("X real value is:",x.real)   
            print("X imaginary value is:",x.imag)

#### error:

         File "/home/pknviki95/Learning/Python/concepts/Datatypes/Number_datatypes/complex/scripts/complex_limitation.py", line 10
            x=20+0b1111101011001110j 
                                 ^
         SyntaxError: invalid binary literal