#http://pythontutor.makerbean.com/visualize.html

class IntList:
	"""docstring for IntList"""
	def __init__(self, first, rest):
		self.first = first
		self.rest = rest
	
	#添加size方法看链表长度
	# def size(self):#递归的方法看size：耗费存储
	# 	if self.rest is None:
	# 		return 1
	# 	else:
	# 		return 1+self.rest.size()
	def size(self):
		p=self
		size = 1
		while p.rest is not None:#p.rest换成p，结果不同
			p= p.rest
			size += 1
		return size

l = IntList(5,None)
l = IntList(10,l)
l = IntList(15,l)
# l1 = IntList(5, None)
# l2 = IntList(10, l1)
# l3 = IntList(15, l2)

print(l.first)#l1.first
print(l.rest.first)#l2.first
print(l.rest.rest.first)#l3.first
print(l.size())	