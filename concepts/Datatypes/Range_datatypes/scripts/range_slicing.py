'''
Slicing:

- Sequence of range elements can be accessed using slicing

                    # start index - By default it is 0 ; This can be changes based on requirement
                    # end index - Last index value len(variable)-1
                    # step  - Sequence of number in specific index steps

'''
sequence = range(10)

#Positive Index slicing

#variable[start index:end index] 
print('Positive variable[start index:end index]: ',sequence[2:6]) 

#variable[:end index] - By default start index is index 0 so it is equivalent to variable[0:end index]
print('Positive variable[:end index]: ',sequence[:6])

#variable[start index:] - By default end index is last element index so it is equivalent to variable[start index:end index]
print('Positive variable[start index:]: ',sequence[2:])      

#variable[:] - Based on above default values it is equivalent to variable
print('Positive variable[:]: ',sequence[:])

#variable[start index:end index:step] - It returns from index 1->3->5 (start+2(step) till end index value)
print('Positive variable[start index:end index:step]: ',sequence[1:6:2])

#Negative Index slicing

#variable[start index:end index] - Here the start index/end index is equivalent negative index value of positive index
print('Negative variable[start index:end index]: ',sequence[-6:-2])  

#variable[:end index] - By default start index is index 0 equivalent negative index
print('Negative variable[:end index]: ',sequence[:-3])         

#variable[start index:] - Here the start index is equivalent negative index value of positive index
print('Negative variable[start index:]: ',sequence[-7:])        

#variable[start index:end index:step] - It returns from index 1->3->5 (start+3(step) till end index value)
print('Negative variable[start index:end index:step]: ',sequence[-7:-2:3])