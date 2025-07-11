#Strings

#strings sempre dentro de aspas

#cria espaços na memória, onde são armazenados o caracteres

# - - - - - - - - -

#operações com string

#fatiamento

frase = 'curso em vídeo de python'

print(frase[9]) #Irá imprimir o 9º caractere

#python é sensível à caixa 

print(frase[9:13]) #irá imprimir do 9º (inclusive) ao 13º caractere

#O ultimo caractere não entra na contagem

print(frase[9:21])

print(frase[9:21:2]) #vai do 9 até  o 20 pulando de 2 em 2

print(frase[:5]) #vai do caractere 0 até o 4

print(frase[15:]) #vai do 15 até o final

print(frase[9::3]) #vai começar do 9 até o final e pula de 3 em 3 

# - - - - - 

#Análise

print(len(frase)) #mostra o comprimento da frase

print(frase.count('o')) #mostra quantas vezes aparece um caractere, no caso 'o'

print(frase.count('o', 0,13)) #mostra a quantidade, mas aoenas do caractere 0 até o 13

# - - - - - 

print(frase.find('deo')) #procura pela cadeia indicada, e mostra a posição
#se o retorno for -1 não há cadeia

print('curso' in frase) #modo mais simples de procurar, indica true ou false

# - - -  - -

#transformação

print(frase.replace('python', 'curso')) #troca determinada palavra

print(frase.upper())#faz a cadeia de caracteres ficar em maiúsculo

print(frase.lower())#transforma os caracteres em minusculos

#parenteses no final pois é um método

print(frase.capitalize())#Deixa apenas o primeiro caractere em maiúsculo

print(frase.title())#identifica os espaços, e deixa as primeiras letras de todas as palavras em maiúsculas

newFrase = "   aprenda python  "

print(newFrase.strip())#remove espaços inuteis, antes e depoi de uma frase

print(newFrase.rstrip())#remove os espaços apenas da direita

print(newFrase.lstrip())#remove os espaços apenas da esquerda

# - - - - 

#divisão

print(frase.split())#Vai dividir as palavras em strings separadas baseando se nos espaços
#separa as palvras em listas numeradas

#Junção

print('-'.join(frase))#Vai juntar frase novamente