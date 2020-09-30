import math
import numpy as np
import sympy as sp 

def f(x):
    #dica: potencia -> ** 
    return np.cos(x)+1 #escreva aqui a funcao desejada

def flinha(x):
    return -np.sin(x)

def g(x):
    ans = x - (f(x)/flinha(x))
    return ans

def newton(e, x0):
    xk1 = x0 #xk-1
    print('|k|xk|flinha(xk)|f(xk)|')
    k=0
    while(1):
        xk = g(xk1)
        gxk = g(xk1)
        fxk = f(xk1)
        flxk = flinha(xk1)
        print('|',k,'|',xk1,'|',flxk,'|',fxk,'|')
        if(math.fabs(fxk)<e): 
            print('condicao de parada: f(xk) < e')
            break
        if(math.fabs((xk-xk1))<e): 
            print('condicao de parada: |xk-xk1| < e')
            break
        k=k+1
        xk1 = xk
    print('Aproximacao = ',xk)
        

#coloque os valores de a (inicio do intervalo), b (final do intervalo) e 'e' (precisao)
e = 10**(-7)
x0 = 3
newton(e,x0)