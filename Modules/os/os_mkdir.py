# os.mkdir("dir_name") - To create new directory in current working directory

import os

print("list the directories content in current working Directory: {}".format(os.listdir()))

os.mkdir("os_mkdir_test")

print("list the directories content in current working Directory after mkdir(): {}".format(os.listdir()))
