# complex() -complex datatypes:

- complex type is a number combination of  **real and imaginary part**
- complex can be represented with real+imagj (i.e) 10+12j
- Complex datatypes are mostly used in mathematical operations,complex calculation etc.

NOTE:
   **imaginary part should always be j/J; if used anyother alphabet it throws error**

### Program: To find the complex type variable using type() function:


            x=11+12j 
            print("X value is:",x)   
            print("The type of x is: ",type(x))
-----------------------------------------------------------------------------

### Program: To display the real and imaginary part individually:

            x=11+12j 
            print("X real value is:",x.real)   
            print("X imaginary value is:",x.imag)
-----------------------------------------------------------------

### Program: To perform arithmetic operation for complex numbers:

#### Addition

            x=11+12j
            y=20+40j
            z=x+y 
            print("X+Y value is:",z)

#### Multiplication

            x=11+12j
            y=20+40j
            z=x*y 
            print("X*Y value is:",z) 

#### Division

            x=11+12j
            y=20+40j
            z=x/y 
            print("X/Y value is:",z)  
-----------------------------------------------------------------

## Limitation of complex number declaration:

- The real value of complex number can be a **decimal value,float value,octal,hexadecimal,binary values**
- **The imaginary value for complex number should be only decimal value if it is declared with other base values it throws syntax error**

| Example | description |
| :---:   | :---: |
| x=10+20j | **deciaml values on both real and imag - Allowed** |
| :---:   | :---: |
| x=10.5+20.5j | **float values on both real and imag - Allowed** |
| :---:   | :---: |
| x=0x123+20j | **hex values 0n real and decimal value on imaginary (same applies for other bases)- Allowed** |
| :---:   | :---: |
| x=20+0x123j | **decimal value on real and hex value on imag - Not allowed** |
| :---:   | :---: |

### Program: Syntax error if updated with imaginary other base values(oct,hex,bin):

#### binary value:

            x=20+0b1111101011001110j 
            print("X real value is:",x.real)   
            print("X imaginary value is:",x.imag)

#### octal value:

            x=20+0o123j 
            print("X real value is:",x.real)   
            print("X imaginary value is:",x.imag)

#### hexadecimal value:

            x=20+0x123j 
            print("X real value is:",x.real)   
            print("X imaginary value is:",x.imag)

### Error:

         cd /home/pknviki95/pknviki/study/python/Python/concepts ; /usr/bin/env /usr/bin/python3.9 /home/pknpknviki95@ubuntu18:~/pknviki/study/python/Python/concepts$  cd /home/pknviki95nsions/ms-python.debugpy-2024.6.0-linux-x64/bundled/libs/debugpy/adapter/../../debugpy/launcher 48245 -- /home/pknviki95/pknviki/study/python/Python/concepts/Datatypes/Number_datatypes/complex/complex_limitation.py 
         File "/home/pknviki95/pknviki/study/python/Python/concepts/Datatypes/Number_datatypes/complex/complex_limitation.py", line 7
         x=20+0b1111101011001110j 
                           ^
         SyntaxError: invalid syntax    