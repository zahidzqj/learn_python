# -*- coding:utf-8 -*-
# 运行时间：20ms
# 占用内存：5856k
class Solution:
    def PrintMinNumber(self, numbers):
        # write code hereu
        if not numbers:
            return ''
        numbers = [str(num) for num in numbers]
        for i in range(len(numbers)-1):
            for j in range(i+1, len(numbers)):
                if numbers[j] + numbers[i] < numbers[i] + numbers[j]:#判断组合的str大小
                    numbers[i],numbers[j] = numbers[j],numbers[i]
        return ' '.join(numbers)

a = Solution()
b = a.PrintMinNumber((1,5,8,4,2))
print(b)


print(str(1)+str(2))

cc = [1,5,2]
for i in range(len(cc)-1):
	for j in range(1,len(cc)):
		if cc[i]<cc[j]:
			pass
		else:
			cc[i],cc[j]=cc[j],cc[i]
print(cc)