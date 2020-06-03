#Q1

Junior = {'SI 206':4, 'SI 310':4, 'BL 300':3, 'TO 313':3, 'BCOM 350':1, 'MO 300':3}
credits=0
keys=Junior.keys()
for key in keys:
    credits+=Junior[key]
    
#Q2

str1 = "peter piper picked a peck of pickled peppers"
freq={}
for c in str1:
    if c not in freq:
        freq[c]=0
       
    freq[c]+=1
   
print(freq)

#Q3

s1 = "hello"
counts={}
for c in s1:
    if c not in counts:
        counts[c]=0
       
    counts[c]+=1
   
print(counts)

#Q4

str1 = "I wish I wish with all my heart to fly with dragons in a land apart"
freq_words={}
words=str1.split()
for c in words:
    if c not in freq_words:
        freq_words[c]=0
       
    freq_words[c]+=1
   
print(freq_words)

#Q5

sent = "Singing in the rain and playing in the rain are two entirely different situations but both can be good"
wrd_d={}
words=sent.split()
for c in words:
    if c not in wrd_d:
        wrd_d[c]=0
       
    wrd_d[c]+=1
   
print(wrd_d)

#Q6

sally = "sally sells sea shells by the sea shore"
characters={}
for c in sally:
    if c not in characters:
        characters[c]=0
       
    characters[c]+=1
   
keys=list(characters.keys())
best_char=keys[0]
for key in keys:
    if characters[key]>characters[best_char]:
        best_char=key

#Q7
    
sally = "sally sells sea shells by the sea shore and by the road"

characters={}
for c in sally:
    if c not in characters:
        characters[c]=0
       
    characters[c]+=1
   
keys=list(characters.keys())
worst_char=keys[0]
for key in keys:
    if characters[key]<characters[worst_char]:
        worst_char=key
        
#Q8
        
string1 = "There is a tide in the affairs of men, Which taken at the flood, leads on to fortune. Omitted, all the voyage of their life is bound in shallows and in miseries. On such a full sea are we now afloat. And we must take the current when it serves, or lose our ventures."
string=string1.lower()
letter_counts={}
for c in string:
    if c not in letter_counts:
        letter_counts[c]=0
       
    letter_counts[c]+=1
   
#Q9
    
p = "Summer is a great time to go outside. You have to be careful of the sun though because of the heat."
low_d={}
for c in p.lower():
    if c not in low_d:
        low_d[c]=0
       
    low_d[c]+=1

