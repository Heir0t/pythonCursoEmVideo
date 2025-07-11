#Desenvolva um programa que leia o nome, idade e sexo de 4 pessoas. No final do programa, mostre: A media da idade, o nome do homem mais velho, e quantas mulheres tem menos de 20 anos

media = float(0)
homemMaisVelho: str
idadeHomemMaisVelho = int(0)
mulheresComMenosDeVinte = int(0)
maior = int(0)
soma = float(0)
media = float(0)

for i in range(1, 5):
    nome = str(input('Digite seu nome: '))
    sexo = str(input('Digite seu sexo: ')).lower()
    idade = int(input('Digite sua idade: '))

    if sexo == 'homem' and idade > maior:
        maior = idade
        homemMaisVelho = nome
        idadeHomemMaisVelho = idade

    if sexo == 'mulher' and idade < 20:
        mulheresComMenosDeVinte+=1

    soma += idade

media = soma/i

print(f'A média de idade é: {media}')
print(f'O homem mais velho é o {homemMaisVelho} e tem {idadeHomemMaisVelho} anos')
print(f'{mulheresComMenosDeVinte} mulheres possuem menos de vinte anos')





