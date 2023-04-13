# os.stat("file/dir")  -> It returns the status of file or directory passed as a parameter it is like stat command in linux


import os

print("The status of file/directory: {}".format(os.stat("os_stat.py")))