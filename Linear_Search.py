# Linear Search

alist = [2,5,7,8,12]
pos = 0

print(alist)
num = int(input("Enter a number from above list to search : "))

# Using for loop
for i in range(0, len(alist)) :
    if alist[i] == num :
        print("found at ", i+1)   
        break
else : 
    print("not found")      

# Using while loop
j = 0
while j < len(alist) :
    if alist[j] == num :
        print("found at ", j+1)   
        break 
    j = j + 1 
    
else : 
    print("not found")