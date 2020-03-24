#http://pythontutor.makerbean.com/visualize.html

class IntNode:
	"""docstring for IntNode"""
	def __init__(self, i, n):
		self.item = i
		self.next = n
		
class SSList:
	"""docstring for SSList"""
	def __init__(self,x):
		self.first = IntNode(x,None)
		#self.size = 1

	def add_first(self,x):
		self.first = IntNode(x,self.first)
		#self.size += 1

	def add_last(self,x):
		p =self.first
		while p.next is not None:
			p = p.next
		p.next = IntNode(x, None)	
		#self.size += 1

	def get_first(self):
		return self.first.item

	# def size(self):
	# 	return self.size#报错 int 没有callback
	def size(self):
		p = self.first
		size = 1
		while p.next is not None:
			p= p.next
			size += 1
		return size

l = SSList(10)
print(l.first.item)
l.add_first(15)
print(l.first.item)
l.add_last(5)
print(l.first.next.next.item)
print(l.get_first())

l.first.item=2#修改
print(l.size())
