#print ('hello,world7')
class ClassName(object):
	"""docstring for ClassName"""
	def __init__(self, new_name,new_age):
		#super(ClassName, self).__init__()
		self.name = new_name
		self.age = new_age
	def function1(self):
		print("老鼠在厨房。。。。")	
	def function2(self):
		print("老鼠在睡觉。。。。")	
	def function3(self):
		print("%s is %d years old\n"%(self.name,self.age))	

jack = ClassName("JACK",30)
#print(tom)#可以改用str的方式
jack.function1()
jack.function2()
#jack.name = "jack"
#jack.age = 30
jack.function3()


class Cat:
    #属性
    #方法
    def eat(self):
        print("猫在吃鱼....")

    def drink(self):
        print("猫正在喝kele.....")

    def introduce(self):
        print("%s的年龄是:%d"%(tom.name, tom.age))
#创建一个对象
tom = Cat()
#调用tom指向的对象中的 方法
tom.eat()
tom.drink()
#给tom指向的对象添加2个属性
tom.name = "汤姆"
tom.age = 40

#获取属性的第1种方式
#print("%s的年龄是:%d"%(tom.name, tom.age))
tom.introduce()
