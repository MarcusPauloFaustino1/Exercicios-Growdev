import random

jogo_gerad = []
jogo_user = []
acertos = []
indice = 1
pontos = 0

while indice < 4:
    jogo_user.append(int(input(f'Digite o {indice}º de 3 para o sorteio: regras -> [digite de 0 até 9] \n')))
    jogo_gerad.append(random.randint(0,9))
    indice += 1

print('')
print('____________')

if (jogo_gerad[0] == jogo_user[0]) and (jogo_gerad)
