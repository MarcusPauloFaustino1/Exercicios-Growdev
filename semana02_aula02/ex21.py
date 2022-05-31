'''Crie um algoritmo que funcione como um jogo de loteria, conforme as seguintes
regras:
a) O algoritmo deve gerar três números aleatórios entre 0 e 9;
b) O usuário deve fornecer um palpite com três números, também entre 0 e 9;

c) Cada um dos palpites do usuário deve ser comparado com os números
aleatórios, de acordo com a tabela abaixo:

Números Correspondentes                  Número de pontos
Nenhum número coincidente                       0

Acertar um número                              10

Acertar dois números                          100

Acertar os três números, 
mas não na mesma ordem em
que foram gerados                            1000

Acertar três números 
na mesma ordem que 
os números aleatórios                   1.000.000'''

import random
from time import sleep

print(f'{"JOGO DE LOTERIA":=^40}')
print('\n        Faça sua aposta!\n')
print('Escolha três números entre 0 e 9: ')
n1 = int(input('1º Número: '))
n2 = int(input('2º Número: '))
n3 = int(input('3º Número: '))

if n1 == n2 == n3 or n1 == n2 or n1 == n3 or n2 == 3:
    print('Não é permitido repetir números!')
    exit()

x = random.sample(range (10), 3)

print('SORTEANDO...')
sleep(2)
print(f'\n{"_":_^40}\n')
print(f'Números sorteados {x}')
print(f'\n{"_":_^40}\n')


erro1 = 10
erro2 = 10
erro3 = 10

try:
    x1 = x.index(n1)
except ValueError:
    erro1 = 0
try:
    x2 = x.index(n2)
except ValueError:
    erro2 = 0
try:
    x3 = x.index(n3)
except ValueError:
    erro3 = 0

if erro1 + erro2 + erro3 == 0:
    print('Infelizmente você errou todas!\n\nPrêmio: 0 ponto')
    print(f'\n{"=":=^40}\n')
    exit()
elif erro1 + erro2 + erro3 == 10:
    print('Parabéns, você acertou UM número!\n\nPrêmio: 10 pontos')
    print(f'\n{"=":=^40}\n')
    exit()
elif erro1 + erro2 + erro3 == 20:
    print('Parabéns, você acertou DOIS números!\n\nPrêmio: 100 pontos')
    print(f'\n{"=":=^40}\n')
    exit()

x1 = x.index(n1)
x2 = x.index(n2)
x3 = x.index(n3)

if x1 == 0 and x2 == 1 and x3 == 2:
    print('\n!!!!!!!PARABÉNS!!!!!!\nVocê acertou os TRÊS números na SEQUÊNCIA EXATA!\n\nPrêmio (máximo): 1.000.000 pontos!!!')
    print(f'\n{"=":=^40}\n')
elif (x1 <= 2 and x1 >= 0) and (x2 <= 2 and x2 >= 0) and x3 <= 2 and x3 >= 0:
    print('Parabéns, você acertou os TRÊS números!\n\nPrêmio: 1.000 pontos!!!')
    print(f'\n{"=":=^40}\n')
