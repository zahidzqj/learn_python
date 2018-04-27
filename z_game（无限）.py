#-*-coding:utf-8 -*-
print('='*50)
print('my game system v4')
print('please choose 0 1 2')
print('='*50)
#names=[]
while True:
	#num=int(input("please enter num: "))
	import random
	player=int(input('enter your choose: '))
	cp=random.randint(0,2)
	if (player==0 and cp==2) or (player==1 and cp==0) or  (player==2 and cp ==1):	
		print('win win')
	elif player==cp:
		print("agine")
	else  :
		print('byebye')
