import math
import numpy as np

def f(x):
    #dica: potencia -> ** 
    return x**3-9*x+3 #escreva aqui a funcao desejada

def posicao_falsa(a, b, e):
    
    #verificando teorema de bolzano
    if (f(a)*f(b)<0): #existe pelo menos um ponto c no intervalo [a,b] tal que f(c)=0
        print('|k|a|b|f(a)|f(b)|x|f(x)|')
        k=0
        while(1):
            x = ((a*f(b))-(b*f(a)))/(f(b)-f(a))

            print('|', k, '|',a, '|', b, '|',f(a),'|', f(b),'|x= ', x, '|',f(x),'|')
            
            #determinando os novos "limites" do intervalo
            if(f(a)*f(x) < 0): #sinais trocados
                b = x
            else:
                a = x
            k=k+1
            if (math.fabs(b-a)<e): break
            if (math.fabs(f(x))<e): break
        
        #print da ultima linha da tabela apos atingir a condicao

        x = ((a*f(b))-(b*f(a)))/(f(b)-f(a))
        print('|', k, '|',a, '|', b, '|',f(a),'|', f(b),'|x= ', x, '|',f(x),'|')
    else:
        print('Nao existe raiz nesse intervalo')

#coloque os valores de a (inicio do intervalo), b (final do intervalo) e 'e' (precisao)
a = 0
b = 1
e = 2*10**(-3)
posicao_falsa(a, b, e)

