#os.chdir("path")  - It is used to change from current working directory to passed path

import os

print("The current working Directory: {}".format(os.getcwd()))

# changing to below path
os.chdir(r"C:\Users\pknviki95\Desktop\tools")

print("The current working Directory after chdir object: {}".format(os.getcwd()))