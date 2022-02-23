import random
def createrand(list,percent):
# 空列表,入座率
    num=len(list)
    count=0
    # n1=num/3
    randnum=num*percent
    while count<=randnum:
        temp=random.randint(0,num-1)
        if list[temp]==0:
            list[temp]=1
            count+=1
size=[135,112,118,129,113,96,92]
l0=[0]
l1=l0*size[0]
createrand(l1,0.8)