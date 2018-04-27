#-*-coding:utf-8 -*-
print('='*50)
print('my manage system v4')
print('1:please add 	name: ')
print('2:please del  	name: ')
print('3:please print 	name: ')
print('4:please find 	name: ')
print('5:  exit ')
print('='*50)
names=[]
while True:
	num=int(input("please enter num: "))
	if num==1:
		name1=input('please add name: ')
		names.append(name1)
		#print(names)#for test
	elif num==2:
			pass	
	elif num==3:
			print('show all menbers:')
			print(names)
	elif num==4:
			name2=input("please find name: ")	
			if name2 in names:
				print('ok,I find it ')
			else:
				print('oh,nobody')	
	elif num==5:
			break					
	else:
		print("please enter  agine")
