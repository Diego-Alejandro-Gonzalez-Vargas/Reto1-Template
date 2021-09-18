import sys
import matplotlib.pyplot as pl
import pandas as pd
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


#GRAFICA PARA FISISCA 1:

datos=pd.read_csv("//Data/fisica.csv")
print(datos.head())