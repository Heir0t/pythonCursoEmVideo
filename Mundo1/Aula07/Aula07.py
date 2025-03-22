#Operadores aritméticos
# + adição
# - subtração
# * multiplicação
# / divisão
# ** potenciação
# // divisão inteira --> retorna a parte inteira da divisão
# % resto da divisão --> também chamado de módulo

#Ordem de precedência
# 1. ()
# 2. **
# 3. * , / , // e %
# 4. + e -

#Se sinais na mesma linha, a ordem de precedência é da esquerda para a direita

#3 * 5 + 4 ** 2 = 31
#3 * (5 + 4) ** 2 = 243
#Parenteses faz muita diferença

#OBS: o limite de números em python é infinito, mas a memória do computador é finita
#sendo assim, o limite de números depende da capacidade de memória do computador

#Prática

#Raiz quadrada
x = 81 ** (1/2)
print(int(x))

#interação de string com operadores aritméticos;

y = 'Olá\t'*5;
print(y);

z = '='*20;
print(z);

nome = input('Qual é o seu nome? ');
print('Prazer em te conhecer, {:20}!'.format(nome)); #escreve o nome em 20 espaços
print('Prazer em te conhecer, {:>20}!'.format(nome)); #escreve o nome em 20 espaços alinhado à direita
print('Prazer em te conhecer, {:<20}!'.format(nome)); #escreve o nome em 20 espaços alinhado à esquerda
print('Prazer em te conhecer, {:^20}!'.format(nome)); #escreve o nome em 20 espaços centralizado
print('Prazer em te conhecer, {:=^20}!'.format(nome)); #escreve o nome em 20 espaços centralizado com = no lugar de espaço vazio
# ':' para adicionar a mascara


#muitas opções de formatação de string
#python é incrível

n1 = int(input('Digite um número:'))
n2 = int(input('Digite outro número:'))

s = n1 + n2
m = n1 * n2
d = n1 / n2
di = n1 // n2
p = n1 ** n2

print('A soma vale: {}'.format(n1+n2)) 

print('A soma vale: {}, o produto vale: {} e a divisão vale: {}'.format(s, m, d))

print('Divisão inteira: {} e potência {}'. format(di, p))










