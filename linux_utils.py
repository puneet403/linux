
#How do I list all files of a directory?
#you can use the os module to list all files in a directory. The os.listdir() function returns a list of all files and directories in the specified directory.

import os

files = os.listdir()
for file in files:
    print(file)
    