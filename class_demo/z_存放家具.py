
#coding:utf-8
class Home:
    def __init__(self, new_area,new_inf,new_addr):
        self.area = new_area
        self.inf = new_inf
        self.addr = new_addr
        self.left_area = new_area
        self.contain_item = []
    def __str__(self):
        msg = "房子的总面积是%d,可用面积是：%d,房型是：%s位于%s"%(self.area,self.left_area,self.inf,self.addr)
        msg += "家具有：%s"%(str(self.contain_item))
        return msg
    def add_item(self,item):
        #self.left_area -= item.area 
        #self.contain_item.append(item.name)
        self.left_area -= item.get_area()
        self.contain_item.append(item.get_name())
class Bed:
    def __init__(self, new_name,new_area):
        self.name = new_name
        self.area = new_area
    def __str__(self):
        bed_msg = "%s的大小是：%d"%(self.name ,self.area) 
        return bed_msg   
    def get_area(self):
        return self.area
    def get_name(self):
        return self.name    
fangzi = Home(120,"三室一厅","南阳理工")
print(fangzi)

bed1 = Bed("席梦思",4)
print bed1

fangzi.add_item(bed1)
print fangzi

bed2 = Bed("沙发",3)
fangzi.add_item(bed2)
print fangzi
issubclass(Home,Bed)#内建函数判断两个类的父子关系
