# -*- coding:utf-8 -*-

'''
把数组分为两部分，组合起来
'''
class Solution:
    def reOrderArray(self, array):
        res1 = []
        res2 = []
        for i in array:
            if i%2==1:
                res1.append(i)
            else:
                res2.append(i)
        array = res1 + res2
        return array
a = Solution()
print(a.reOrderArray([1,2,3,4]))
