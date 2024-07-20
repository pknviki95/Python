'''
Program-4: Write a Python program that calculates the area of a circle based on the radius entered by the user.

Sample Output :
r = 1.1
Area = 3.8013271108436504

'''

from math import pi 

radius_input=eval(input("Enter radius of the circle: "))

# Area of circle = πr^2

area_of_circle=pi*(radius_input**2)

print("Area of circle= ",area_of_circle)