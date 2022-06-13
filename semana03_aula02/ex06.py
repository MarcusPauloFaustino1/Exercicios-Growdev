'''Crie um programa que leia continuamente a altura e o sexo de uma lista de
pessoas salvando todas as informações em listas, até que uma altura
negativa seja fornecida. Ao final, sabendo que a média de altura para as
mulheres brasileiras é de 1.60m e a dos homens brasileiros é de 1.73m,
escreva as seguintes informações:
a) quantas mulheres da lista estão acima da média nacional de altura
para mulheres, e quantas estão abaixo;
b) quantos homens da lista estão acima da média nacional de altura para
homens, e quantos estão abaixo.'''

from ast import Return


alturaF = []
alturaM = []
alturaf = []
alturam = []
altura = 1
mediaF = 1.6
mediaM = 1.73

while altura > 0:
    altura = float(input('Digite a altura: '))
    if altura < 0:
        break
    sexo = input('Digite o sexo (M/F): ')
    
    if sexo in 'M' and altura > 1.73:
        alturaM.append(altura)
    elif sexo in 'M' and altura < 1.73:
        alturam.append(altura)
    elif sexo in 'F' and altura > 1.6:
        alturaF.append(altura)
    elif sexo in 'F' and altura < 1.6:
        alturaf.append(altura)

print(f'Mulheres com altura acima da média: {len(alturaF)}')
print(f'Mulheres com altura abaixo da média: {len(alturaf)}')
print(f'Homens com altura acima da média: {len(alturaM)}')
print(f'Homens com altura acima da média: {len(alturam)}')
