# Fibonacci using recursion

def fib(inn) :
    if inn <= 1 :
        return inn

    else :
        return (fib(inn - 1) + fib(inn - 2)) 

# fib(inn - 1) means previous call. For example if it's running for 2 it will be fib(2 - 1) or fib(1)
# fib(inn - 2) means previous call of previous call. For example if it's running for 2 it will be fib(2 - 2) or fib(0)

n = int(input("Enter the number of times : "))  

for i in range(n) :
    print(fib(i))