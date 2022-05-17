from array import *

# Empty array
arr = array('i',[])

# Array length
length = int(input("Enter length "))

# Taking input in array
for i in range(length):
    num = int(input("Enter number "))
    arr.append(num)

# Showing array
print(arr)   

# Number input to search index
index = int(input("Enter number to find index "))

# Method 1 using loop
k=0
for j in arr:
    if j == index :
        print(k)
        break
    k=k+1 

# Method 2 using function
print(arr.index(index))    