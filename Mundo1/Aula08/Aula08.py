#Módulos
#Aumentam possibilidades da linguagem python
#sintaxe --> import "nome da biblioteca" --> importa todas a funcionalidades da biblioteca
#from "nome da biblioteca" import "módulo especifico que deseja importar"

import math #importa a biblioteca math de python
#a biblioteca permite operações matemáticas mais complexas

from math import sqrt #importo apenas a função sqrt

from math import floor, ceil #importa apenas funções específicas da biblioteca

#ceil --> arredonda pra cima
#floor --> arredonda para baixo
#trunc --> eliminar da vírgula pra frente
#pow --> potência
#sqrt --> raiz 
#factorial --> fatorial

#Prática

num = int(input('Digite um número: '))

raiz = math.sqrt(num)

print('A raiz de {} é igual a {}'.format(num , raiz))
print('A raiz de {} é igual a {}'.format(num , ceil(raiz))) #Arredonda pra cima
print('A raiz de {} é igual a {}'.format(num , floor(raiz))) #Arredonda pra baixo

#python.org --> pesquisar sobre bibliotecas, e encontrar outras bibliotecas

import random #colocar antes do código, apenas coloquei para dividir a aula

num1 = random.randint(1, 10) #Cria um número inteiro aleatório de 1 a 10
print(num)

import emoji

print(emoji.emojize('Python is :thumbs_up:'))










