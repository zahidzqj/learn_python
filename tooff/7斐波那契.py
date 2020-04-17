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
re=a.Fibonacci(5)
print(re)

def fib(num):
    if num==1:
        return 1
    if num==2:
        return 1
    else:
        return fib(num-2)+fib(num-1)
result = fib(5)
print(result)