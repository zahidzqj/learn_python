#!/usr/bin/env python3   
# -*- coding: utf-8 -*-  
#为了告诉Linux系统，这个是python可执行程序  
#为了告诉python解释器，按照utf-8编码读取源代码，否则，你在源代码中写的中文输出可能会由乱码  

def power (x,n ): 
  s=1
  while n>0:
    n=n-1
    s=s*x 
  return s 
  
print(power (5,2))

def enroll(name,gen):
 print('name',name )
 print('gen',gen)
enroll('tim','f ')

def add_end(L=[]):
  
  L.append('end')
  return L 

print(add_end([1,2,3]))
print(add_end())
print(add_end())#如果list为空，再次调用会出现两个end


def addend(L=None):
 if  L is None:
     L=[]
 L.append ('END')
 return L 
print(addend())
print(addend())

def calc(num):
  sum =0
  for n in num:
   sum=sum +n*n
  return  sum
 
print(calc([1,2,3]))
print(calc([1,3,5,7]))

def person(name, age, **kw):
    print('name:', name, 'age:', age, 'other:', kw)
print (person("tim",24))	
print(person('Bob', 35, city='Beijing'))
extra = {'city': 'Beijing', 'job': 'Engineer'}
print(person('jack',32,**extra)) 

def person(name, age, city='tokyo'):
    print('name:', name, 'age:', age, 'other:', city )
print (person("tim",24))

def f1(a, b, c=0, *args, **kw):
    print('a =', a, 'b =', b, 'c =', c, 'args =', args, 'kw =', kw)
	
print(f1(1,2))	