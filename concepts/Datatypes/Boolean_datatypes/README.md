# bool() - boolean type:

- Boolean – bool() is to determine the given value is True or False
- It can be determined if the given input exists , condition is valid or etc.,

            True,False
                
NOTE:
    - Always the declaration of boolean values should be **True** and **False**
    - if declared as **true** and **false** it throws error in python

### Error:

        Traceback (most recent call last):
        File "/home/pknviki95/pknviki/study/python/Python/concepts/Datatypes/Boolean_datatypes/Boolean_type.py", line 5, in <module>
            x=false
        NameError: name 'false' is not defined

| Boolean type | value    | Description  |
| :---:   | :---: | :---: |
| **True** | 1   | By default the value is 1 - True valid declaration |
| :---:   | :---: | :---: |
| **False**| 0    | By default the value is 0 - False valid declaration|

### Program: To find the Boolean type variable using type() function:


            x=True 
            print("X value is:",x)   
            print("The type of x is: ",type(x))
----------------------------------------------------------------------------------

### Program: To find the Boolean return type of variable when condition is invoked:

            x=10
            y=20
            z=x>y 
            print("Z value is:",z)   
            print("The type of x is: ",type(x))
-------------------------------------------------------------------------------

### Program: To find the arithmetic value of two boolean input:

            x=True              # By default True=1 ; False=0
            y=False
            z=x+y               # z=1+0=1    
            print("Z value is:",z)   
            print("The type of x is: ",type(x))
-------------------------------------------------------------------------------

NOTE:
    - In matematical expression by default
            **True=1** 
            **False=0**

