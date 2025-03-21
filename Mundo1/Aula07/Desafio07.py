# Desafio 01 - Crie um programa que leia o nome de uma pessoa e mostre uma mensagem de boas-vindas
num = int(input('Digite um número inteiro: '))

sucessor = num + 1
antecessor = num - 1

print('O número digitado foi: {}, seu sucessor é: {}, seu antecessor é: {}'.format(
    num, sucessor, antecessor))

# Desafio 06 - Crie um algoritmo que leia um número e mostre o seu dobro, triplo  e raiz quadrada

num1 = float(input('Digite um número:'))
dobro = num1*2
triplo = num1*3
raiz = num1**(1/2)

print('O número é {}. seu dobro é {}, seu triplo é {} e sua raiz é {}'.format(
    num1, dobro, triplo, raiz))

# Desafio 07 - Desenvolva um programa que leia duas notas de um aluno e calcule a média

nota1 = float(input('Digite a primeira nota: '))
nota2 = float(input('Digite a segunda nota:'))
media = (nota1 + nota1) / 2

print('A média é {}'.format(media))

# Desafio 08 - Escreva um programa que leia um valor em metros e o exiba convertido em centímetros e milímetros

mts = float(input('Digite um valor em metros:'))
cm = mts * 100
mm = mts*1000
print('{}M são {}cm e {}mm'.format(mts, cm, mm))

# desafio 09 - Faça um programa que leia um número inteiro qualquer e mostre na tela a sua tabuada

numer = int(input('Digite um número inteiro:'))

i = 1

while i <= 10:
    print('{} x {} = {}'.format(numer, i, i*numer))
    i += 1

# Desafio 10 - Crie um programa que leia quanto dinheiro uma pessoa tem na carteira e mostre quantos dólares ela pode comprar

valDolar = 3.27  # cotação do dólar em 2018, ano em que o curso foi gravado

real = float(input('Digite quanto dinheiro você tem na carteira (em reais):'))

dolar = real/valDolar

print('Com R${:.2f} você pode comprar US${:.2f}'.format(real, dolar))

# Desafio 11 - Faça um programa que leia a largura e a altura de uma parede em metros, calcule a sua área e a quantidade de tinta necessária para pintá-la, sabendo que cada litro de tinta pinta uma área de 2m²

largura = float(input('Digite a largura da parede em metros:'))
altura = float(input('Digite a altura da parede em metros:'))

area = largura * altura

tintaLit = area/2

print('A área da parede é de {}m² e você precisará de {} litros de tinta para pintá-la'.format(area, tintaLit))

# Desafio 12 - Faça um algoritmo que leia o preço de um produto e mostre seu novo preço com 5% de desconto

preco = float(input('Digite o preço do produto:'))
desconto = preco*0.05
novoPreco = preco - desconto
print('O preço a ser pago é {}'.format(novoPreco))

# Desafio 13 - Faça um algoritmo que leia o salário de um funcionário e mostre seu novo salário com 15% de aumento

sal = float(input('Digite o salário do funcionário:'))
aumento = sal*0.15
salFinal = sal + aumento
print('O salário com o aumento ficou {}'.format(salFinal))
