import math
import numpy as np

def f(x):
    #dica: potencia -> ** 
    return 300000 - ((1500/(x/12))*(1 - ((1+x/12)**(-12*30)))) #escreva aqui a funcao desejada

def bisseccao(a, b, e):
    
    #verificando teorema de bolzano
    if (f(a)*f(b)<0): #existe pelo menos um ponto c no intervalo [a,b] tal que f(c)=0
        print('|k|a|b|f(a)|f(b)|x|f(x)|')
        k=0
        while(1):
            x = (a+b)/2
            
            
            print('|', k, '|',a, '|',x,'|', b, '|',f(a),'|', f(x),'|',f(b),'|')
            
            #determinando os novos "limites" do intervalo
            if(f(a)*f(x) < 0): 
                b = x
            else:
                a = x
            k=k+1
            if (math.fabs(b-a)<e): break
            if (math.fabs(f(x))<e): break
        
        #print da ultima linha da tabela apos atingir a condicao
        x = (a+b)/2
        print('|', k, '|',a, '|', x, '|',b,'|', f(a),'|', f(x), '|',f(b),'|')
    else:
        print('f(a)=',f(a))
        print('f(b)=',f(b))
        print('Nao existe raiz nesse intervalo')

#coloque os valores de a (inicio do intervalo), b (final do intervalo) e 'e' (precisao)
a = 0.03
b = 0.09
e = 5*10**-2
bisseccao(a, b, e)

