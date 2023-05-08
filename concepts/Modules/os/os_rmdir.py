# os.rmdir("dir_name") -> To remove the directory from specific path or current working directory

import os

print("The current content in CWD:{}".format(os.listdir()))

os.rmdir("os_mkdir_test")

print("The current content in CWD after removing directory:{}".format(os.listdir()))