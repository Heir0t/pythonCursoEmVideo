#Crie um programa que leia o ano de nascimento de sete pessoas. No final mostre quantas não atingiram a maioridade e quantas já são maiores.

maioridade: int = 0
menoridade: int = 0
anoAtual: int = 2025

for i in range(1, 8):
    dataNasc = int(input('Digite o ano em que você nasceu: '))
    idade = anoAtual - dataNasc
    if idade > 0 and idade < 21:
        menoridade+=1
    elif idade >= 21 and idade < 120:
        maioridade+=1
    else:
        print('Idade inválida')
        print('Tente novamente')
        i-=1
    
print(f'{maioridade} pessoas estão na maioridade')
print(f'{menoridade} pessoas estão na menoridade')

