# keyword.iskeyword(parameter) -> It returns the boolea result of parameter if it is keyword or not.

import keyword

input_keyword=input("Enter the keyword: ")
print("The keyword is : {}".format(keyword.iskeyword(input_keyword)))

