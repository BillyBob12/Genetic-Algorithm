import re
with open('Data1.txt', 'r',encoding='UTF-8') as f:
    words = {}
    # Find the words each line
    for line in f.readlines():
        listMatch = re.findall('[a-zA-Z\']+', line.lower())  # 以小写表示
        # Count
        for eachword in listMatch:
            eachLetterCount = len(re.findall(eachword, line.lower()))
            words[eachword] =words.get(eachword, 0) + eachLetterCount
            # Sort the result
    result = sorted(words.items(), key=lambda d: d[1], reverse=True)
    print(result)
    # for each in result:
    #     if each[1]>=2:
    #        print(each[0])
    for i in result:
        if i[0]=='adidas':
            print(i[1])



