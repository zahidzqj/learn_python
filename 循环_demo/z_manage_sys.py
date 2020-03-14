#-*-coding:utf-8 -*-
print('='*50)
print('my manage system v4')
print('1:请添加人员')
print('2:')
print('3:')
print('4:请查找人员')
print('='*50)
names=[]
while True:
	num=int(input("张请输入数字编号： "))
	if num==1:
		num1=input('请添加姓名：')
		names.append(num1)
		print(names)
	elif num==2:
			pass	
	elif num==3:
			pass
	elif num==4:
			num2=input("请输入查员姓名")	
			if num2 in names:
				print('张有了，找到了')
			else:
				print('张系统未识别')	
	elif num==5:
			break					
	else:
		print("张输入有误，重新输入")
