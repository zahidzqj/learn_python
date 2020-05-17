
# -*- coding:utf-8 -*-
class Solution:
    def jumpFloor(self, number):
        # write code here
        if number == 1:
            return 1
        elif number == 2:
            return 2
        num1 = 1
        num2 = 2
        target = num1 + num2
        for i in range(2, number-1):
            num1 = num2
            num2 = target
            target = num1 + num2
        return target
a = Solution()
re=a.jumpFloor(5)
print(re)


# 变态挑台阶，一次挑的阶数随意
class Solution1:
    def jumpFloorII(self, number):
        # write code here
        return 2**(number - 1)
a = Solution1()
jump1=a.jumpFloorII(5)
print(jump1)

