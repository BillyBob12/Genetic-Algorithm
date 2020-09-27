import copy
import math
import re
import Replacers

repalcer = Replacers.RegexpReplacer()

def countPN(data):
	e = math.e
	positivecount = []
	negativecount = []
	count = []
	mutationdirection = []

	for i in range(len(arr)):
		count.append(0)  # 将初始出现的次数置为0
		positivecount.append(0)
		negativecount.append(0)
	file1 = open(data, 'r+', encoding='UTF-8-sig')
	line1 = file1.readlines()
	ni = 0
	for line in line1:
		line = replacer.replace(line)
		listmatch = re.findall('[a-zA-Z]+', line.lower())
		line.replace('\n', '')
		Dataline = listmatch
		# print(Dataline)
		if (note[ni] == 'positive'):
			for i in range(len(Dataline)):
				low = 0
				high = len(arr) - 1
				while (low <= high):
					mid = int((low + high) / 2)
					if ((Dataline[i] == arr[mid])):
						positivecount[mid] = positivecount[mid] + 1
						break
					elif (Dataline[i] > arr[mid]):
						low = mid + 1
					elif (Dataline[i] < arr[mid]):
						high = mid - 1
		elif (note[ni] == 'negative'):
			for i in range(len(Dataline)):
				low = 0
				high = len(arr) - 1
				while (low <= high):
					mid = int((low + high) / 2)
					if ((Dataline[i] == arr[mid])):
						negativecount[mid] = negativecount[mid] + 1
						break
					elif (Dataline[i] > arr[mid]):
						low = mid + 1
					elif (Dataline[i] < arr[mid]):
						high = mid - 1

		ni = ni + 1
	# print(positivecount)
	# print(negativecount)
	for line in line1:
		line = reaplecer.replace(line)
		listmatch = re.findall('[a-zA-Z]+', line.lower())
		line.replace('\n', '')
		Dataline = listmatch
		# print(Dataline)
		for i in range(len(Dataline)):
			low = 0
			high = len(arr) - 1
			while (low <= high):
				mid = int((low + high) / 2)
				if (Dataline[i] == arr[mid]):
					# if(note[ni]=='positive'):
					count[mid] = count[mid] + 1
					break

				elif (Dataline[i] > arr[mid]):
					low = mid + 1
				elif (Dataline[i] < arr[mid]):
					high = mid - 1
				# print(count)
	for i in range(len(count)):
		if (count[i] == 0):
			print(i, 'is the zero')
	for i in range(len(arr)):
		mutationdirection.append(positivecount[i] / count[i])
	for i in range(len(mutationdirection)):  # 利用函数y=80*(x-1/2)^3
		x = copy.deepcopy((mutationdirection[i]))
		mutationdirection[i] = int(80 * (x - 1 / 2) * (x - 1 / 2) * (x - 1 / 2))
	return mutationdirection

if __name__ =='__main__':
	data_path = ''
	mutationdirection=countPN(data)