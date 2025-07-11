import math
import random

#Desafio 16 - Crie um programa que leia um número real e mostre sua porção inteira

num = float(input('Digite um valor: '))
print('A porção inteira de {} é {}'.format(num, math.trunc(num)))
print('A porção inteira de {} é {}'.format(num, int(num))) #Também funciona

#Desafio 17 - Faça um programa que leia o comprimento do cateto oposto e do cateto adjacente de um trângulo retângulo
#calcule e mostre o comprimento da hipotenusa

#sem a bib math
co = float(input('Comprimento do cateto oposto: '))
ca = float(input('Comprimento do cateto adjacente: '))
hi = (co ** 2 + ca ** 2) ** (1/2)

#com a bib math
hi1 = math.sqrt(co**2 + ca**2)

#ou ainda
hip = math.hypot(co, ca)

print('res: {:.2f}'.format(hi))
print('res: {:.2f}'.format(hi1))
print('res: {:.2f}'.format(hip))


#Desafio 18 - Faça um programa que leia um ângulo qualquer e mostre o valor do seno, cosseno e tangente deste ângulo

ang = float(input('Digite um ângulo: '))
sin = math.sin(math.radians(ang))
cos = math.cos(math.radians(ang))
tan = math.tan(math.radians(ang))
#Realiza a conversão para radianos, assim a operação se torna correta

print('Seno: {:.2f}, cosseno: {:.2f}, tangente {:.2f}'.format(sin,cos,tan))

#Desafio 19 - Faça um programa que realiza um sorteio para um de quatro alunos apagar o quadro

aln1 = str(input('Digite o nome do aluno: '))
aln2 = str(input('Digite o nome do aluno: '))
aln3 = str(input('Digite o nome do aluno: '))
aln4 = str(input('Digite o nome do aluno: '))

alunos = [aln1, aln2, aln3, aln4] #Criar um array

apg = random.choice(alunos) #Faz uma escolha aleatória entre valores

print('O aluno que vai apagar o quadro é: {}'.format(apg))

#Desafio 20 - Faça um sorteio da ordem de apresentação de quatro alunos, e mostre a ordem sorteada

random.shuffle(alunos) #Ele muda a ordem de um array
print('A ordem será: ')
print(alunos)

