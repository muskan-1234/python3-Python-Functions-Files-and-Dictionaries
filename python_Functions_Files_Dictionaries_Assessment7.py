#Q1

def mult(s,n=6):
    return s*n

#Q2


def greeting(name,greeting="Hello ",  excl="!"):
    return greeting + name + excl

print(greeting("Bob"))
print(greeting(""))
print(greeting("Bob", excl="!!!"))

#Q3


def sum( intx,intz=5):
    return intz + intx

#Q4
    
def test(int,boole=True,dict1={2:3, 4:5, 6:8}):
    if boole:
       if int in dict1.keys():
            return dict1[int]   
        
    else:
        return boole

#Q5

def checkingIfIn(str,direction=True,d={'apple': 2, 'pear': 1, 'fruit': 19, 'orange': 5, 'banana': 3, 'grapes': 2, 'watermelon': 7}):
    if direction:
        if str in d.keys():
            return True
        else:
            return False
       
    else:
        if str not in d.keys():
            return True
        else:
            return False

#Q6

def checkingIfIn(a, direction = True, d = {'apple': 2, 'pear': 1, 'fruit': 19, 'orange': 5, 'banana': 3, 'grapes': 2, 'watermelon': 7}):
    if direction == True:
        if a in d:
            return d[a]
        else:
            return False
    else:
        if a not in d:
            return True
        else:
            return d[a]

# Call the function so that it returns False and assign that function call to the variable c_false
c_false=checkingIfIn('strawberry')
# Call the fucntion so that it returns True and assign it to the variable c_true
c_true=checkingIfIn('litchi',direction=False)
# Call the function so that the value of fruit is assigned to the variable fruit_ans
fruit_ans=checkingIfIn('fruit')
# Call the function using the first and third parameter so that the value 8 is assigned to the variable param_check
param_check=checkingIfIn('litchi',False,{'litchi':8})

