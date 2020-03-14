 #-*-coding:utf-8 -*-
print('='*50)
print('my choose game  v4')
print('1:please choose 	num: ')
print('2:  exit ')
print('='*50)

while True:
	num=int(input("please enter your menu value: "))
	if num == 1:
		import random
		player=int(input('enter your choose: '))
		cp=random.randint(0,2)
		#.randint生成整数
		if (player==0 and cp==2) or (player==1 and cp==0)or  (player==2 and cp ==1):	
			print('win win')
		elif player==cp:
			print("agine")
		else  :
			print('byebye')
	elif num ==2:
			break					
	else:
		print("please enter  agine")
