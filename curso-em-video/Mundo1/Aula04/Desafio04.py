#Desafio 1 - Crie um script Python que leia o nome de uma pessoa e mostre uma mensagem de boas-vindas de acordo com o valor digitado.

nomeDesafio = input('Qual o seu nome? ');
print('Olá ' + nomeDesafio + '! Prazer em te conhecer!');

#Desafio 2 - Crie um script Python que leia o dia, o mês e o ano de nascimento de uma pessoa e mostre uma mensagem com a data formatada.

dia = input('Qual o dia do seu nascimento? ');
mes = input('Qual o mês do seu nascimento? ');
ano = input('Qual o ano do seu nascimento? ');

print('Você nasceu no dia ' + dia + ' de ' + mes + ' de ' + ano + '.');

#Desafio 3 - Crie um script Python que leia dois números e tente mostrar a soma entre eles.

num1 = input('Digite um número:');
num2 = input('Digite outro número:');

res = int(num1) + int(num2);#Converte os números para inteiros 

print('O resultado da some entre os dois valores é: ' , res);



