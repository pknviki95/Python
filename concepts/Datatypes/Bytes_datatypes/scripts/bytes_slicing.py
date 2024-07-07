'''
Slicing:

- **Sequence of bytes elements can be accessed using slicing**

'''

sequence = [65,66,67,68,69,1,2,3]
bytes_variable=bytes(sequence)

#Positive Index slicing

#variable[start index:end index] 
print('Positive variable[start index:end index]: ',bytes_variable[2:6]) 

#variable[:end index] - By default start index is index 0 so it is equivalent to variable[0:end index]
print('Positive variable[:end index]: ',bytes_variable[:6])

#variable[start index:] - By default end index is last element index so it is equivalent to variable[start index:end index]
print('Positive variable[start index:]: ',bytes_variable[2:])      

#variable[:] - Based on above default values it is equivalent to variable
print('Positive variable[:]: ',bytes_variable[:])

#variable[start index:end index:step] - It returns from index 1->3->5 (start+2(step) till end index value)
print('Positive variable[start index:end index:step]: ',bytes_variable[1:6:2])

#Negative Index slicing

#variable[start index:end index] - Here the start index/end index is equivalent negative index value of positive index
print('Negative variable[start index:end index]: ',bytes_variable[-6:-2])  

#variable[:end index] - By default start index is index 0 equivalent negative index
print('Negative variable[:end index]: ',bytes_variable[:-3])         

#variable[start index:] - Here the start index is equivalent negative index value of positive index
print('Negative variable[start index:]: ',bytes_variable[-7:])        

#variable[start index:end index:step] - It returns from index 1->3->5 (start+3(step) till end index value)
print('Negative variable[start index:end index:step]: ',bytes_variable[-7:-2:3])