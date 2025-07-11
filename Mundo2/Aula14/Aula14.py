#Repetições while
#São repetições baseadas em condições
#Geralmente usado quando não sabemos quantas repetições iremos precidar


c = 1
par = impar = 0

while c < 10:
    print(c)
    c+=1
print('fim')
#Aqui eu sei um limite

num = int(1)

while num != 0:
    num = int(input('Digite um valor: '))
    if num != 0:
        if num%2 == 0:
            par+=1
        else:
            impar+=1

print(f'Você digitou {par} números pares')
print(f'Você digitou {impar} números ímpares')

print('Fim')
#Aqui ele repete até que eu digite 0, ou seja, não sei quantas vezes ele vai repetir





