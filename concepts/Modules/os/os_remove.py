# os.remove("file_name") -> To remove the file in current working directory
import os

print("The current content in CWD:{}".format(os.listdir()))

os.remove("remove_test.txt")

print("The current content in CWD after removing file:{}".format(os.listdir()))