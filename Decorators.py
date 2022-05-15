'''Modify existing functions'''

'''initial function'''
def divide(a, b) :
    print(a/b)

'''initial calling'''
divide(2,4)

'''Modification'''
def divideWithSmaller(func) :
    def inner (a, b) :
        if a < b :
            a, b = b , a 
        return func(a, b) 
    return inner    

divide = divideWithSmaller(divide)

'''calling after Modification'''
divide(2,4)