#公式计算
pi = 0
N = 100
for k in range(N) :
    pi += 1/pow(16,k)*( \
    4/(8*k+1) - 2/(8*k+4) - \
    1/(8*k+5) - 1/(8*k+6))
print("圆周率值是: {}".format(pi))


#蒙塔卡罗方法
from random import random
from time import perf_counter
DARTS = 1000*1000
#撒点的数量1000000
hits = 0.0
#在圆内的点数

start = perf_counter()
#开始计时
for i in range(1, DARTS+1):
    x, y = random(), random()
    #圆为1*1大小 
    dist = pow(x ** 2 + y ** 2, 0.5)
    #点到圆心的距离
    if dist <= 1.0:
        hits = hits + 1
pi = 4 * (hits/DARTS)
print("圆周率值是: {}".format(pi))
print("运行时间是: {:.5f}s".format(perf_counter()-start))
