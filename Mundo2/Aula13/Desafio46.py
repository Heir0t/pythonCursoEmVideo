#46 - Programa que mostra uma contagem regressiva na tela para o estouro de fogos de artificio, indo de 10 até 0, com uma pausa de  1 segundo entre eles

lancarFogos = bool(False)

for c in range (10, -1, -1):
    print(c)
    lancarFogos = True

if lancarFogos:
    print('Lançando uma saraivada de foguetes 🎆🎆🎆')

