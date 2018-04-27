#-*-coding:utf-8 -*-
nnn=input("请输入: ")#输入要加引号
if nnn.isalpha ():
	print('ok')

if nnn.isdigit():
	print('number ')

if nnn.isalnum():
	print('number+alpha ')
else :
	print('no alpha+number')	
