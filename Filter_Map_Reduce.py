# Lamda Filter Map Reduce

from functools import reduce

# function doing similar to lambda n : n % 2 == 0
def even(n) :
    return n % 2 == 0

# function doing similar to lambda n : n * 2
def multiplyBy2(n) :
    return n * 2

# function doing similar to lambda a,b : a+b
def sum(n1, n2) :
    return n1 + n2

list_name = [1 , 4 , 5 , 8]

# Filter
fil1 = list(filter(even,list_name))
fil2 = list(filter(lambda n : n % 2 == 0,list_name))

# Map
fil3 = list(map(multiplyBy2,list_name))
fil4 = list(map(lambda n : n * 2,list_name))

# Reduce
fil5 = reduce(sum,list_name)
fil6 = reduce(lambda a,b : a+b,list_name)

print(fil1)
print(fil2)
print(fil3)
print(fil4)
print(fil5)
print(fil6)