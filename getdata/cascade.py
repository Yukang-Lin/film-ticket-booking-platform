import os
f1=open('top100data.txt','r',encoding='utf-8')
f2=open('top100urls.txt','r')
# cascade1=f1.read()
# cascade2=f2.read()
cascade1=[]
cascade2=[]
cascade=['']*100
f=open("top100.csv","a",encoding='utf-8')
i=0
for line in f1.readlines():
    line=line.rstrip('\n')
    cascade1.append(line)
print(cascade1)
for line in f2.readlines():
    cascade2.append(line)
    cascade2[i]=cascade1[i]+','+cascade2[i]
    print(cascade2[i])
    f.write(cascade2[i])
    i+=1