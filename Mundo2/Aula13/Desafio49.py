#refaça o desafio 9, mostrando a tabuada de um número que o usuário escrever usando for

num = int(input("Digite o número inteiro que deseja descobrir a tabuada: "))

res = int(0)

for c in range(1, 11):
    res = num * c
    print(f'{num} x {c} = {res}')

