# Selection Sort

listXYZ = [5,9,2,12,6,4]

#print(listXYZ)

for i in range (len(listXYZ)) :
    minpos = i

    for j in range (i,len(listXYZ)) :
        if listXYZ[j] < listXYZ[minpos] :
            minpos = j                        # capturing min value postion


    temp = listXYZ[i]                #Swap
    listXYZ[i] = listXYZ[minpos]   
    listXYZ[minpos] = temp 

    #print(listXYZ)

print(listXYZ)    