#Faça um programa que leia um número inteiro e diga se ele é ou não um número primo

contador: int = 0
num = int(input('Digite um número inteiro: '))

for i in range(1,num+1):
    if num%i == 0:
        contador+=1
        print(i)

if contador == 2:
    print('É primo! ')
else: 
    print('Não é primo! ')
