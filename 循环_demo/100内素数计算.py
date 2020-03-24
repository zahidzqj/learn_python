
list=[]
for i in range (2,100):
    #j=2
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
