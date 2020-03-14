class CarStore():

	def __init__(self,name1,type1):
		self.name1 = name1
		self.type1 = type1
	def carr(self):
		print(self.type1)
      
carstore = CarStore('polo','10')
print(carstore.name1)
carstore.carr()


'''
class Car():
	def __init__(self,make,model,year):
		#属性
		self.make1 = make
		self.model = model
		self.yaer = year
		self.licheng = 0

	def read_odometer(self):
		"""打印里程信息"""
		print(str(self.licheng))


my_new_car = Car('audi','a4',2018)
print(my_new_car.make1.title())
#my_new_car.read_odometer()
'''