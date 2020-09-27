import re
import copy
file2=open('chromosome1.txt','r',encoding='UTF-8')#染色体初始化
arr=[]#将染色体的每一项存入列表
line2=file2.readlines()
for eachitem in line2:
    rs=eachitem.replace('\n','')
    arr.append(rs)
arr.sort()
print('染色体arr:',arr,'\n','染色体长度：',len(arr))
file4=open('note1.txt','r',encoding='UTF-8')
note=[]  #将标注文档放在一个列表note中
line4=file4.readlines()
for eachnote in line4:
	rs1=eachnote.replace('\n','')
	note.append(rs1)
print('标注note：',note)
positivecount=[]
negativecount=[]

count=[]
for i in range(len(arr)):
    count.append(0) #将初始出现的次数置为0
    positivecount.append(0)
    negativecount.append(0)
file1=open('Data1.txt','r+',encoding='UTF-8-sig')
line1=file1.readlines()
ni=0
# for line in line1:
#     listmatch=re.findall('[a-zA-Z\']+', line.lower())
#     line.replace('\n','')
#     Dataline=listmatch
#     # print(Dataline)
#     if (note[ni]=='positive'):
#         for i in range(len(Dataline)):
#             low=0
#             high=len(arr)-1
#             while(low<=high):
#                 mid=int((low+high)/2)
#                 if((Dataline[i]==arr[mid])):
#                     positivecount[mid]=positivecount[mid]+1
#                     break
#                 elif(Dataline[i]>arr[mid]):
#                     low=mid+1
#                 elif(Dataline[i]<arr[mid]):
#                     high=mid-1
#     elif(note[ni]=='negative'):
#         for i in range(len(Dataline)):
#             low=0
#             high=len(arr)-1
#             while(low<=high):
#                 mid=int((low+high)/2)
#                 if((Dataline[i]==arr[mid])):
#                     negativecount[mid]=negativecount[mid]+1
#                     break
#                 elif(Dataline[i]>arr[mid]):
#                     low=mid+1
#                 elif(Dataline[i]<arr[mid]):
#                     high=mid-1
#
#     ni=ni+1
# print(positivecount)
# print(negativecount)
for line in line1:
    listmatch=re.findall('[a-zA-Z\']+', line.lower())
    line.replace('\n','')
    Dataline=listmatch
    # print(Dataline)
    for i in range(len(Dataline)):
        low=0
        high=len(arr)-1
        while(low<=high):
            mid=int((low+high)/2)
            if(Dataline[i]==arr[mid]):
                # if(note[ni]=='positive'):
                count[mid]=count[mid]+1
                break

            elif(Dataline[i]>arr[mid]):
                low=mid+1
            elif(Dataline[i]<arr[mid]):
                high=mid-1
print(count)
lowerthan2=[]
for i in range(len(count)):
    if(count[i]==1):
        lowerthan2.append(arr[i])
print(lowerthan2)
print(len(lowerthan2))
for i in range(len(lowerthan2)):
    arr.remove(lowerthan2[i])
print(len(arr))
for i in range(len(arr)):
    print(arr[i])