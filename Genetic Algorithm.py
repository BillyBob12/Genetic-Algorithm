import sys
import numpy
import math 
import random
import Initialization
population=50  #������Ⱥ��Ϊ50����Ⱦɫ����ĿΪ50
popsize=1
num_of_iterations=250000 #��������
pc=0.2  #�������
pm=0.01 #�������
chromosome=[[]]
while popsize<=population:
	Initialization()
	chromosome.append([Initialization.chroini]) #�����е�Ⱦɫ���ʼ��������ڶ�ά������
	Initialization.Fitness()
	Rre=R  #�����ص���Ӧ��ֵ����Rre
Rre=[]


####�������н�������������####

	
		####�Ŵ�####
	def selections(): #ѡ�񸸴�,ѡ�����ֵ������
		Rbackup=Rre  #��ԭȾɫ����б���
		Max1=Rre.index(max(Rre)) #��λ���ֵ��λ��
			inf=-10000000
			Rre[Max1]=inf #�����λ�õ�ֵ��һ����С��ֵ���棬�ڶ����ֵ�ͳ�Ϊ������ֵ��
			Max2=Rre.index(max(Rre))
			p1=chromosome[Max1]
			p2=chromosome[Max2]
			Rre=Rbackup  #��ԭ�޸�ǰ��Rre
			return p1,p2,Max1,Max2

####�������н�������������####
	for iteration in range(num_of_iterations):
		def Crosser(): #����
			if [random.random()]<pc:
				crosscount=math.ceil(len(selections().p1)*pc) #����ȡ����
				bu=range(len(selections().p1))
				bu1=random.sample(bu,crosscount) #��0��Ⱦɫ�峤�ȼ�1�ķ�Χ�������ظ���crosscount������������н���
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
		####����###
		def Mutation():
			if [random.random()]<pm: #����0��1֮��������
				mutationcount=math.ceil(len(selections().p1)*pm) #����ȡ����
				bu2=range(len(Crosser().c1))
				bu3=random.sample(bu2,mutationcount) #��0��Ⱦɫ�峤�ȼ�1�ķ�Χ�������ظ���mutationcount������������б���
				for mutationbegin in range(mutationcount):
					Crosser().c1[bu3[mutationcount]]=random.randint(-10,10)
					Crosser().c2[bu3[mutationcount]]=random.randint(-10,10)
					chromosome[selections().Max1]=Crosser().c1  #����Ⱦɫ�帳ֵ
					chromosome[selections().Max2]=Crosser().c2
					a=Crosser().c1 #��c1����a��fitness�����е�Ⱦɫ�壩
					Fitness()
					Rc1=Rre #����Ӧ��ֵ����Rc1
					Rre[selections().Max1]=Rc1[0]  #������Ӧ��ֵ
					a=Crosser().c2
					Fitness()
					Rc2=Rre #����Ӧ��ֵ����Rc2
					Rre[selections().Max2]=Rc2[0]   #������Ӧ��ֵ
					return Rc1,Rc2
		
		##Replacement###
		###ѡ��������Խ�С��Rֵ��Ⱦɫ���뽻�������Rc1��Rc2���бȽ�
		def Replacement():
			##��ѡ��������Ĵ���Ӧ��ֵ��Ⱦɫ��
			Rbackup=Rre #��ԭȾɫ����б���
			inf1=-10000000
			Rre[Rre.index(max(Rre))]=inf1 #�����λ�õ�ֵ��һ����С��ֵ���棬�ڶ����ֵ�ͳ�Ϊ������ֵ��
			Rre[Rre.index(max(Rre))]=inf1 #�����λ�õ�ֵ��һ����С��ֵ���棬�ڶ����ֵ�ͳ�Ϊ������ֵ��
			Max3=Rre.index(max(Rre)  #������ֵ��λ��
			Rre[Rre.index(max(Rre))]=inf1 #�����λ�õ�ֵ��һ����С��ֵ���棬�ڶ����ֵ�ͳ�Ϊ������ֵ��
			Max4=Rre.index(max(Rre)  #���Ĵ�ֵ��λ��
			r1=chromosome[Max3]
			r2=chromosome[Max4]
			Rre=Rbackup  #��ԭ�޸�ǰ��Rre
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

		

			


			
		

						 





				



	
		
		

				
				

