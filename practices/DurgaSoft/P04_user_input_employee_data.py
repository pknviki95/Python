'''
Program-04: Write a  program to get employee data as user input and print the data:
'''

# Employee user input:

Employee_Name=input("Enter Employee Name: ")
Employee_Age=int(input("Enter Employee Age: "))
Employee_salary=float(input("Enter Employee Salary: "))
Employee_Address=input("Enter Employee Address: ")

print("Employee Information: \n\nEmployee_Name: {} \nEmployee_Age: {} \nEmployee_Salary: {} \nEmployee_Address: {}".format(Employee_Name,Employee_Age,Employee_salary,Employee_Address))