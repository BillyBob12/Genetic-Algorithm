import sys
import numpy
import math 
import random
import Initialization
population=50  #设置种群数为50，即染色体数目为50
popsize=1
num_of_iterations=250000 #迭代次数
pc=0.2  #交叉概率
pm=0.01 #变异概率
chromosome=[[]]
while popsize<=population:
	Initialization()
	chromosome.append([Initialization.chroini]) #将所有的染色体初始化结果放在二维数组中
	Initialization.Fitness()
	Rre=R  #将返回的适应度值存入Rre
Rre=[]


####迭代进行交叉变异产生最优####

	
		####遗传####
	def selections(): #选择父代,选择最大值的两个
		Rbackup=Rre  #将原染色体进行备份
		Max1=Rre.index(max(Rre)) #定位最大值的位置
			inf=-10000000
			Rre[Max1]=inf #将最大位置的值用一个极小的值代替，第二大的值就成为了最大的值了
			Max2=Rre.index(max(Rre))
			p1=chromosome[Max1]
			p2=chromosome[Max2]
			Rre=Rbackup  #还原修改前的Rre
			return p1,p2,Max1,Max2

####迭代进行交叉变异产生最优####
	for iteration in range(num_of_iterations):
		def Crosser(): #交叉
			if [random.random()]<pc:
				crosscount=math.ceil(len(selections().p1)*pc) #向上取整数
				bu=range(len(selections().p1))
				bu1=random.sample(bu,crosscount) #在0到染色体长度减1的范围产生不重复的crosscount个随机数，进行交叉
				for crossbegin in range(crosscount):
					 p3=selections().p1
					 selections().p1[bu1[crossbegin]]=selections().p2[bu1[crossbegin]]
					 selections().p2[bu1[crossbegin]]=p3[bu1[crossbegin]]
					 c1=selections().p1
					 c2=selections().p2
			else:
				c1=selections().p1
				c2=selections().p2
			
			return c1,c2
		####变异###
		def Mutation():
			if [random.random()]<pm: #产生0，1之间的随机数
				mutationcount=math.ceil(len(selections().p1)*pm) #向上取整数
				bu2=range(len(Crosser().c1))
				bu3=random.sample(bu2,mutationcount) #在0到染色体长度减1的范围产生不重复的mutationcount个随机数，进行变异
				for mutationbegin in range(mutationcount):
					Crosser().c1[bu3[mutationcount]]=random.randint(-10,10)
					Crosser().c2[bu3[mutationcount]]=random.randint(-10,10)
					chromosome[selections().Max1]=Crosser().c1  #更新染色体赋值
					chromosome[selections().Max2]=Crosser().c2
					a=Crosser().c1 #将c1赋给a（fitness函数中的染色体）
					Fitness()
					Rc1=Rre #将适应度值存入Rc1
					Rre[selections().Max1]=Rc1[0]  #更新适应度值
					a=Crosser().c2
					Fitness()
					Rc2=Rre #将适应度值存入Rc2
					Rre[selections().Max2]=Rc2[0]   #更新适应度值
					return Rc1,Rc2
		
		##Replacement###
		###选择两个相对较小的R值的染色体与交叉变异后的Rc1，Rc2进行比较
		def Replacement():
			##先选择第三第四大适应度值的染色体
			Rbackup=Rre #将原染色体进行备份
			inf1=-10000000
			Rre[Rre.index(max(Rre))]=inf1 #将最大位置的值用一个极小的值代替，第二大的值就成为了最大的值了
			Rre[Rre.index(max(Rre))]=inf1 #将最大位置的值用一个极小的值代替，第二大的值就成为了最大的值了
			Max3=Rre.index(max(Rre)  #第三大值的位置
			Rre[Rre.index(max(Rre))]=inf1 #将最大位置的值用一个极小的值代替，第二大的值就成为了最大的值了
			Max4=Rre.index(max(Rre)  #第四大值的位置
			r1=chromosome[Max3]
			r2=chromosome[Max4]
			Rre=Rbackup  #还原修改前的Rre
			return r1,r2
			Compare=[]
			Compare.append(Rc1[0],Rc2[0],Rre[Max3],Rre[Max4])
			Co1=Compare.index(max(Compare))
			if Co1==0:
				Q1=c1
				Rre[Max1]=Compare[0]
			elif Co1==1:
				Q1=c2
				Rre[Max2]=Compare[1]
			elif Co1==2:
				Q1=r1
			else:
				Q1=r2
			Compare[Compare.indexx(max(Compare))]=inf1
			Co2=Compare.index(max(Compare))
			if Co2==0:
				Q2=c1
			elif  Co1==1:
				Q2=c2
			elif Co1==2:
				Q2=r1
			else:
				Q2=r2
			r1=Q1
			r2=Q2
			p1=r1
			p2=r2
			return p1,p2

		

			


			
		

						 





				



	
		
		

				
				

