import sys

def fibonacci(n):
    if n <=1:
        if n==1:
            rta1=1
            return rta1
        else:
            r=0
            return r 

    x = fibonacci(n-1)
    y = fibonacci(n-2)
    return int(x+y)


    #elif n==0:
        #rta2=0
        #return rta2

print(fibonacci(8))



