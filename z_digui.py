# -*- coding: utf-8 -*- 
def fact(n ):
 if n==1:
    return n #返回为1和n的区别？
 return n*fact (n-1)
print (fact (3)) 

def fact_iter(num, product):
    if num == 1:
        return product 
    return fact_iter(num - 1, num * product)
print(fact_iter(5,3))

L=[]
n =1
while n<=99:
  L.append(n)
  n=n+2
print(L)


def getNums(num):
    if num>1:
        return num * getNums(num-1)
    else:
        return num

result = getNums(4)
print(result)
#print (getNums(4)) 


def test(n):
    if n>1:
        print("&"*10)
        print(n)
        return n*test(n-1)
    else:
        print("="*10)
        print(n)
        return n
    

s=test(4)
print(s)