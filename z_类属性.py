class ClassName(object):
	"""docstring for ClassName"""
	def __inaccessible(self):
	#用双下划线定义为私有性private property	
		print "private property"
	def accessible(self):
		print "the secret is"
		self.__inaccessible()
		#私有性在类的内部进行访问
tom = ClassName()
tom.accessible()
tom.__inaccessible()#外部访问 不行的
#issubclass(ClassName,accessible)#内建函数判断两个类的父子关系
