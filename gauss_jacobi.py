import math
from copy import deepcopy

def criterio_linha(m,l): #l tamanho da matriz, m a matriz
    max = 0
    print('alfa_i = ')
    casas_dec = 4
    alfai = []
    for i in range(0,l):
        soma = 0
        for j in range(0,l):
            if(i!=j):
                soma = soma + math.fabs(m[i][j])
        soma = soma/math.fabs(a[i][i])
        alfai.append(round(soma,casas_dec))
        if(max < soma):
            max = soma
    print(alfai)
    if(max < 1):
        print('Criterio das linhas satisfeito')
        return True
    print('Criterio das linhas nao satisfeito')
    return False

def equacao(a,x,l,b): #x^(k+1)
    c = deepcopy(a)
    y = deepcopy(x)
    casas_dec = 4
    pivo = []
    g = []
    for i in range(0,l):
        pivo.append(a[i][i])
        g.append(round(b[i]/pivo[i],casas_dec))

    for i in range(0,l):
        for j in range(0,l):
            if(i==j):
                c[i][j]=0
            else:
                c[i][j] = round(-c[i][j]/pivo[i],casas_dec)

    for i in range(0,l):
        ans = 0
        for j in range(0,l):
            ans = ans + c[i][j]*x[j]
        y[i] = round(ans + g[i],4)

    
    print('C=')
    for i in range(0,l):
        print(c[i])

    print('g=')
    print(g)
    return y
    
    

def gauss_jacobi(a,b,x,l,e):
    if(criterio_linha(a,l)):
        cont = 0
        while 1:
            cont = cont + 1
            num = 0
            den = 0
            print('k=',cont-1)
            y = equacao(a,x,l,b)
            for i in range(0,l):
                print('|x(%d)-x(%d)|=%.4f'%(i,i-1,math.fabs(y[i]-x[i])))
                if(num < math.fabs(y[i]-x[i])):
                    num = math.fabs(y[i]-x[i])
                if(den < math.fabs(y[i])):
                    den = math.fabs(y[i])
            
            x = y 
            print('x(%d)='%(cont))
            print(x)
            print('')
            print('Numerador: ', num)
            print('Denominador: ',den)
            print('num/den = ', num/den)
            print('******************************')
            if((num/den)<e):
                break
    


a = [[9,1,-2,2],
    [1,15,-3,2],
    [1,-2,8,3],
    [2,2,1,12]]

b = [10.5,14.6,18.1,19.4]
x = [0,0,0,0]
l = len(b)
e = 0.01
gauss_jacobi(a,b,x,l,e)