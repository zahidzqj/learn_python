#-*-coding:utf-8 -*-
import os

L=[]
for x in range(1,11):
    L.append(x*x)
print(L)
#上下写法效果一样    
[x*x for x in range(1,11)]

[m + n for m in 'ABC' for n in 'XYZ']

[d for d in os.listdir('.')]
#列出当前目录下的所有文件和目录名:先调用import os

d = {'x': 'A', 'y': 'B', 'z': 'C' }
for k, v in d.items():
    print(k, '=', v)
#for循环其实可以同时使用两个甚至多个变量，
    #比如dict的items()可以同时迭代key和value：

def mulu():
    print('='*5,'show all','='*5)
    print([d for d in os.listdir('.')])
#os.listdir('.')列出当前目录下的所有文件和目录名:先调用import os
mulu()

LI = ['Hello', 'World', 'IBM', 'Apple']
[s.lower() for s in LI]
#list中所有的字符串变成小写


dict={'age':18,'name':'tim'}
dict.items()
dict.values()
#dict.keys(),按关键字切分成元组,组成数组
