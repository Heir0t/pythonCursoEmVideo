#Desenvolva um programa que leia o primeiro termo e a razão de um PA. No final, mostre os 10 primeiros termos dessa progressão

primeiroTermo = int(input(('Digite o primeiro termo da progressão: ')))

razao = int(input('Digite a razão dessa PA: '))

primeiroTermo-=razao
for i in range(1, 11):
    primeiroTermo+=razao
    print(primeiroTermo)

    