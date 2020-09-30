import math
import numpy as np
import sympy as sp 

def f(x):
    #dica: potencia -> ** 
    return x**3-9*x+3 #escreva aqui a funcao desejada

def g(xk, xk1):
    ans = (xk1*f(xk) - xk*f(xk1))/(f(xk)-f(xk1))
    return ans

def secante(e, x0,x1):
    xk = x1
    xk1 = x0
    print('|k|xk|flinha(xk)|f(xk)|')
    k=1
    while(1):
        xkk = g(xk1,xk)
        print('|',k,'|',xkk,'|',f(xkk),'|')
        if(math.fabs(f(xkk))<e): 
            print('condicao de parada: f(xk) < e')
            break
        if(math.fabs((xk-xk1))<e): 
            print('condicao de parada: |xk-xk1| < e')
            break
        k=k+1
        xk1 = xk
        xk = xkk
    print('Aproximacao = ',xkk)
        

#coloque os valores de a (inicio do intervalo), b (final do intervalo) e 'e' (precisao)
e = 0.0005
x0 = 0
x1 = 1
secante(e,x0,x1)