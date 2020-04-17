'''
100内素数求和
当迭代的对象迭代完并为空时，位于else的子句将执行，而如果在for循环中含有break时则直接终止循环，并不会执行else子句。
'''

list=[]
for i in range (2,100):
    for j in range(2,i):
        if(i%j==0):
            break
    else:
        list.append(i)
print(list)
print(sum(list))


from math import sqrt
N = 100
sum1  = 0
list = [p for p in range(2,N) if 0 not in [p % d for d in range(2,int(sqrt(p)) + 1)]]
print(sum(list))









