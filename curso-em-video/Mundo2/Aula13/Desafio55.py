#faça um programa que leia o peso de cinco pessoas. NO final mostra qual foi o maior e o menor peso lidos

maior: int = 0
menor: int = 0

for i in range(1,6):
    peso = float(input('Digite seu peso: '))
    if peso > maior:
        maior = peso
    if i == 1:
        menor = peso
    elif peso < menor:
        menor = peso

print(f'O menor peso digitado foi: {menor}')
print(f'O maior peso digitado foi {maior}')