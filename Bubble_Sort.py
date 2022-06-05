# Bubble Sort

listXYZ = [9,6,2,4,16,25,9]

for i in range (len(listXYZ)-1,0,-1) :    # starting from end, till 0, decrementing -1
    for j in range(i) :                   # till unsorted list
        if listXYZ[j] > listXYZ[j+1] :
            temp = listXYZ[j]             # swap
            listXYZ[j] = listXYZ [j+1]
            listXYZ [j+1] = temp

print(listXYZ)                            # [2, 4, 6, 9, 9, 16, 25]