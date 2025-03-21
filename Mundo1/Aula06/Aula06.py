#Tipos primitivos

#para de botar essas sugestões no meu código ia de merda
#não é pq eu sou iniciante que eu sou burro

#Definindo o tipo no input
n1 = int(input('Digite um número: '));
print(n1);

#Definindo o tipo na impressão
n1 = input('Digite um número:');
print(int(n1));

#int --> número inteiro --> 7, -4, 0, 9875
#float --> número real --> 4.5, 0.076, -15.223, 7.0
#bool --> valor lógico/booleano --> True, False
#str --> cadeia de caracteres/texto --> 'Olá', '7.5', ''

print('A soma vale{}'.format(5+3));

#Prática

n1 = input('Digite um número:');
print(type(n1));#É uma string

n2 = int(input('Digite outro número:'));
print(type(n2));#É um número inteiro

num1 = int(input('Digite um número:'));
num2 = int(input('Digite outro número:'));
s = num1 + num2;

#Tipo de formatação de string mais simples
print('A soma entre {} e {} vale {}'.format(num1, num2, s));

n = float(input('Digite um número:'));

print(n);
print(type(n)); #Número real/float

nTwo = bool(input('Digite um valor:'));

print(nTwo);
print(type(nTwo));#Booleano

nThree = str(input('Digite um valor:'));

print(nThree);
print(type(nThree));#String

print = ('Digite algo: ');

print(n.isnumeric());#Verifica se é um número
print(n.isalpha());#Verifica se é uma letra
print(n.isalnum());#Verifica se é alfanumérico (número e letra)
print(n.isupper());#Verifica se está em maiúsculo
print(n.islower());#Verifica se está em minúsculo
print(n.isspace());#Verifica se é um espaço
print(n.istitle());#Verifica se é um título
print(n.isdigit());#Verifica se é um dígito
print(n.isdecimal());#Verifica se é um decimal
print(n.isidentifier());#Verifica se é um identificador
print(n.isprintable());#Verifica se é imprimível
print(n.isascii());#Verifica se é ascii
#E mais...

