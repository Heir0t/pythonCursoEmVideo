frase = str(input('Digite uma frase: ')).strip().lower()
palavras = frase.split()
junto = ''.join(palavras)
#tirar os espaços

inverso = ''
for letra in range(len(junto) -1, -1, -1):
    inverso+=junto[letra]
print(inverso)
if inverso == junto:
    print('É um palindromo ')
else:
    print('Não é um palíndromo ')
    