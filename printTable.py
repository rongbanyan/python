# coding:utf-8
# 表格打印

tableData = [['apples', 'oranges', 'cherries', 'banana'],
['Alice', 'Bob', 'Carol', 'David'],
['dogs', 'cats', 'moose', 'goose']]

def findmaxlen(datas):
    maxlen = 0
    for i in range(len(datas)):
        if len(datas[i]) > maxlen:
            maxlen = len(datas[i])
    return maxlen

def printTable(lists):
    k = len(lists)
    v = len(lists[0])
    for i in range(v):
        for j in range(k):
            print (lists[j][i].rjust(findmaxlen(lists[j])), end=' ')
        print ()

print (printTable(tableData))

# 方法二
def listsOp(lists):
    lens = [0]*len(lists)
    for i in range(len(lists[0])):
        for j in range(len(lists)):
            if len(lists[j][i]) > lens[j]:
                lens[j] = len(lists[j][i])
    return lens

def printTable2(lists):
    lens = listsOp(lists)
    for i in range(len(lists[0])):
        for j in range(len(lists)):
            print (lists[j][i].rjust(lens[j]), end= ' ')
        print ()


print (printTable2(tableData))