'''Crie uma estrutura bidimensional utilizando listas com sublistas para para
representar um tabuleiro (1 lista com 20 elementos e cada elemento é uma
lista de 20 elementos, tabuleiro 20x20). Cada posição irá armazenar 1 valor
numérico que significa:
0 - Água
1 - Navio

Para cada posição escolha esses valores aleatoriamente, respeitando a regra
de que não podem existir mais de 20 navios no tabuleiro. Após os valores
serem distribuídos, o programa deve pedir ao usuário uma posição do
tabuleiro e informar se ele acertou um navio ou água e repetir o procedimento
até que o usuário derrote todos os navios ou chegue ao limite de 35
tentativas.'''


import random



tabuleiro = []

for i in range (0, 20):
    tab = [0]*20
    w = random.randint(0, 19)
    tab[w] = 1
    tabuleiro.append(tab)

cont = 0
acertos = 0
print(tabuleiro)

while cont <= 35 and acertos <= 20:
    x = int(input('Para determinar a posição na linha digite um valor de 0 a 19: '))
    y = int(input('Para determinar a posição na coluna digite um valor de 0 a 19: '))
    if tabuleiro[x][y] == 1:
        print('Você acertou um navio!')
        acertos += 1
        tabuleiro[x][y] = 0
    elif tabuleiro[x][y] == 0:
        print('Você acertou a água!')
    