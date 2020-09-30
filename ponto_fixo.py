import math
import numpy as np

def f(x):
    #dica: potencia -> ** 
    return (((x**3)+3)/9.0) #escreva aqui a funcao desejada

def ponto_fixo(a, b, e, x0):
    xk1 = x0 #xk-1
    print('|k|xk|f(xk)|')
    k=0
    while(1):
        xk = f(xk1)
        fxk = f(xk)
        print('|',k,'|',xk1,'|',fxk,'|')
        if(math.fabs(fxk)<e): break
        if(math.fabs((xk-xk1))<e): break
        k=k+1
        xk1 = xk
    k=k+1
    xk1=xk    
    print('|',k,'|',xk1,'|',fxk,'|') #ultima linha
    print('Aproximacao = ',xk)
        

#coloque os valores de a (inicio do intervalo), b (final do intervalo) e 'e' (precisao)
a = 0
b = 1
e = 4*10**(-4)
x0 = 0.5
ponto_fixo(a, b, e, x0)

