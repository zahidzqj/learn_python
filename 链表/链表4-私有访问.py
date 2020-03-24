#http://pythontutor.makerbean.com/visualize.html

class IntNode:
 	"""docstring for IntNode"""
 	def __init__(self, i, n):
 		self.item = i
 		self.next = n

class SLList:
 	"""docstring for SLList"""
 	def __init__(self, x):
 		self.__first = IntNode(x,None)#self.first相当于第一节车厢
 		self.__size = 1

 	def add_first(self, x):#add第一节车
 		self.__first = IntNode(x, self.__first)
 		self.__size += 1

 	def add_last(self,x):
 		p = self.__first
 		while p.next is not None:
 			p = p.next
 		p.next = IntNode(x,None)
 		self.__size += 1

 	def get_first(self):#查看第一节车
 		return self.__first.item

 	def size(self):
 		return self.__size


l = SLList(10)
print(l.get_first())
l.add_first(15)
print(l.get_first())
l.add_first(20)
print(l.get_first())
l.add_last(5)
print(l.size())

l._SLList__first.item = 8#修改第一个值
print(l.get_first())