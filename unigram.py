import re
import Replacers

repalcer = Replacers.RegexpReplacer()
def Unigram(data):
	with open(data, 'r',encoding='UTF-8') as f:
    words = {}
    # Find the words each line
		for line in f.readlines():
			line = replacer.repalce(line)
			listMatch = re.findall('[a-zA-Z]+', line.lower())  # 以小写表示
        # Count
			for eachword in listMatch:
				eachLetterCount = len(re.findall(eachword, line.lower()))
				words[eachword] =words.get(eachword, 0) + eachLetterCount
            # Sort the result
    result = sorted(words.items(), key=lambda d: d[1], reverse=True)
    return result


if __name__ == '__main__':
	path_data = ' '
	unigram = Unigram(path)
	for each in unigram:
        if each[1]>=2:
           print(each[0])
