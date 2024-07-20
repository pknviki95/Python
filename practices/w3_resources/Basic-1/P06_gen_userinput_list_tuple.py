'''
Program-06: Write a Python program that accepts a sequence of comma-separated numbers from the user and generates a list and a tuple of those numbers.

Sample data : 3, 5, 7, 23

Output :
List : ['3', ' 5', ' 7', ' 23']
Tuple : ('3', ' 5', ' 7', ' 23')

'''

comma_sep_numbers=input("Enter the sequence of comma-separated numbers : ")
print(type(comma_sep_numbers))
# Converting user input to list using split():

user_list= comma_sep_numbers.split(',')

print("List: ",user_list)
print("Tuple: ",tuple(user_list))