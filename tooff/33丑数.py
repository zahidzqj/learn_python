'''
生成第K个丑数（质因子只有2,3,5）。建立一个set，从1开始，
依次保存和1,2,3分别相乘后值，取较小的值作为下一个丑数，
同时从set中去掉已经作为丑数的这个数。
[2 3 5 4 6 10 9 15.......]
'''

# -*- coding:utf-8 -*-
class Solution:
# 运行时间：28ms
# 占用内存：5856k
    def GetUglyNumber_Solution(self, index):
        # write code here
        if index == 0:
            return 0
        count = 1
        result = 1
        ugly_list = set()
        while count < index:
            ugly_list.add(2*result)
            ugly_list.add(3*result)
            ugly_list.add(5*result)
            result = min(ugly_list)
            ugly_list.remove(result)
            count += 1
        return result
a = Solution()
b = a.GetUglyNumber_Solution(15)
print(b)
