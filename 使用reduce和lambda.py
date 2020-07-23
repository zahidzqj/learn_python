from functools import reduce
a= range(10)
b = reduce(lambda x,y:x+y,a)
print(b)