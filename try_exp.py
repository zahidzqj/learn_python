#
try:
    1/x
    #1/0
    #1/b
    print(2222)
except (ValueError, ArithmeticError):#错误1
    print("程序发生了数字格式异常、算术异常之一")
except:#错误2
	print("未知异常")
else :#不发生异常时执行
    print("try 正常")
finally:#一定执行
	print("程序结束")