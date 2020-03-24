ss = 'I LOVE YOU'

class Solution:
    # ss 源字符串
    
    def replaceSpace(self, ss):
    	s = ''
    	for i in ss:
    		if i != ' ':
    			s+=i
    		else:
    			s+="**"
    	return s
s1 = Solution()
s=s1.replaceSpace(ss)
print(s)