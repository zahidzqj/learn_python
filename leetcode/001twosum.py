# coding: utf-8
'''
给定一个整数数组 nums 和一个目标值 target，请你在该数组中找出和为目标值的那 两个 整数，并返回他们的数组下标。
'''

class Solution(object):
    def twoSum(self, nums, target):
        dic = {}
        for i, num in enumerate(nums):
            if num in dic:
                return [dic[num], i]#词典中第一个数的值和当前数的索引值
            else:
                dic[target - num] = i
if __name__ == '__main__':
	a = Solution()
	print(a.twoSum([2,7,11,15],9))