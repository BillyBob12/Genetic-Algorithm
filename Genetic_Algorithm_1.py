import random
import math
import re
import copy
import pprint
import Mutation_Guide

mutationdirection = Mutation_Guide.mutationdirection

populationsize=2000 #种群数量
w=60   #惩罚因子
pm=0.10 #变异概率
pc=0.8  #交叉概率
Topn=0.025  #保优概率
iterations=1000
#####代码整体思想：
#####第一步：将情感词文件读取出来
#####第二步：对种群进行初始化
#####第三步：读取标注文件（用于后面适应度值计算）
#####第四步：计算种群适应度值
#####第五步：对种群适应度值进行排序，并且将种群中每一条染色体按适应度顺序排序
#####第六步：选取种群中Topn直接进入到下一代，记为p1
#####第七步：将p1按顺序依次取一条作为父亲染色体，按轮盘赌的方式从原始种群中选取一条作为母亲染色体
#####第八步：进行交叉
#####第九步：进行变异
#####第十步：将交叉变异后的父母染色体添加至下一代种群中，并重复7，8，9步len（p1）c次
#####第十一步：下一代种群中剩余的个体采用轮盘赌的方式从上一代随机选取
#####重复4-11步
#####终止条件设定：100代 或是 最大最小适应度值差值小于等于5%
arr=[]
def Chromosome(a):  ##读取情感词
	file_of_chromosome=open('chromosome_1gram.txt','r', encoding='UTF-8')
	line_of_chromosome=file_of_chromosome.readlines()
	for eachline in line_of_chromosome:
		rs=eachline.replace('\n','')
		a.append(rs)
Chromosome(arr)
# print('染色体arr:',arr,'\n','染色体长度：',len(arr))

a=[[0 for x in range(2)] for y in range(len(arr))]

def Initialization(m):  ##初始化染色体
	for i in range(populationsize):
		chroini=[]
		for j in range(len(arr)):
			chroini.append(random.randint(-10,10))
		m.append(chroini)
	m.remove(m[0])

note=[]
def ReadFile_Note(n):
	file=open('Note_Stanford.txt','r',encoding='UTF-8')
	line=file.readlines()
	for eachline in line:
		rs=eachline.replace('\n','')
		n.append(rs)
ReadFile_Note(note)

###calculate p


def Fitness(Fitness,chromosome,n):
	##
#calculate p
	file3 = open('Data_Stanford.txt', 'r', encoding='UTF-8')
	line3 = file3.readlines()
	# print(len(line3))
	x=0
	while x<n:  #chromosome的下标是从0开始的
		R = []  #每一条tweet的适应度值存在一个列表中
		m = 0
		ni=-1
		if n==1:
			chroini=copy.deepcopy(chromosome)
		else:
			chroini=copy.deepcopy(chromosome[x])
		for line in line3:   #一条tweet
			P = 0
			r = 0
			listMatch = re.findall('[a-zA-Z\']+', line.lower())  # 以小写表示
			line.replace('\n', '')
			Dataline = listMatch  #每一行都作为一个列表存放
			# print('Tweet长度：',len(Dataline))
			for i in range(len(Dataline)):  #对一条tweet的每一个词进行判别是否存在于染色体中
				low=0
				high=len(arr)-1
				while (low<=high):
					mid=int((low+high)/2)
					if Dataline[i]==arr[mid]:
						P=P+chroini[mid]
						# print(arr[mid])
						break
					elif Dataline[i]>arr[mid]:
						low=mid+1
					elif Dataline[i]<arr[mid]:
						high=mid-1

			# print('predict_classP:',P)

			ni=ni+1
			# print(ni)
			if ((P > 0 and note[ni] == 'positive') or (P <= 0 and note[ni] == 'negative')):
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
		Fitness.append(m)
		x=x+1


####对适应度值进行排序
def Sort(m,n):
	# print(m)
	c=[]
	d=sorted(enumerate(m), key=lambda x:x[1],reverse=True)
	for i in range(len(d)):
		c.append(d[i][0])
	# print(c)
	m.sort(reverse=True)
	ncopy=[]
	for i in range(len(n)):
		ncopy.append(n[c[i]])
	# print(ncopy)
	for i in range(len(n)):
		n[i]=ncopy[i]


##开始遗传算法

def Top_n_persent(a,persent ,chromosome_top,ori):   ##选取种群中前n%直接进入到下一代
	lena=len(a)
	topn=int(lena*persent)
	for i in range(topn):
		chromosome_top.append(ori[i])
	chromosome_top.remove(chromosome_top[0])
# Top_n_persent(Topn,chromosomecopy)
# print('Topn are:',chromosomecopy,'\n',len(chromosomecopy))


# p1=[]
# p2=[]
def selections(a,p,c):  # 选择母代,父代从topn中顺序选出
	##计算每条染色体适应度值比率
	sum_of_Fit=0
	for i in range(len(a)):
		sum_of_Fit=sum_of_Fit+a[i]
	Fitvalue=[]
	for i in range(len(a)):
		Fitvalue.append(a[i]/sum_of_Fit)
	###计算累积概率
	cumvalue=[]
	for i in range(len(Fitvalue)):
		cum = 0
		for j in range(i+1):
			cum=cum+Fitvalue[i]
		cumvalue.append(cum)
		# print(cumvalue)
	##开始选择
	ps1=random.random() #随机产生一个0-1的随机数
	# print(ps1)
	indexp=0
	for i in range(len(cumvalue)):
		if(ps1<cumvalue[i]):
			indexp=i
			break
	for i in range(len(c[indexp])):
		p.append(c[indexp][i])
	return a[indexp]
###选择结束###

######交叉#####

def Crossover(a,b):  # 交叉
	cp=random.random()
	if cp<pc:
		crosscount = math.ceil(len(a) * pc)  # 向上取整数
		bu = range(len(a))
		bu1 = random.sample(bu, crosscount)  # 在0到染色体长度减1的范围产生不重复的crosscount个随机数，进行交叉
		# print('交叉下标',bu1)
		p3=[]
		for i in range(len(a)):
			p3.append(a[i])
		for crossbegin in range(crosscount):
			a[bu1[crossbegin]] = b[bu1[crossbegin]]
			b[bu1[crossbegin]] = p3[bu1[crossbegin]]



def Mutation(a,b):
	if (random.random()) < pm:  # 产生0，1之间的随机数
		mutationcount = math.ceil(len(a) * pm)  # 向上取整数
		bu2 = range(len(a))
		bu3 = random.sample(bu2, mutationcount)  # 在0到染色体长度减1的范围产生不重复的mutationcount个随机数，进行变异
		# print('变异下标：',bu3)
		for mutationbegin in range(mutationcount):
			a[bu3[mutationbegin]] = random.randint(-10, 10)+mutationdirection[bu3[mutationbegin]]
			if(a[bu3[mutationbegin]]>10):
				a[bu3[mutationbegin]]=10
			elif(a[bu3[mutationbegin]]<-10):
				a[bu3[mutationbegin]]=-10
			b[bu3[mutationbegin]] = random.randint(-10, 10)+mutationdirection[bu3[mutationbegin]]
			if(b[bu3[mutationbegin]]>10):
				b[bu3[mutationbegin]]=10
			elif(b[bu3[mutationbegin]]<-10):
				b[bu3[mutationbegin]]=-10   #超过边界则设置为边界值


	###下一代更新结束

p11=[]
def main():
	chromosome=[[]]
	Initialization(chromosome)
	file_best_Fit=open('Bes_Fit.txt','w',encoding='UTF-8')
	Fit=[]
	Fitness(Fit,chromosome,populationsize)
	for i in range(iterations):
		Fitcopy=[]
		# print('Fit',Fit)
		Sort(Fit,chromosome)
		# for i in range(len(chromosome)):
		# 	print(chromosome[i])
		Chromosomecopy=[[]]
		Top_n_persent(Fit,Topn, Chromosomecopy,chromosome)
		for i in range(int(len(Fit)*Topn)):
			Fitcopy.append(Fit[i])
		# print('Chromosomecopy', Chromosomecopy)
		for i in range(int(populationsize*Topn)):
			p2=[]
			p1=copy.deepcopy(Chromosomecopy[i])
			selections(Fit,p2,chromosome)
			Crossover(p1,p2)
			Mutation(p1,p2)
			Chromosomecopy.append(p1)
			Chromosomecopy.append(p2)
			Fit1_pie=[]
			Fitness(Fit1_pie,p1,1)
			Fitcopy.append(Fit1_pie[0])
			Fit2_pie = []
			Fitness(Fit2_pie, p2, 1)
			Fitcopy.append(Fit2_pie[0])
		count=populationsize-int(3*Topn*populationsize)
		for i in range(count):
			a=[]
			f=selections(Fit,a,chromosome)
			Chromosomecopy.append(a)
			Fitcopy.append(f)
		chromosome=copy.deepcopy(Chromosomecopy)
		# print(Fit[0],file=file_best_Fit,end=' ')
		print(Fit[0])
		print(chromosome[0],file=file_best_Fit,end='\n')

		Fit = copy.deepcopy(Fitcopy)
	for i in range(len(chromosome[0])):
		p11.append(chromosome[0][i])

def Lexicon_Construction():
    parameter=[]
    for i in range(len(p11)):
        if p11[i]>0:
            parameter.append('positive')
        elif p11[i]==0:
            parameter.append('neutral')
        else:
            parameter.append('negative')
    print(parameter)
    lexicon=[[0 for x in range(2)] for y in range(len(arr))]
    for i in range(len(arr)):
        lexicon[i][0]=arr[i]
        lexicon[i][1]=parameter[i]
    print('最终产生的词库的正负性：', lexicon)
    for j in range(len(arr)):
        lexicon[j][1]=p11[j]
    print('最终产生的词库：',lexicon)

if __name__ == '__main__':
    print('The program is running, please wait(The topn is 10%)...')
    main()
    print('最终得到的最优染色体：', p11)
    Lexicon_Construction()



