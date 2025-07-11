# Cores no terminal

# Padrão ANSI

# \033[style;text;backgorundm

# Ex: \033[0;33;44m

# Style
# 0 --> none
# 1 --> negrito
# 4 --> underline
# 7 --> negative

# Text
# 30 --> branco
# 31 --> vermelho
# 33 --> amarelo
# 34 --> azul
# 35 --> roxo
# 36 --> ciano
# 37 --> cinza

# Background
# 40 --> branco
# 41 --> vermelho
# 43 --> amarelo
# 44 --> azul
# 45 --> roxo
# 46 --> ciano
# 47 --> cinza

# ---------------------------------

# Prática

print('\033[31;43mOlá, Mundo!\033[m')

print('\033[0;30;44mCurso em vídeo\033[m')

a = 3
b = 4

print('Os valores são \033[32m{} \033[me \033[33m{}\033[m'.format(a, b))

nome = 'Heitor'

print('Olá prazer em te conhecer {}{}{}'.format('\033[4;34m', nome, '\033[m'))

cores = {'limpa': '\033[m', 
         'azul': '\033[34m',
         'amarelo': '\033[33m', 
         'preto&branco': '\033[7;30m'
         }

print('Olá prazer em te conhecer {}{}{}'.format(cores['preto&branco'], nome, cores['limpa']))