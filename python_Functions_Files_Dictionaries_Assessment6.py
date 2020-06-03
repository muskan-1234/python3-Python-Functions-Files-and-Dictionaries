#Q1

def sublist(list):
    index=0
    sub=[]
    while index<len(list):
        if list[index]!=5:
            sub.append(list[index])
           
        else:
            break
        index+=1
       
    return sub

#Q2

def check_nums(list):
    index=0
    sub=[]
    while index<len(list):
        if list[index]!=7:
            sub.append(list[index])
           
        else:
            break
        index+=1
       
    return sub
    
#Q3

def sublist(list):
    index=0
    sub=[]
    while index<len(list):
        if list[index]!='STOP':
            sub.append(list[index])
           
        else:
            break
        index+=1
       
    return sub

#Q4

def stop_at_z(list):
    index=0
    sub=[]
    while index<len(list):
        if list[index]!='z':
            sub.append(list[index])
           
        else:
            break
        index+=1
       
    return sub

#Q5


sum1 = 0

lst = [65, 78, 21, 33]

for x in lst:
    sum1 = sum1 + x

index=0
sum2=0
while index<len(lst):
    sum2+=lst[index]
    index+=1
    
#Q6

def beginning(list):
    index=0
    sub=[]
    while index<len(list):
        if list[index]!='bye':
            sub.append(list[index])
           
        else:
            break
        index+=1
       
    if len(sub)>10:
        max=[]
        index=0
        while index<10:
            max.append(sub[index])
            index+=1
        return max
    else:
        return sub
        