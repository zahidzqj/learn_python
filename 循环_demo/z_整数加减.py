# -*- coding: utf-8 -*-
'''
1-2+3-4...100
其中，所有数字为整数，从1开始递增，奇数为正，偶数为负
'''

odd = 0
for i in range(1,100,2):
	odd+=i
even = 0
for x in range(2,100+2,2):
#for j in range(-100,0,2):
	even-=x

print(odd+even)
