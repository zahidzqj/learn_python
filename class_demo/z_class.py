#coding:utf-8
class Cat:
    #属性
    def __init__(self,new_name,new_age):
    	self.name =new_name
    	self.age = new_age
    #方法
    def eat(self):
        print("猫在吃鱼....")

    def drink(self):
        print("猫正在喝kele.....")

    def introduce(self):#谁调用，self就指向谁
        #print("%s的年龄是:%d"%(tom.name, tom.age))
        print("%s的年龄是:%d"%(self.name, self.age))

#创建一个对象
#tom = Cat()
tom = Cat("汤姆",40)
#调用tom指向的对象中的 方法
tom.eat()
tom.drink()

#给tom指向的对象添加2个属性
#tom.name = "汤姆"
#tom.age = 40

#获取属性的第1种方式
#print("%s的年龄是:%d"%(tom.name, tom.age))
tom.introduce()#相当于 tom.introduce(tom)
lanmao = Cat('蓝猫',10)
#lanmao = Cat()
#lanmao.name = "蓝猫"
#lanmao.age = 10
lanmao.introduce()

'''
#私有性内部进行访问
class ClassName(object):
    """docstring for ClassName"""
    def __inaccessible(self):
    #用双下划线定义为私有性private property    
        print ("private property")
    def accessible(self):
        print ("the secret is")
        self.__inaccessible()#私有性在类的内部进行访问
tom = ClassName()
tom.accessible()
tom.__inaccessible()#外部访问 不行的
#issubclass(ClassName,accessible)#内建函数判断两个类的父子关系
'''