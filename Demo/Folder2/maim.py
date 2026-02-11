import sys
import os


print(os.getcwd())
sys.path.append("~/Documents/Python/Demo/")
print(os.getcwd())

from Folder1 import add

print(add.add(1, 2))
