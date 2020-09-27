import random
import math
import re

populationsize=50
# def Initialization():
# 	file1=open('Data.txt')
# 	while 1:#按行读取数据集
# 		line1=file1.readline()
# 		if not line1:
# 			break
# 	file1.close()
file2=open('Chromosome.txt','r',encoding='UTF-8')#染色体初始化
arr=[]#将染色体的每一项存入列表
line2=file2.readlines()
for eachitem in line2:
    rs=eachitem.replace('\n','')
    arr.append(rs)
print('染色体arr:',arr,'\n','染色体长度：',len(arr))
#随机赋值-10，10，放入二维数组(population-size行，len(arr)列
# a={}
a=[[0 for x in range(2)] for y in range(len(arr))]
chromosome=[[]]
for m in range(populationsize):
    for i in range(len(arr)):
        a[i][0]=arr[i]
        a[i][1]=random.randint(-10,10)
    # print('染色体随机赋值后a：',a)
    file2.close()
    # 将染色体的赋值存在一个列表中
    chroini=[]
    for j in range(len(arr)):
        chroini.append(a[j][1])
    chromosome.append(chroini)
    # print('染色体的赋值chroini：',chroini)
# print(a)

#读取文本的行数
file4=open('note.txt','r',encoding='UTF-8')
note=[]  #将标注文档放在一个列表note中
line4=file4.readlines()
for eachnote in line4:
	rs1=eachnote.replace('\n','')
	note.append(rs1)
print('标注note：',note)
length=len(note)
print('测试文本的行数length：',length)
###calculate p

Fit = []
w=500
def Fitness():
	r=0
	P=0

	##
#calculate p
	file3=open('Data2.txt','r',encoding='UTF-8')
	line3 = file3.readlines()
	x=1
	while x<51:
		R = []  #每一条tweet的适应度值存在一个列表中
		m = 0
		chroini=chromosome[x]
		for line in line3:   #一条tweet
			listMatch = re.findall('[a-zA-Z]+', line.lower())  # 以小写表示
			line.replace('\n', '')
			Dataline = listMatch  #每一行都作为一个列表存放
			# print('Tweet长度：',len(Dataline))
			for i in range(len(Dataline)):  #对一条tweet的每一个词进行判别是否存在于染色体中
				for j in range(len(arr)):
					if Dataline[i]==arr[j]:
						P=P+chroini[j]

				# print('predict_classP:',P)
			if ((P > 0 and note[i] == 'positive') or (P < 0 and note[i] == 'negative') or (P == 0 and note[i] == 'neutral')):
				r = r + 1
			else:
				r = r - abs(P)/w # w是自定义的值
			# print('适应度值r：',r,'\n','predict_class:',P)
			R.append(r)
			r=0   #每一天染色体操作结束之后将值置为0
			P=0   #每一天染色体操作结束之后将值置为0

		# print('每一条tweet的适应度值：',R)
		for i in range(len(R)):
			m=m+R[i]
		# print('No',x,'条染色体所得适应度值：',m)
		Fit.append(m)
		x=x+1
	print('populationsize条染色体产生的适应度值Fit:',Fit)
	print('染色体的条数：',len(Fit))
	# print(Fit[0])
	# return Fit
	####Fit列表下标是从0开始，chromosome下标从1开始
Fitness()
###计算适应度值结束###
print('返回的所有染色体适应度值Fit：',Fit)

Rre=[] #将原染色体的适应度值进行备份,Rre=Fit是指针的赋值
for i in range(len(Fit)):
	Rre.append(Fit[i])

####迭代进行交叉变异产生最优####
# Max1 = Fit.index(max(Fit))  # 定位最大值的位置
####遗传####
####选择####
def selections():  # 选择父代,选择最大值的两个
	global Max1,Max2,p1,p2
	Max1 = Rre.index(max(Rre))  # 定位最大值的位置
	inf = -10000000
	Rre[Max1] = inf  # 将最大位置的值用一个极小的值代替，第二大的值就成为了最大的值了
	Max2 = Rre.index(max(Rre))
	p1 = chromosome[Max1+1]  #Fit列表下标从0开始，而chromosome下标是从1开始的
	p2 = chromosome[Max2+1]  #Fit列表下标从0开始，而chromosome下标是从1开始的
	print('染色体中最大值的位置下标：', Max1)
	print('染色体中第二大值的位置下标：', Max2)
	# print(p1)
	# print(p2)
	# return Max1,Max2,p1,p2
selections()
chrom1=[]
md1=chromosome[Max1+1]
for i in range(len(md1)):
	chrom1.append(md1[i])
print('交叉变异前的父代染色体1',chrom1)
chrom2=[]
md2=chromosome[Max2+1]
for j in range(len(md2)):
	chrom2.append(md2[j])
print('交叉变异前的父代染色体2',chrom2)
# print(chromosome[50])
# print(Max1)
# print(Max2)
print('p1:',p1)
print('p2:',p2)
###选择结束###

######交叉#####

pc=0.2  #交叉概率
def Crosser():  # 交叉
	global c1, c2
	cp=random.random()
	print(cp)
	if cp<1:
		crosscount = math.ceil(len(p1) * pc)  # 向上取整数
		bu = range(len(p1))
		bu1 = random.sample(bu, crosscount)  # 在0到染色体长度减1的范围产生不重复的crosscount个随机数，进行交叉
		print('交叉下标',bu1)
		p3=[]
		for i in range(len(p1)):
			p3.append(p1[i])
		for crossbegin in range(crosscount):
			p3[bu1[crossbegin]] = p2[bu1[crossbegin]]
			p2[bu1[crossbegin]] = p1[bu1[crossbegin]]
		c1 = p3
		c2 = p2
	else:
		c1 = p1
		c2 = p2
# Crosser()
# c11=[]
# for i in range(len(c1)):
# 	c11.append(c1[i])
# print('变异前c1:',c11)
# c22=[]
# for j in range(len(c2)):
# 	c22.append(c2[j])
# print('变异前c2:',c22)  ###c1 c2进行备份
####交叉结束###

####变异###
pm=0.01  #变异概率
def Mutation():
	if (random.random()) < 1:  # 产生0，1之间的随机数
		mutationcount = math.ceil(len(c1) * pm)  # 向上取整数
		bu2 = range(len(c1))
		bu3 = random.sample(bu2, mutationcount)  # 在0到染色体长度减1的范围产生不重复的mutationcount个随机数，进行变异
		print('变异下标：',bu3)
		for mutationbegin in range(mutationcount):
			c1[bu3[mutationbegin]] = random.randint(-10, 10)
			c2[bu3[mutationbegin]] = random.randint(-10, 10)
		chromosome[Max1+1] = c1  # 更新染色体赋值
		chromosome[Max2+1] = c2  # 更新染色体赋值
		###计算c1，c2的适应度值###
	global Rc1,Rc2,mc11,mc22
	Rc1=[]
	Rc2=[]
	file3 = open('Data2.txt', 'r', )
	line3 = file3.readlines()
	chroinic1 = c1

	for linec1 in line3:  # 一条tweet
		listMatchc1 = re.findall('[a-zA-Z]+', linec1.lower())  # 以小写表示
		linec1.replace('\n', '')
		Pc1 = 0
		rc1 = 0
		Datalinec1 = listMatchc1  # 每一行都作为一个列表存放
		for i in range(len(Datalinec1)):  # 对一条tweet的每一个词进行判别是否存在于染色体中
			for j in range(len(arr)):
				if Datalinec1[i] == arr[j]:
					Pc1 = Pc1 + chroinic1[j]


		if ((Pc1 > 0 and note[i] == 'positive') or (Pc1 < 0 and note[i] == 'negative') or (
				Pc1 == 0 and note[i] == 'neutral')):
			rc1 = rc1 + 1
		else:
			rc1 = rc1 - abs(Pc1) / w  # w是自定义的值
		# print('适应度值r：',r,'\n','predict_class:',P)
		Rc1.append(rc1)
	mc1=0
	for i in range(len(Rc1)):
		mc1=mc1+Rc1[i]
	mc11=[]
	mc11.append(mc1)
	print('c1的适应度值：', mc11)
	chroinic2 = c2
	for linec2 in line3:  # 一条tweet
		Pc2 = 0
		rc2 = 0
		listMatchc2 = re.findall('[a-zA-Z]+', linec2.lower())  # 以小写表示
		linec2.replace('\n', '')
		Datalinec2 = listMatchc2  # 每一行都作为一个列表存放
		for i in range(len(Datalinec2)):  # 对一条tweet的每一个词进行判别是否存在于染色体中
			for j in range(len(arr)):
				if Datalinec2[i] == arr[j]:
					Pc2 = Pc2 + chroinic2[j]

		if ((Pc2 > 0 and note[i] == 'positive') or (Pc2 < 0 and note[i] == 'negative') or (
						Pc2 == 0 and note[i] == 'neutral')):
			rc2 = rc2 + 1
		else:
			rc2 = rc2 - abs(Pc2) / w  # w是自定义的值
	# print('适应度值r：',r,'\n','predict_class:',P)
		Rc2.append(rc2)
	mc2=0
	for j in range(len(Rc2)):
		mc2=mc2+Rc2[j]
	mc22=[]
	mc22.append(mc2)

	print('c2的适应度值：', mc22)
# Mutation()
# print('交叉变异后的父代染色体1',chromosome[Max1+1])
# print('交叉变异后的父代染色体2',chromosome[Max2+1])
# print('变异后c1',c1)
# print('变异后c2',c2)
####变异完成###


##Replacement###
	###选择两个相对较小的R值的染色体与交叉变异后的Rc1，Rc2进行比较

def Replacement():
	bup1 = []
	bup2 = []
	##先选择第三第四大适应度值的染色体
	Rre = []  # 将原染色体的适应度值进行备份,Rre=Fit是指针的赋值
	for i in range(len(Fit)):
		Rre.append(Fit[i])
	global Max3,Max4,r1,r2
	inf1 = -1000000
	m1=Rre.index(max(Rre))
	Rre[m1] = inf1  # 将最大位置的值用一个极小的值代替，第二大的值就成为了最大的值了
	m2=Rre.index(max(Rre))
	Rre[m2] = inf1  # 将最大位置的值用一个极小的值代替，第二大的值就成为了最大的值了
	Max3 = Rre.index(max(Rre))  # 第三大值的位置
	max3=[]
	max3.append(Rre[Max3])
	Rre[Max3] = inf1  # 将最大位置的值用一个极小的值代替，第二大的值就成为了最大的值了
	Max4 = Rre.index(max(Rre))  # 第四大值的位置
	max4=[]
	max4.append(Rre[Max4])
	r1 = chromosome[Max3+1]
	r11=[]  #适应度第三大的染色体
	for i in range(len(r1)):
		r11.append(r1[i])
	r2 = chromosome[Max4+1]
	r22=[]  #适应度第四大染色体
	for j in range(len(r2)):
		r22.append(r2[j])
	print('r1:',r1)
	print('r2:',r2)
	Compare = []
	Compare.append(mc11[0])
	Compare.append(mc22[0])
	Compare.append(max3[0])
	Compare.append(max4[0])
	print(Compare[0])
	print(Compare[1])
	print(Compare[2])
	print(Compare[3])
	Co1 = Compare.index(max(Compare))
	if Co1 == 0:
		Q1 = c1
		Fit[Max1]=Compare[0]
	elif Co1 == 1:
		Q1 = c2
		Fit[Max1] = Compare[1]
	elif Co1 == 2:
		Q1 = r1
		Fit[Max1] = Compare[2]
	else:
		Q1 = r2
		Fit[Max1] = Compare[3]
	Commax=Compare.index(max(Compare))
	Compare[Commax] = inf1

	Co2 = Compare.index(max(Compare))
	print('最大两个值的位置：',Co1, Co2)
	if Co2 == 0:
		Q2 = c1
		Fit[Max2] = Compare[0]
	elif Co2 == 1:

		Q2 = c2
		Fit[Max2] = Compare[1]
	elif Co2 == 2:
		Q2 = r1
		Fit[Max2] = Compare[2]
	else:
		Q2 = r2
		Fit[Max2] = Compare[3]
	p1=Q1
	p2=Q2
	for i in range(len(Q1)):
		bup1.append(Q1[i])

	for j in range(len(Q2)):
		bup2.append(Q2[j])

	print('替代后的p1：', p1)
	print('替代后的p2：', p2)
	####更新染色体以及相对应的适应度值的赋值###
	com3=Compare.index(max(Compare))
	Compare[com3]=inf1
	if com3==0:
		Fit[Max3]=Compare[0]
		chromosome[Max3 + 1] =c1
	elif com3==1:
		Fit[Max3] = Compare[1]
		chromosome[Max3 + 1] =c2
	elif com3==2:
		Fit[Max3] = Compare[2]
		chromosome[Max3 + 1] =r11
	else:
		Fit[Max3] = Compare[3]
		chromosome[Max3 + 1] =r22
	com4=Compare.index(max(Compare))
	if com4==0:
		Fit[Max4]=Compare[0]
		chromosome[Max4 + 1] =c1
	elif com4==1:
		Fit[Max4] = Compare[1]
		chromosome[Max4 + 1] =c2
	elif com4==2:
		Fit[Max4] = Compare[2]
		chromosome[Max4 + 1] =r11
	else:
		Fit[Max4] = Compare[3]
		chromosome[Max4 + 1] =r22
	chromosome[Max1 + 1] = p1
	chromosome[Max2 + 1] = p2
	i = 0
	while i < len(bup1):
		p1[i] = bup1[i]
		p2[i] = bup2[i]
		i = i + 1
	print(p1)
	print(p2)
	global p11,p22
	p11=[]
	p22=[]
	for i in range(len(p1)):
		p11.append(p1[i])
		p22.append(p2[i])
# Replacement()
###替代结束##
###主函数###
def main():
	num_of_iterations = 2500
	for i in range(num_of_iterations):
		Crosser()
		c11 = []
		for i in range(len(c1)):
			c11.append(c1[i])
		print('变异前c1:', c11)
		c22 = []
		for j in range(len(c2)):
			c22.append(c2[j])
		print('变异前c2:', c22)  ###c1 c2进行备份
		Mutation()
		print('交叉变异后的父代染色体1', chromosome[Max1 + 1])
		print('交叉变异后的父代染色体2', chromosome[Max2 + 1])
		print('变异后c1', c1)
		print('变异后c2', c2)
		Replacement()

		# i=0
		# while i<len(bup1):
		# 	p1[i]=bup1[i]
		# 	p2[i]=bup2[i]
		# 	i=i+1
		print('最终得到的最优染色体1：', p11)
		print('最终得到的最优染色体2：', p22)
		for i in range(len(p11)):
			p1[i]=p11[i]
			p2[i]=p22[i]

# def main():
# 	Crosser()
# 	c11 = []
# 	for i in range(len(c1)):
# 		c11.append(c1[i])
# 	# print('变异前c1:', c11)
# 	c22 = []
# 	for j in range(len(c2)):
# 		c22.append(c2[j])
# 	# print('变异前c2:', c22)  ###c1 c2进行备份
# 	Mutation()
# 	# print('交叉变异后的父代染色体1', chromosome[Max1 + 1])
# 	# print('交叉变异后的父代染色体2', chromosome[Max2 + 1])
# 	# print('变异后c1', c1)
# 	# print('变异后c2', c2)
# 	Replacement()
# 	# print('最终得到的最优染色体1：', bup1)
# 	# print('最终得到的最优染色体2：', bup2)
# 	i = 0
# 	while i < len(bup1):
# 		p1[i] = bup1[i]
# 		p2[i] = bup2[i]
# 		i=i+1
# print(p1)
main()
print('最终得到的最优染色体：', p11)
print(p1)
print(p2)
###产生词库###
# parameter=[]
# for i in range(len(p1)):
#     if p1[i]>0:
#         parameter.append('positive')
#     elif p1[i]==0:
#         parameter.append('neutral')
#     else:
#         parameter.append('negative')
# print(parameter)
# lexicon=[[0 for x in range(2)] for y in range(len(arr))]
# for i in range(len(arr)):
#     lexicon[i][0]=arr[i]
#     lexicon[i][1]=parameter[i]
# print('最终产生的词库：',lexicon)

























