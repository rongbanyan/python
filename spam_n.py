# coding:utf-8
"""
在一些连续编号的文件中，空出一些编号，
以便加入新的文件。
"""
import os
import random
m = [3,4,6,25,21,15,34]
for i in range(50):
    filename = "ce\\spam_%03d.txt" % (i+1)
    if (i+1) not in  m:
        if not os.path.exists(filename):
            f = open(filename, 'w')
            f.write('%03d' % (i+1))
            f.close()

