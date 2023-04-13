# os.makedirs("parent_dir/child_dir")  -> To create the parent and child directories it is similar to mkdir -p in linux

import os

print("List diretories of Modules: {}".format(os.listdir("../")))
os.makedirs("/home/pknviki95/pknviki/study/python/python_study/Modules/sys")
print("List diretories of Modules after parent directory: {}".format(os.listdir("../")))