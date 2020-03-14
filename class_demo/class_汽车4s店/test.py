class CarStore(object):
    def choosecar(self,name):
        #self.name=name
        if name == "BMW":#为什么不写成self.name
            return Bmw()
        elif name =='AUDI':
            return Audi()   
class Car(object):
    def move(self):
        print ('------move----')
    def stop(self):
        print ('-----stop-----')

class Bmw(Car):
    pass
class Audi(Car):
    pass
      
carstore = CarStore()
car = carstore.choosecar("BMW")
car.move()




