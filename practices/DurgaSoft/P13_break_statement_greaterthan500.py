'''
Program-13: Write a  program to break from loop using break statement if cart value exceeds more than 500:

'''

cart_value={'milk':28,'sugar':10,'vegetables':240,'lotion':550,'toothpaste':40}

for iteration in cart_value.values():
    print("Current iteration value: ",iteration)
    if iteration>500:
        print(f"Executing the break statement inside loop as {iteration} is greater than 500")
        break
print(f"outside the loop as {iteration} value")