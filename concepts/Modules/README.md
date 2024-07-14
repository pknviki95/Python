# Modules:

- A Python module is **a file containing Python definitions and statements.** 
- A module can define **functions, classes, and variables. A module can also include runnable code.**
- **Grouping related code into a module makes the code easier to understand and use.** 
- It also makes the code **logically organized.**
- It mainly helps with code **reusability**.

#### Syntax:

#### To import module:

                import [module name]

#### To import functions from module:

                import [module name]
                [module.name].[function name]

###  To import variable declared from module:       

                import [module name]
                [module.name].[variable name]

### Example for Module with Explanation:

- **"module_dmath.py" - File declared with functions and variable to use as module in other main program**
- **"module_main.py" - Import module_dmath module declared and call its functions and variables inside file and perform operations defined inside module_dmath.py using modules concept**

### [module_dmath.py](https://github.com/pknviki95/Python/tree/main/concepts/Modules/scripts/module_dmath.py) - File declared with functions and variable to use as module in other main program:

                # Function to add two values

                def add_fn(a,b):
                    return a+b

                # Function to Subtract two values

                def diff_fn(a,b):
                    return a-b

                # string variable

                string='viki'

### [module_main.py](https://github.com/pknviki95/Python/tree/main/concepts/Modules/scripts/module_main.py) - To Import modules declared and call its functions and variables inside other python file :

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

#### output:

                module_dmath.add_fn():  3
                module_dmath.diff_fn():  1
                module_dmath.variable:  viki

## Various ways of declaring modules:

|S.no|Declaration Types| Description|
|:--|:--| :--|
|1.|**import [module name]<br><br># module function/variable call <br><br>[module name].[function/variable name]**|  **- It imports module t the program <br> - To access the individual functions or variable we need to use below syntax <br> [module name].[function/variable name]**|
|2.|**from [module name] import [function/variable]<br><br># module function/variable call <br><br>[function/variable name]** |**- It imports specific function/variable declared in module using "from" keyword <br> - To access this functions and variable using below syntax <br><br> [function/variable name] <br><br> - PVM directly access specific function or variable inside that module <br> - No need of declaring <br> [module name].[function/variable name]** |
|3.|**from [module name] import \*<br><br># module function/variable call <br><br>[function/variable name]** |**- It imports all function/variable declared in module using "from" keyword <br> - To access this functions and variable using below syntax <br><br> [function/variable name] <br><br> - PVM directly access function or variable inside that module <br> - No need of declaring <br> [module name].[function/variable name]** |

### [module_import_nameerror.py](https://github.com/pknviki95/Python/tree/main/concepts/Modules/scripts/module_import_nameerror.py) - importing of specific function and variable and using function/variable not imported causes error - Name error:

                # importing only add_fn from module_dmath module

                from module_dmath import add_fn

                # using function that is imported returns value

                sum_value=add_fn(3,2)

                print("add_fn(): ",sum_value)

                # using function that is not imported throws - Name error

                diff_value=diff_fn(3,2)

                print("diff_fn(): ",diff_value)
#### output:
                add_fn():  5

#### error:

                Traceback (most recent call last):
                File "/home/pknviki95/Learning/Python/concepts/Modules/scripts/module_import_nameerror.py", line 17, in <module>
                    diff_value=diff_fn(3,2)
                NameError: name 'diff_fn' is not defined
#### Explanation:

- **Importing specific function/variable declared in module using "from" keyword**
- **function that is imported returns value**
- **function that is not imported throws - Name error**