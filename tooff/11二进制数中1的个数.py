# -*- coding:utf-8 -*-
#print(bin(3).count('1'))#内置函数
'''
如果一个整数不为0，那么这个整数至少有一位是1。如果我们把这个整数减1，那么原来处在
整数最右边的1就会变为0，原来在1后面的所有的0都会变成1(如果最右边的1后面还有0的话)。
其余所有位将不会受到影响。
把原数和减去1之后的结果做与运算，从原来整数最右边一个1那一位开始所有位都会变成0
'''
class Solution:
    def NumberOf1(self, n):
        # write code here
        count = 0
        if n < 0:#n小于0时会无限循环
            n = n & 0xffffffff
        while n!= 0:
            count += 1
            n = (n-1)& n
        return count
a = Solution()
print(a.NumberOf1(2))
