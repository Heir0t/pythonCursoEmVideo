import random
import time

vitoria = False

print('Jokenpô contra máquina')
time.sleep(1)

print('Escolha')
print('1 - Pedra')
print('2 - Papel')
print('3 - Tesoura')
humanInput = int(input(''))

match humanInput:
    case 1: 
        humanDecision = 'Pedra'
    case 2:
        humanDecision = 'Papel'
    case 3:
        humanDecision = 'Tesoura'
    case _:
        print('Decisão inválida')
        exit()

machineInput = random.randint(1, 3)

match machineInput:
    case 1: 
        machineDecision = 'Pedra'
    case 2:
        machineDecision = 'Papel'
    case 3:
        machineDecision = 'Tesoura'

print('Jo...')
time.sleep(1)
print('Ken...')
time.sleep(1)
print('Po\n')
time.sleep(0.5)

print(f'Você: {humanDecision}')
print(f'CPU: {machineDecision}\n')

if humanDecision == machineDecision:
    print('Empate')
else:
    if humanDecision == 'Pedra':
        if machineDecision == 'Tesoura':
            vitoria = True
    elif humanDecision == 'Papel':
        if machineDecision == 'Pedra':
            vitoria = True
    else:
        if machineDecision == 'Papel':
            vitoria = True

if vitoria:
    print('Parabéns...')
    print('Você venceu!\n')
else:
    print('Você perdeu')
    print('Boa sorte na próxima\n')
   
        
