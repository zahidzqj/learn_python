#http://pythontutor.makerbean.com/visualize.html

class IntList(object):
	"""docstring for IntList"""
	def __init__(self):
		self.first = None
		self.rest = None
		
l1 = IntList()
l2 = IntList()
l3 = IntList()

l1.first = 5
l2.first = 10
l3.first = 15

l1.rest = l2
l2.rest = l3

print(l1.first)#l1.first
print(l1.rest.first)#l2.first
print(l1.rest.rest.first)#l3.first
