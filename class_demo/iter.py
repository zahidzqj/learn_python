class C:
 
    def __iter__(self):
        return iter('123')
 
obj = C()
for item in obj: 
    print(item)


class game(object):
	"""docstring for game"""
	num = 1#类属性
	def __init__(self,name,age):
		self.name = name
		self.age = age
	def pri_name(self):
		print("name is %s,and age is %d" % (self.name,self.age))
	@classmethod#使用类方法
	def change_num(cls):#
		cls.num = 100

	@staticmethod#使用静态方法
	def pri_menu():
		print('over')

gg = game('tom',12)
print(gg.num)
gg.pri_name()
gg.change_num()
print(gg.num)
gg.pri_menu()
