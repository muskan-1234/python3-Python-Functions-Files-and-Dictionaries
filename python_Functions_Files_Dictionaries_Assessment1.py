#Q1

file=open('travel_plans.txt','r')
num=0
for char in file.read():
    num+=1
   
#Q2
    
file=open('emotion_words.txt','r')
words=file.read().split()
num_words=len(words)

#Q3

file=open('school_prompt.txt','r')
num_lines=0
lines=file.readlines()
for line in lines:
    num_lines+=1

#Q4
    
file=open('school_prompt.txt','r')
beginning_chars= file.read(30)

#Q5

file=open('school_prompt.txt','r')
three=[]
for line in file.readlines():
    l=line.split()
    three.append(l[2])

#Q6
    
file=open('emotion_words.txt','r')
emotions=[]
for line in file.readlines():
    l2=line.split()
    emotions.append(l2[0])

#Q7
    
file=open('travel_plans.txt','r')
first_chars=file.read(33)

#Q8

file=open('school_prompt.txt','r')
p_words=[]
for words in file.read().split():
    if 'p' in words:
        p_words.append(words)
