a = [1,2,3,4,2]
b = [1,2,3,4,5]
c = {1,2}
d = {'age':12}
print(d['age'])
print(type(d))
r1 = set(range(5))
a1 = set(a)
b1 = set(b)
print(a1 | b1)#并集
print(a1 & b1)#交集
print(len(a1 & b1))
a1.add(6)

print(a1)
a1.remove(6)#元素不存在，会抛出keyerror
print(a1)
a1.discard(99)#元素不存在，不会抛出异常
a1.pop()#从第一个元素移除
print(a1)
a1.__iter__()