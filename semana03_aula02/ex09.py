'''Modifique o programa anterior para exibir as seguintes estatísticas.
a) Acertos em água
b) Acertos em Navios
c) Porcentagem de acertos em água
d) Porcentagem de acertos em Navios
e) Acertos ininterruptos (maior quantidade de acertos em sequência)'''

import random
import collections


tabuleiro = []

for i in range (0, 20):
    tab = [0]*20
    w = random.randint(0, 19)
    tab[w] = 1
    tabuleiro.append(tab)

cont = 0
acertosNavios = 0
acertosAgua = 0
sequencia = 0
listaSequencia = []


while cont <= 35 and acertosNavios <= 20:
    x = int(input('Para determinar a posição na linha digite um valor de 0 a 19: '))

    y = int(input('Para determinar a posição na coluna digite um valor de 0 a 19: '))
    if tabuleiro[x][y] == 1:
        print('Você acertou um navio!')
        acertosNavios += 1
        tabuleiro[x][y] = 2
        cont += 1
        sequencia += 1
        listaSequencia.append(sequencia)
        while tabuleiro[x][y] == 2:
            x = int(input('Para determinar a posição na linha digite um valor de 0 a 19: '))
            y = int(input('Para determinar a posição na coluna digite um valor de 0 a 19: '))
            cont += 1
            if tabuleiro[x][y] == 1:
                acertosNavios += 1
                print('Você acertou um navio!')
                sequencia += 1
                cont += 1
                listaSequencia.append(sequencia)

    elif tabuleiro[x][y] == 0:
        
        print('Você acertou a água!')
        acertosAgua += 1 
        cont += 1
        sequencia = 0

print(listaSequencia)
print(f'a) Acertos em água: {acertosAgua}\nb) Acertos em Navios: {acertosNavios}\nc) Porcentagem de acertos em água: {(100 * acertosAgua) / 35}\nd) Porcentagem de acertos em Navios: {(100 * acertosNavios) / 35}\ne) Acertos ininterruptos: {max(listaSequencia)}')
