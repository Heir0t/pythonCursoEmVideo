#Repetições controladas 
#for
#laço com variável de controle

#Em português 
#laço c intervalo(1,10)
    #passo
#pega

takeApple = bool(False)
step = int(0)

for c in range(1,10):
    step+1; #Lembrar que não tem ++
take = True
print(f'Você deu {step} passos, e pegou a maçã')

takeApple = False
step = 0
hasCoin = bool(False)
takeCoin = bool(False)
jump = int(0)

#Em português

#laço c intervalo(0,3)
    #se moeda = true
        #pega
    #passo
    #pula
#passo
#pega

for c in range(0,3):
    if hasCoin:
        takeCoin = True
    step+1
    jump+1
step+1
take = True

# - - - - - - - - - - - - - 
#pratica

for c in range(1, 6):# 1 a 5
    print(c)
print('FIM')

for c in range(6,0,-1):#Do 6 ao 0
    print(c)
print('FIM')

i = int(input('Inicio: '))
f = int(input('Fim: '))
p = int(input('pulando de: '))

for c in range(i, f+1, p):
    print(c)