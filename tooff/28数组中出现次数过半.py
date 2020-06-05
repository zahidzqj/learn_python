# -*- coding:utf-8 -*-
#print(bin(3).count('1'))#内置函数
'''
数组中有一个数字出现的次数超过数组长度的一半，请找出这个数字。例如输入一个长度为9的数组{1,2,3,2,2,2,5,4,2}。
由于数字2在数组中出现了5次，超过数组长度的一半，因此输出2。如果不存在则输出0。
'''
class Solution:
    def MoreThanHalfNum_Solution(self, numbers):

        num_dict = {}
        lenght = len(numbers)
        result = 0
        for num in numbers:
            if num in num_dict:
            	num_dict[num] += 1
            else:
            	num_dict[num] = 1
            #num_dict[num] = num_dict.get(num,0)+1
            # try:
            #     num_dict[num] = num_dict[num] + 1
            # except:
            #     num_dict[num] = 1

        for key, values in num_dict.items():
            if values > lenght//2:
                result = key
        return result
a = Solution()
print(a.MoreThanHalfNum_Solution([1,1,3]))
