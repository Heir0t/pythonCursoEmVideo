# Desafio 01 - Faça um programa que leia algo e mostre o seu tipo e todas as informações possíveis sobre ele.

var = input('Digite algo: ');
print('O tipo primitivo desse valor é: ', type(var));
print('Só tem espaços? ', var.isspace());
print('É um número? ', var.isnumeric());
print('É alfabético? ', var.isalpha());
print('É alfanumérico? ', var.isalnum());



