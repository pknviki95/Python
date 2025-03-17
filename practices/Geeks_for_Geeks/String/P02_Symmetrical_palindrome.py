'''
program to check whether the string is Symmetrical or Palindrome
'''

string_input=input("Enter the string: ")
half_str=len(string_input)//2
first_half=string_input[:half_str]
second_half=string_input[half_str:] if len(string_input)%2==0 else string_input[half_str+1:]
def is_symmetrical(string_input):
    if first_half==second_half[::-1]:
        return "Symmetrical"
    else:
        return "Not Symmetrical"

def is_palindrome(string_input):
    if string_input==string_input[::-1]:
        print("string_input: ",string_input)
        print("reverse string: ",string_input[::-1])
        return "Is Palindrome"
    else:
        return "Not palindrome"


string_value_palindrome=is_palindrome(string_input)
string_value_Symmetrical=is_symmetrical(string_input)
print(string_value_Symmetrical)
print(string_value_palindrome)