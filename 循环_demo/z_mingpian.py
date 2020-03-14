#-*-coding:utf-8 -*-

print('='*50)
print('my information manage system v4')
print('1:请添加一个名片')
print('2:请删除一个名片')
	print('3:请修改一个名片')
print('4:请查找一个名片')
print('='*50)
mycard=[]
while True:
	num=int(input('请输入编码： '))
	if num==1:
		name1=input('添加姓名')
		tel1=input('添加手机号')
		address1=input('添加地址')
		card1={}
		card1.append(name1,tel1,address1)
		mycard.append(card1)
		print(mycard)
	elif num==2:
				pass
	elif num==3:
				pass
	elif num==4:	
                pass
    else:
        print("输入有误，重输入")
