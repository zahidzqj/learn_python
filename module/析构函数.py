class aniaml(object):
	"""docstring for aniaml"""
	def __init__(self, name):
		self.name = name
		print('初始化')
	def __del__(self):
		print('这是析构方法,自动执行')

cat = aniaml('tom')
