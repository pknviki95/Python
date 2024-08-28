'''
loops with else with break statement:

- The else block just after for/while is executed only when the loop is ```NOT``` terminated by a break statement. 

syntax:

for loop with break statement condition True:


for iteration in sequence:
        if [condition=True]:
            break
else:
    # else part is not executed as condition for break is True
    statement 

for loop with break statement condition False:


for iteration in sequence:
        if [condition=False]:
            break
else:
    # else part is executed as condition for break is False
    statement 

'''
#### for loop with break statement condition True:

list_values_break_True=[2,3,60,90,500,550,250]
for iteration in list_values_break_True:
    print("current iteration value: ",iteration)
    if iteration>500:
        print(f"Current iteration value: {iteration} met condition and executes break statement")
        print("Neglects the else part as break condition =True")
        break
else:

    # else part is not executed as condition for break is True

    print(f"else part executed as break is not executed with iteration value: {iteration} as break condition =False")

#### for loop with break statement condition False:

list_values_break_False=[2,3,60,90,500,250]
for iteration in list_values_break_False:
    print("current iteration value: ",iteration)
    if iteration>500:
        print(f"Current iteration value: {iteration} met condition and executes break statement")
        print("Neglects the else part as break condition =True")
        break
else:

    # else part is executed as condition for break is False

    print(f"else part executed as break is not executed with iteration value: {iteration} as break condition =False")