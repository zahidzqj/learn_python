__metaclass__ = type
class Bird(object):
    """docstring for Bird"""
    def __init__(self):
        self.hungry = True
    def eat(self):
        if self.hungry:
            print ('aaaaaah')
            self.hungry =False
        else:
            print ('no,thanks')    
        
class SongBird(object):
    """docstring for ClassName"""
    def __init__(self):
        super(SongBird, self).__init__()#super会查找所有的超类
        #Bird.__init__(self)#和super的效果一样
        self.sound = 'song of bird'
    def sing(self):
        print (self.sound)
ge = SongBird()
ge.sing()

bb = Bird()
bb.eat()         