#不借助工具统计txt文档中的词频
def find_word_count(words):
	words_count={}
	for word in words:
		if word in words_count:#words_count.keys()
			words_count[word] +=1
		else:
			words_count[word] = 1
		#words_count[word] = words_count.get(word,0)+1
	for word in words:
		if words_count[word] == 1:
			return words.index(word)
print(find_word_count(['a','b','a','c']))

# -*- coding:utf-8 -*-
class Solution:
    def FirstNotRepeatingChar(self, s):
        # write code here
        char_count = {}
        for char in s:
            try:
                char_count[char] += 1
            except:
                char_count[char] = 1
        for char in s:
            if char_count[char] == 1:
                return s.index(char)
        return -1
a =Solution()
b = a.FirstNotRepeatingChar(['a','b','a','c'])
print(b)


# 运行时间：26ms
# 占用内存：5752k
# -*- coding:utf-8 -*-
class Solution:
    # 返回[a,b] 其中ab是出现一次的两个数字
    def FindNumsAppearOnce(self, array):
        # write code here
        num_count = {}
        result = []

        for num in array:
        	# if num in num_count:
        	# 	num_count[num] +=1
        	# else:
        	# 	num_count[num] =1
            num_count[num] = num_count.get(num,0) + 1
        for key,value in num_count.items():
            if value == 1:
                result.append(key)
        return result
a2 =Solution()
b2 = a2.FindNumsAppearOnce([1,2,3,1])
print(b2)