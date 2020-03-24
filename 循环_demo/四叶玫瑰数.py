'''
四叶玫瑰数是4位数的自幂数。自幂数是指一个n位数，它的每个位上的数字的 n 次幂之和等于它本身。（例如：当n为3时，
有1^3 + 5^3 + 3^3 = 153，153即是n为3时的一个自幂数，3位数的自幂数被称为水仙花数）
'''

for i in range(1000,10000):
  a = int(i/1000)
  b = int(i%1000/100)
  c = int(i%100/10)
  d = int(i%10)
  if pow(a,4)+pow(b,4)+pow(c,4)+pow(d,4)==i:
    print(i)

for i in range(100,1000):
  a = int(i/100)
  b = int(i%100/10)
  c = int(i%10)
  if pow(a,3)+pow(b,3)+pow(c,3)==i:
    print(i)