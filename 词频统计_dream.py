#不借助工具统计txt文档中的词频
def find_word_count(words):
	words_count={}
	for word in words:
		if word in words_count:#words_count.keys()
			words_count[word] +=1
		else:
			words_count[word] = 1
	return words_count

words = []
with open('dream.txt','r') as f:
	lines = f.readlines()
	for line in lines:
		line = line.replace(',',' ')
		line = line.replace('.',' ')
		line = line.replace('?',' ')
		line = line.replace('!',' ')
		line = line.replace(':',' ')
		line = line.replace('\n',' ')
		line = line.replace('"',' ')
		line = line.replace('\'',' ')
		line = line.replace('-',' ')

		for word in line.split(' '):
			if word:
				words.append(word)
print(len(words))
print(len(set(words)))

print(find_word_count(words))

