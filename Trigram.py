import re
import Replacers

repalcer = Replacers.RegexpReplacer()

def Trigram(data):
	with open(data, 'r',encoding='UTF-8') as f:
	    words = {}
	    # Find the words each line
	    for line in f.readlines():
			line = repalcer.replace(line)
	        listMatch1 = re.findall('[a-zA-Z]+', line.lower())  # 以小写表示
	        # Count
	        listMatch=[]
	        for i in range(len(listMatch1)-2):
	            listMatch.append(str(listMatch1[i])+str(' ')+str(listMatch1[i+1])+str(' ')+str(listMatch1[i+2]))
	        for eachword in listMatch:
	            eachLetterCount = len(re.findall(eachword, line.lower()))
	            words[eachword] =words.get(eachword, 0) + eachLetterCount
	            # Sort the result
	    result = sorted(words.items(), key=lambda d: d[1], reverse=True)
	    return result

if __name__ == '__main__':
	path = ' ' 
	trigram = Trigram(path)
    for each in trigram:
        if each[1]>=2:
           print(each[0])

