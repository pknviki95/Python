'''
Program to Check if a String is Palindrome or Not

'''


string_input=input("Enter the string: ")


def is_palindrome(string_input):
    if string_input==string_input[::-1]:
        print("string_input: ",string_input)
        print("reverse string: ",string_input[::-1])
        return "Is Palindrome"
    else:
        return "Not palindrome"


string_value=is_palindrome(string_input)
print(string_value)