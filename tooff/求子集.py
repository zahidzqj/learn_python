#集合a子集：转为2进制
'''
0 [] --> 00
1 [1] --> 01
2 [2] --> 10
3 [1, 2] --> 11
0移位%2==0   1移位0个%2=1  2移位1个%2=1 3移位0、1个%2=1
a[移位数]=要求的一个子集-->[[], [0], [1], [0, 1]]
'''
def PowerSetsBinary(x):  
    N = len(x)   
    set_all=[]
    for i in range(2**N):
        combo = []  
        for j in range(N):
            if(i >> j ) % 2:#用来判断二进制数的下标为j的位置的数是否为1 
                #print('i=',i,'j=',j)
                combo.append(x[j]) 
        #print(combo)
        set_all.append(combo)
    return set_all
print(PowerSetsBinary([0,1]))