#Desafio 22 - Cire um programa que leia o nome completo de um apessoa e exiba:
#o nome com todas a letras maiusculas
#todas minusculas 
#quantas letras, sem considerar espaços q
#quantas letras tem o primeiro nome

nome = str(input('Qual o seu nome completo?'))

print(nome.upper())
print(nome.lower())

print(len(nome.replace(" ", "")))

nom2 = nome.split()
print(nom2[0])