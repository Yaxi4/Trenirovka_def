file=open(r'D:\Python\обучение\numbers.txt','r',encoding='utf-8')
count=0
summ=0
for i in file:
    if len(str(i))==4:
        count+=1
    if len(str(i))==3:
        summ+=int(i)
print(count,summ)