class CarStore(object):
    def __init__(self):
        self.factor = Factor()
    def order(self,name):
        return self.factor.Choosecar(name)

class Factor(object):
    def  Choosecar(self,name):
            if name == "BMW":#为什么不写成self.name
                return Bmw()
            elif name =='AUDI':
                return Audi()   
class Car(object):
    def move(self):
        print '------move----'
    def stop(self):
        print '-----stop-----'

class Bmw(Car):
    pass
class Audi(Car):
    pass
      
carstore = CarStore()
car = carstore.order("BMW")
car.move()



