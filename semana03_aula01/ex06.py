'''Em uma eleição presidencial existem quatro candidatos. Os votos são
informados através de códigos. Os dados utilizados para a contagem dos
votos obedecem à seguinte codificação:
a) 1,2 = voto para os respectivos candidatos
b) 3 = voto nulo
c) 4 = voto em branco;
Elabore um programa que leia o código de votação de 5 eleitores. Calcule
e escreva:

a) total de votos para cada candidato
b) total de votos nulos
c) total de votos em branco'''

from time import sleep


print(f'\n{"ELEIÇÕES":=^60}\n')

candidato1 = 1
candidato2 = 2
candidato3 = 11
candidato4 = 12


votoNulo = 3

votoBranco = 4

listaBranco = []
listaNulo = []
lista1 = []
lista2 = []
lista3 = []
lista4 = []
votoTotal = 0

for n in range( 1, 6 ):
    voto = int(input('Digite seu voto: '))
    if voto == 4:
        listaBranco.append(n)
    elif voto == 3:
        listaNulo.append(n)
    elif voto == 1:
        lista1.append(n)
    elif voto == 2:
        lista2.append(n)
    elif voto == 11:
        lista3.append(n)
    else:
        lista4.append(n)

print('CONFERINDO VOTOS...')
sleep(2)
print(f'\n{"_"*60}\n')

print(f'\nVotos em branco:     {" ":>12}{len(listaBranco)}\n')

print(f'\nVotos nulos:         {" ":>12}{len(listaNulo)}\n')

print(f'\nVotos no candidato 1:  {" ":>10}{len(lista1)}\n')

print(f'\nVotos no candidato 2:  {" ":>10}{len(lista2)}\n')

print(f'\nVotos no candidato 3:  {" ":>10}{len(lista3)}\n')

print(f'\nVotos no candidato 4:  {" ":>10}{len(lista4)}\n')

print(f'\n{"="*60}\n')
