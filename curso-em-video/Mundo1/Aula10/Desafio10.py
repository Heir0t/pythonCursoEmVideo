
#1. **Desafio 28**: Escreva um programa que faça o computador "pensar" em um número inteiro entre 0 e 5 e peça para o usuário tentar descobrir qual foi o número escolhido pelo computador. O programa deverá escrever na tela se o usuário venceu ou perdeu.

import random

numUser = int(input('Digite um número entre 0 e 5: '))
numCerto = random.randint(0, 5)

if numUser == numCerto:
    print('Você acertou o número')
    print('Parabéns')
else:
    print('Errou! Tente novamente')
    

#2. **Desafio 29**: Escreva um programa que leia a velocidade de um carro. Se ele ultrapassar 80 km/h, mostre uma mensagem dizendo que ele foi multado. A multa vai custar R$ 7,00 por cada km acima do limite.

limitVel = 80

vel = float(input('Qual a velocidade do carro (Km/h)? '))

if vel > 80:
    acmLimit = vel - limitVel
    multa = acmLimit * 7
    print('Você foi multado!')
    print('A multa foi de: R${:.2f} '.format(multa))

else:
    print('Velocidade dentro do limite!')
    print('Continue assim :)')


#3. **Desafio 30**: Crie um programa que leia um número inteiro e mostre na tela se ele é par ou ímpar.

num = int(input('Digite um número (irei verificar se é par ou ímpar)'))

if num % 2 == 0:
    print('O número é par')
else:
    print('O número é ímpar')

#4. **Desafio 31**: Desenvolva um programa que pergunte a distância de uma viagem em km. Calcule o preço da passagem, cobrando R$ 0,50 por km para viagens de até 200 km e R$ 0,45 para viagens mais longas.

disViagem = float(input('Qual a distância da viagem? '))

if disViagem <= 200 and disViagem > 0:
    precFinal = disViagem * 0.5
    print('A passagem vai custar R${:.2f}'.format(precFinal))
elif disViagem > 200:
    precFinal = disViagem * 0.45
    print('A passagem vai custar R${:.2f}'.format(precFinal))
else:
    print('Número inválido')

#5. **Desafio 32**: Faça um programa que leia um ano qualquer e mostre se ele é bissexto.

ano = int(input('Digite o ano que deseja verificar: '))

if ano % 4 == 0:
    print('O ano é bissexto')
else:
    print('O ano não é bissexto')

#6. **Desafio 33**: Faça um programa que leia três números e mostre qual é o maior e qual é o menor.
maior = float('-inf')
menor = float('inf')

for i in range(3):
    num = int(input('Digite o {}º número: '.format(i+1)))
    if num > maior:
        maior = num
    if num < menor:
        menor = num
    
print('O maior número é: {}, e o menor é {}'.format(maior, menor))


#7. **Desafio 34**: Escreva um programa que pergunte o salário de um funcionário e calcule o valor do seu aumento. Para salários superiores a R$ 1.250,00, calcule um aumento de 10%. Para os inferiores ou iguais, o aumento é de 15%.

salario = float(input('Digite o valor do seu salário: '))

if salario <= 1250:
    aumento = salario * 0.15
    salFinal = salario + aumento
    print('Seu aumento foi de R${:.2f}, agora seu salário é {:.2f}'.format(aumento, salFinal))
elif salario > 1250:
    aumento = salario * 0.1
    salFinal = salario + aumento
    print('Seu aumento foi de R${:.2f}, agora seu salário é {:.2f}'.format(aumento, salFinal))
else: 
    print('Valor inválido')
#8. **Desafio 35**: Desenvolva um programa que leia o comprimento de três retas e diga ao usuário se elas podem ou não formar um triângulo.

lado1 = int(input('Digite o lado de um triângulo: '))
lado2 = int(input('Digite o lado de um triângulo: '))
lado3 = int(input('Digite o lado de um triângulo: '))

if lado1 != 0 and lado2 != 0 and lado3 != 0:
    if lado1 + lado2 > lado3 and lado1 + lado3 > lado2 and lado2 + lado3 > lado1:
        print('Os lados formam um triângulo! ')
    else:
        print('Estas retas não formam um triângulo ')
else:
    print('Estas retas não formam um triângulo')