#coding=utf-8
test2 = lambda a,b:a-b
result2 = test2(11,22)#调用匿名函数
print(result2)

infors = [{"name":"laowang","age":21},{"name":"xiaoming","age":20},{"name":"banzhang","age":21}]
infors.sort(key=lambda x:x['age'])
print(infors)

def test_sum(a,b,func):
    result = func(a,b)
    return result
num1 = test_sum(11,22,lambda x,y:x+y)
print(num1)


def test(a,b,func):
    result = func(a,b)
    return result
#python2中的方式
func_new = input("请输入一个匿名函数:")#lambda a,b:a*b

#python3中的方式
#func_new = input("请输入一个匿名函数:")
#func_new = eval(func_new)

num = test(11,22,func_new)
print(num)


