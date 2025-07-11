# Desafio 36: Escreva um programa para aprovar o empréstimo bancário para a compra de uma casa.
# O programa deve perguntar o valor da casa, o salário do comprador e em quantos anos ele vai pagar.
# Calcule o valor da prestação mensal, sabendo que ela não pode exceder 30% do salário ou então o empréstimo será negado.

valCasa = float(input('Digite o valor da casa que deseja comprar: '))
salario = float(input('Digite seu salário mensal: '))
anosPPag = int(input('Digite em quantos anos irá pagar: '))

mesesPPag = anosPPag * 12
prest = valCasa/mesesPPag

if prest < salario*0.3:
    print('Empréstimo aprovado')
    print('A prestação será de R${:.2f} por mês'.format(prest))
else:
    print('Empréstimo negado')

# Desafio 37: Escreva um programa que leia um número inteiro qualquer e peça para o usuário escolher qual será a base de conversão:
# 1 para binário, 2 para octal e 3 para hexadecimal.

num = int(input('Digite o valor que deseja converter: '))

res = int(input('Digite para qual tipo deseja converter: (1 - binário, 2 - octal, 3 - hexadecimal)'))

if(res == 1):
    print('{} em binário fica: {}'.format(num, bin(num)))
elif(res == 2):
    print('{} em octal fica: {}'.format(num, oct(num)))
elif(res == 3):
    print('{} em hexadecimal fica: {}'.format(num, hex(num)))
else:
    print('Opção inválida')

# --> está respondida corretamente, possivel que o problema seja no VScode
    
# Desafio 38: Escreva um programa que leia dois números inteiros e compare-os, mostrando na tela uma mensagem:
# - O primeiro valor é maior
# - O segundo valor é maior
# - Não existe valor maior, os dois são iguais

n1 = int(input('Digite o primero número: '))
n2 = int(input('Digite o valor do segundo número: '))

if n1 > n2:
    print('O primeiro valor é maior')
elif n2 > n1:
    print('O segundo número é maior')
else:
    print('Os dois possuem o mesmo valor')

# Desafio 39: Faça um programa que leia o ano de nascimento de um jovem e informe, de acordo com sua idade:
# - Se ele ainda vai se alistar ao serviço militar.
# - Se é a hora de se alistar.
# - Se já passou do tempo do alistamento.
# Seu programa também deverá mostrar o tempo que falta ou que passou do prazo.

dataNasc = int(input('Digite o ano que você nasceu: '))
anoAtual = 2025

idade = anoAtual - dataNasc

if idade == 18:
    print('Hora de se alistar')
elif idade < 18 and idade > 0:
    anoAlist = 18 - idade
    if anoAlist == 1:
        print('Você vai se alistar daqui a 1 ano')
    else: 
        print('Você vai se alistar daqui a {} anos'.format(anoAlist))
elif idade > 18:
    print('Já passou da idade de se alistar')
else:
    print('Idade inválida, verifique se preencheu corretamente a data de nascimeto')

# Desafio 40: Crie um programa que leia duas notas de um aluno e calcule sua média, mostrando uma mensagem no final:
# - Média abaixo de 5.0: REPROVADO
# - Média entre 5.0 e 6.9: RECUPERAÇÃO
# - Média 7.0 ou superior: APROVADO

nota1 = float(input('Digite a primera nota: '))
nota2 = float(input('Digite a segunda nota: '))

media = (nota1 + nota2)/2

if media < 5:
    print('Reprovado')
elif media >= 5 and media <= 6.9:
    print('Recuperação')
else:
    print('Aprovado')

# Desafio 41: A Confederação Nacional de Natação precisa de um programa que leia o ano de nascimento de um atleta e mostre sua categoria:
# - Até 9 anos: MIRIM
# - Até 14 anos: INFANTIL
# - Até 19 anos: JÚNIOR
# - Até 25 anos: SÊNIOR
# - Acima de 25 anos: MASTER

nascData = int(input('Digite o ano em que nasceu: '))

idade = anoAtual - nascData

if idade <= 9:
    print('Mirim')
elif idade > 9 and idade <= 14:
    print('Infantil')
elif idade > 14 and idade <= 19:
    print('Júnior')
elif idade > 19 and idade <= 25:
    print('Sênior')
elif idade > 25:
    print('Master')

# Desafio 42: Refaça o DESAFIO 35 dos triângulos, acrescentando o recurso de mostrar que tipo de triângulo será formado:
# - Equilátero: todos os lados iguais
# - Isósceles: dois lados iguais
# - Escaleno: todos os lados diferentes

lado1 = int(input('Digite o lado de um triângulo: '))
lado2 = int(input('Digite o lado de um triângulo: '))
lado3 = int(input('Digite o lado de um triângulo: '))

if lado1 != 0 and lado2 != 0 and lado3 != 0:
    if lado1 + lado2 > lado3 and lado1 + lado3 > lado2 and lado2 + lado3 > lado1:
        print('Os lados formam um triângulo! ')
        ehTriangulo = True
    else:
        print('Estas retas não formam um triângulo ')
        ehTriangulo = False
else:
    print('Estas retas não formam um triângulo')
    ehTriangulo = False

if ehTriangulo:
    if lado1 == lado2 and lado2 == lado3:
        print('Triângulo equilátero')
    elif lado1 == lado2 or lado2 == lado3 or lado1 == lado3:
        print('Triângulo isósceles')
    else:
        print('Triângulo escaleno')

# Desafio 43: Desenvolva uma lógica que leia o peso e a altura de uma pessoa, calcule seu Índice de Massa Corporal (IMC) e mostre seu status:
# - Abaixo de 18.5: Abaixo do peso
# - Entre 18.5 e 25: Peso ideal
# - 25 até 30: Sobrepeso
# - 30 até 40: Obesidade
# - Acima de 40: Obesidade mórbida

peso = float(input('Digite seu peso(kg):'))
altura = float(input('Digite sua altura(m):'))
imc = peso/altura**2
print(f'Seu IMC é {imc:.2f}')

# Desafio 44: Elabore um programa que calcule o valor a ser pago por um produto, considerando o seu preço normal e condição de pagamento:
# - À vista dinheiro/cheque: 10% de desconto
# - À vista no cartão: 5% de desconto
# - Em até 2x no cartão: preço normal
# - 3x ou mais no cartão: 20% de juros

valorProduto = float(input('Digite o valor do produto:'))
print('Escolha a forma de pagamento:')
print('1 - À vista dinheiro/cheque')
print('2 - À vista no cartão')
print('3 - Até 2x no cartão')
print('4 - 3x ou mais')

metodoPag = int(input(''))

match metodoPag:
    case 1:
        valorFinal = float(valorProduto + (valorProduto * 0.10))
        print(f'Você irá pagar R${valorFinal:.2f}')
    case 2:
        valorFinal = float(valorProduto + (valorProduto * 0.05))
        print(f'Você irá pagar R${valorFinal:.2f}')
    case 3:
        valorFinal = float(valorProduto/2)
        print(f'Você irá pagar duas parcelas de R${valorFinal:.2f}')
    case 4:
        numParc = int(input('Em quantas parcelas deseja pagar?(3x ou mais)'))
        if  numParc > 3:
            valorFinal = valorProduto/numParc
            print(f'Você irá pagar {numParc} parcelas de R${valorFinal:.2f}')
        else:
            print('Apenas 3 parcelas ou mais')
            exit()

# Desafio 45: Crie um programa que faça o computador jogar Jokenpô com você

# Resposta no arquivo separado
    

