#Condições
#Simples
#Compostas 

tempo = int(input('Quantos anos tem seu carro?'))

if tempo <= 3:
    print('Carro novo')

else:
    print('Carro velho')

print('carro novo' if tempo <=3 else 'carro velho') #Representa os operadores ternários que não existem em python

nome = str(input('Qual seu nome?'))

#Os condicionais em python se baseiam em identação, tem q estar um tab a frente para ser executado
#Se estiver sem este tab não faz parte do condicional

if nome == 'Heitor':
    print("Belo nome")
   
print('Bom dia {}'.format(nome))


n1 = float(input('Primeira nota: '))
n2 = float(input('Segunda nota: '))

media = (n1 + n2)/2

print('A média da nota foi: {}'.format(media))

if media < 6:
    print('Sua média foi ruim, estude mais')

elif media ==6:
    print('Sua média foi literalmente a média')

else:
    print('Sua média foi boa')
    print('Não fez mais que sua obrigação')
