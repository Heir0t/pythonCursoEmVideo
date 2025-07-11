#Desenvolver um programa que leia 6 números inteiros e mostre a soma apenas daqueles que forem pares. Se o valor digitado for impar, desconsidere-o.

soma: int = 0

for i in range(1, 7):
    num =  int((input(f'Digite o {i}º número inteiro: ')))
    if num %2 == 0:
        soma += num

if soma !=0:
    print(f'A soma dos números é igual a: {soma}')
else:
    print('Nenhum número declarado ')
