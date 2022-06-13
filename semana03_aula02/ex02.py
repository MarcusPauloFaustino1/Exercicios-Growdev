'''Faça um programa que peça o nome e as duas notas de 5 alunos, calcule a
média das notas e armazene nome e média cada uma em uma lista, ao final
imprima o nome e o número de alunos com média maior ou igual a 7.0.'''

listaMedia = []
listaNome = []



for i in range (5):
    nome = input('Digite o nome: ')
    n1 = float(input('Digite a nota 1: '))
    n2 = float(input('Digite a nota 2: '))
    media = (n1 + n2) / 2
    if media >= 7:
        listaNome.append(nome)
        listaMedia.append(media)

print(f'{len(listaNome)} Aprovados: ')

for i in range (len(listaNome)):
        print(listaNome[i])
