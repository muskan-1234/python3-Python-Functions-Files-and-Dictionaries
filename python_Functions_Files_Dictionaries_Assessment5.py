#Q1

olympics=( 'Beijing', 'London', 'Rio', 'Tokyo')

#Q2

tuples_lst = [('Beijing', 'China', 2008), ('London', 'England', 2012), ('Rio', 'Brazil', 2016, 'Current'), ('Tokyo', 'Japan', 2020, 'Future')]
country=[]
for list in tuples_lst:
    country.append(list[1])

#Q3

olymp = ('Rio', 'Brazil', 2016)
city, country, year = 'Rio', 'Brazil', 2016

#Q4

def info( name, gender, age, bday_month, hometown):
    return  name, gender, age, bday_month, hometown

#Q5

gold = {'USA':31, 'Great Britain':19, 'China':19, 'Germany':13, 'Russia':12, 'Japan':10, 'France':8, 'Italy':8}
num_medals=[]
for medals in gold.items():
    medal=medals[1]
    num_medals.append(medal)
