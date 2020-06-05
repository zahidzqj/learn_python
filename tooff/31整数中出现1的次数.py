# -*- coding:utf-8 -*-
# 遍历1到n，然后求包含1的整数个数

class Solution:
    def NumberOf1Between1AndN_Solution(self, n):
        result = 0
        for num in range(1,n+1):
            while num != 0:
                if num%10 == 1:
                    result += 1
                num = num//10
        return result

a = Solution()
b = a.NumberOf1Between1AndN_Solution(11)
print(b)
