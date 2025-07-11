#Condições aninhadas

nome = str(input('Qual é seu nome: '))

if nome == 'Heitor':
    print('Belo nome')
elif nome == 'João' or nome == 'Maria' or nome == 'Paulo':
    print('Seu nome é bem popular no Brasil ')
elif nome == 'Davi':
    print('Você é da india')

print('Tenha um ótimo dia {}'.format(nome)) 