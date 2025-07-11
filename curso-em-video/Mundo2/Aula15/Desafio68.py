import random

while True:
    decisao = input('Impar ou Par? ').strip().lower()
    while decisao not in ['impar', 'par']:
        decisao = input('Digite apenas "Impar" ou "Par": ').strip().lower()

    numJogador = int(input('Digite o número que deseja jogar: '))
    numMaquina = random.randint(1, 11)

    soma = numJogador + numMaquina
    resultado = 'par' if soma % 2 == 0 else 'impar'

    print(f'Você: {numJogador}')
    print(f'Máquina: {numMaquina}')
    print(f'Soma: {soma} -> {resultado}')

    if resultado == decisao:
        print('Você venceu!\n')
    else:
        print('Você perdeu!\nFim do jogo.')
        break
