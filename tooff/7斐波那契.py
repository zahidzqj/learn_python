class Solution:
    def Fibonacci(self, n):
        # write code here
        num1 = 0
        num2 = 1
        target = 0
        for i in range(0,n):
            num1 = num2
            num2 = target
            target = num1 + num2
        return target

a = Solution()
re=a.Fibonacci(6)
print(re)