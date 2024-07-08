# Basic-1:

## Program-01: [print_multistring_escape.py](https://github.com/pknviki95/Python/tree/main/practices/w3_resources/Basic-1/print_multistring_escape.py) - Write a  Python program to print the following string in a specific format using Escape characters.


    Sample String : "Twinkle, twinkle, little star, How I wonder what you are! Up above the world so high, Like a diamond in the sky. Twinkle, twinkle, little star, How I wonder what you are"

    Expected Output :

                    Twinkle, twinkle, little star,
                        How I wonder what you are! 
                            Up above the world so high,   		
                            Like a diamond in the sky. 
                    Twinkle, twinkle, little star, 
                        How I wonder what you are
----------------------------------------------------------------------------------------------------------------------------------

                # sring print using escape character (\n,\t)

                print("Twinkle, twinkle, little star, \n\tHow I wonder what you are! \n\tUp above the world so high, \n\tLike a diamond in the sky. \nTwinkle, twinkle, little star, \n\tHow I wonder what you are")
#### output:

                Twinkle, twinkle, little star, 
                        How I wonder what you are! 
                                Up above the world so high, 
                                Like a diamond in the sky. 
                Twinkle, twinkle, little star, 
                        How I wonder what you are

## Program-06: [gen_userinput_list_tuple.py](https://github.com/pknviki95/Python/tree/main/practices/w3_resources/Basic-1/gen_userinput_list_tuple.py) - Write a Python program that accepts a sequence of comma-separated numbers from the user and generates a list and a tuple of those numbers.

    Sample data : 3, 5, 7, 23

    Output :
    List : ['3', ' 5', ' 7', ' 23']
    Tuple : ('3', ' 5', ' 7', ' 23')
-----------------------------------------------------------------------------------------------

                comma_sep_numbers=input("Enter the sequence of comma-separated numbers : ")

                # Converting user input to list using split():

                user_list= comma_sep_numbers.split(',')

                print("List: ",user_list)
                print("Tuple: ",tuple(user_list))

#### output:

                Enter the sequence of comma-separated numbers : 3, 5, 7, 23
                List:  ['3', ' 5', ' 7', ' 23']
                Tuple:  ('3', ' 5', ' 7', ' 23')