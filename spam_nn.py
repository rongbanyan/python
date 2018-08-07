# coding:utf-8

import os, re, shutil, zipfile
"""
编写一个程序，在一个文件夹中，找到所有带指定前缀的文件，诸如spam001.txt,
spam002.txt 等，并定位缺失的编号（例如存在spam001.txt 和spam003.txt，但不存
在spam002.txt）。让该程序对所有后面的文件改名，消除缺失的编号。
"""
filenamelist = []
reg = re.compile(r'spam_\d{3}.txt')

#从指定文件夹里找出符合要求的文件，并将文件的绝对路径放到FilenamesList里面
for folder, subfolders, filenames in os.walk("ce"):
    for x in filenames:
        if reg.search(x).group() != None:
            filenamelist.append(os.path.join(folder,x))

filenamelist.sort() #给FilenamesList排序
print(filenamelist)


#检查FilenamesList里面遗漏的文件，显示出来
num = 1
for filename in filenamelist:
    while True:
        if int(filename[-7:-4]) == num:
            break
        print ("lost spam_%03d.txt" % num)
        num += 1
    num +=1

#将所有的文件同一命名
num = 1
for x in filenamelist:
    y = x[:-7]+('%03d' % num) + '.txt'
    print (y)
    num+=1
    shutil.move(x,y)

m = 'ce\\spam_001.txt'
print (m[-7:-4])