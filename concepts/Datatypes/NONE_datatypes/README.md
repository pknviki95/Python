# None - None datatypes.

- None is a special data type in Python that represents **the absence of a value or a null value**. 
- It is an object of its own datatype, the NoneType.

                None_variable=None
- None is mostly used in scenario where a object needs to be assigned and keep an address reserved or future use.

### [none_type.py](https://github.com/pknviki95/Python/tree/main/cconcepts/Datatypes/NONE_datatypes/scripts/none_type.py) - To find the none type variable using type() function:

                none_variable=None
                none_variable_1=None

                # Id of the None variable remain same as it is pointing to same object value

                print("The identity of none_variable: ",id(none_variable))
                print("The identity of none_variable_1: ",id(none_variable_1))

                print("The Type of none_variable: ",type(none_variable))

#### output:

                The identity of none_variable:  94141827290080
                The identity of none_variable_1:  94141827290080
                The Type of none_variable:  <class 'NoneType'>