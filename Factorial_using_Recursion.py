# Factorial using recursion

def fac (num) :
    if num == 1 :
        return num  # This will execute first
    else :
        return num * fac(num - 1)  # Then Order will be fac(2) > fac(3) > fac(4) > fac(5) and so on


input_num = int(input("Enter a number for factorial value : "))
value = fac(input_num)  
print(value)