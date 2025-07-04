#calcule a soma entre todos os números impares que são multiplos de 3 e que estão entre 1 até 500

soma = int(0)

for c in range(1, 500):
    if c %2 != 0 and c %3 == 0:
        soma += c
print(soma)
