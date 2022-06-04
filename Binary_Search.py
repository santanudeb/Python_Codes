# Binary Search

listABC = [3,9,5,2,4,16]

listABC.sort() # for binary search you need sorted list

print(listABC)

pos = 0

def BinarySearch(listABC, val) :
    min = 0                             # initial lower bound
    max = len(listABC) - 1              # initial upper bound
    
    while (min <= max) :
        mid = (min + max) // 2          # getting mid value
        #print("min now : ",min)
        #print("max now : ", max)

        if val == listABC[mid] :        # comparing mid value with searching value
            globals() ['pos'] = mid     # if found storing it in pos
            return True
        else :
            if listABC[mid] < val :     # if mid value is less than searching value
               min = mid + 1            # mid value is now new min value
            else :                      # if mid value is bigger than searching value
               max = mid - 1            # mid value is now new max value

    return False
   

val = int(input("Enter a value you want to search : "))
#val = 9

if BinarySearch(listABC, val) :
    print("Found", pos+1)
else :
    print("Not found")    