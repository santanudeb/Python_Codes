# Exception Handling

num1=100

try :
    print ("opening file")         # open file in try block
    num2 = int(input("Enter a number to divide 100 : "))
    print(num1/num2)

except ZeroDivisionError as ZD :
    print("Divided by Zero", ZD)   # Divided by Zero division by zero

except ValueError as VE :
    print("Wrong value", VE)       # Wrong value invalid literal for int() with base 10: 'p'

except Exception as e :
    print("Unknown error")         # Unknown error

finally :
    print ("closing file")         # close file in try block      