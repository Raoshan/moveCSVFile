import os
import shutil
src = os.path.join('C:/Users/RDATS/Desktop/Projects/Data/')
dest = os.path.join('C:/Users/RDATS/Desktop/Projects/backupData/')
files = os.listdir(src)
print(files)
files.sort()
for file in files:
    src1 = src + file
    dst = dest + file
    shutil.move(src1,dst)
