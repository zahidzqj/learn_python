#coding:utf-8
class Sweetpotato:
    def __init__(self):
        self.cookedString = "生的"
        self.cookedLevel = 0
        self.condiments = []

    def __str__(self):
        return "地瓜 状态：%s(%d)我加了味道%s"%(self.cookedString,self.cookedLevel,str(self.condiments))

    def cook(self, cooktime):
        self.cookedLevel += cooktime
        if self.cookedLevel >= 0 and self.cookedLevel < 3:
            self.cookedString = "生的"
        elif self.cookedLevel >= 3 and self.cookedLevel < 5:
            self.cookedString = "半生不熟"
        elif self.cookedLevel >= 5 and self.cookedLevel < 8:
            self.cookedString = "熟了"
        elif self.cookedLevel>8:
            self.cookedString = "烤糊了"   
    def add_tiaowei(self,item):
        self.condiments.append(item)
hongshu = Sweetpotato()
print(hongshu)

hongshu.cook(1)
print(hongshu)
hongshu.cook(1)
print(hongshu)
hongshu.add_tiaowei("大蒜")
hongshu.cook(1)
print(hongshu)
hongshu.cook(1)
print(hongshu)
hongshu.add_tiaowei("酱")
hongshu.cook(1)
print(hongshu)
hongshu.cook(1)
print(hongshu)
hongshu.cook(1)
print(hongshu)
hongshu.add_tiaowei("辣椒")
hongshu.cook(1)
print(hongshu)
hongshu.cook(1)
print(hongshu)
