'''
range() - Range datatypes:

- Range Datatype is **Sequence of numbers (i.e) number in range** 
- Range Datatype is **immutable (i.e) Its values cannot be Updated or changed** 
- Range can be accessed using **index value (i.e) Indexing/Slicing is possible** 

        range_variable=range(number)

            # number - sequence of number from 0 to n-1

- Range can be accessed based on **specific range values**.
        
        range_variable=range(begin number,end number,step)

            # begin number - sequence of number to start
            # end number - sequence of number to end end=n-1
            # step - sequence of number in specific steps

'''

range_variable=range(10)
print("The type of range_variable : ",type(range_variable))
