#Q1

letters = "alwnfiwaksuezlaeiajsdl"
sorted_letters=sorted(letters,reverse=True)

#Q2

animals = ['elephant', 'cat', 'moose', 'antelope', 'elk', 'rabbit', 'zebra', 'yak', 'salamander', 'deer', 'otter', 'minx', 'giraffe', 'goat', 'cow', 'tiger', 'bear']
animals_sorted=sorted(animals)

#Q3

medals = {'Japan':41, 'Russia':56, 'South Korea':21, 'United States':121, 'Germany':42, 'China':70}
alphabetical=[]
for medal in sorted(medals):
    alphabetical.append(medal)

#Q4

medals = {'Japan':41, 'Russia':56, 'South Korea':21, 'United States':121, 'Germany':42, 'China':70}
top_three=[]
top=[]
for medal in sorted(medals,key=lambda x:medals[x],reverse=True):
    top.append(medal)
   
for medal in top[:3]:
    top_three.append(medal)

#Q5

groceries = {'apples': 5, 'pasta': 3, 'carrots': 12, 'orange juice': 2, 'bananas': 8, 'popcorn': 1, 'salsa': 3, 'cereal': 4, 'coffee': 5, 'granola bars': 15, 'onions': 7, 'rice': 1, 'peanut butter': 2, 'spinach': 9}
most_needed=[]
for groc in sorted(groceries,key=lambda x:groceries[x],reverse=True):
    most_needed.append(groc)

#Q6

def last_four(x):
    y=str(x)
    z= y[4:8]
    return int(z)


ids = [17573005, 17572342, 17579000, 17570002, 17572345, 17579329]
sorted_ids=[]
for id in sorted(ids,key=lambda x:last_four(x)):
    sorted_ids.append(id)

#Q7

ids = [17573005, 17572342, 17579000, 17570002, 17572345, 17579329]
sorted_id=[]
for id in sorted(ids,key=lambda x:(str(x))[4:8]):
    sorted_id.append(id)

#Q8

ex_lst = ['hi', 'how are you', 'bye', 'apple', 'zebra', 'dance']
lambda_sort=[]
for ex in sorted(ex_lst,key=lambda x:x[1:2]):
    lambda_sort.append(ex)
