'''Faça um programa que leia as duas notas parciais obtidas por um aluno
numa disciplina ao longo de um semestre, e calcule a sua média. A atribuição
de conceitos obedece à tabela abaixo:

Média de Aproveitamento          Conceito
Entre 9.0 e 10.0                    A
Entre 7.5 e 8.9                     B
Entre 6.0 e 7.4                     C
Entre 4.0 e 5.9                     D
Entre 0 e 3.9                       E

O algoritmo deve mostrar na tela as notas, a média, o conceito
correspondente e a mensagem:
a) APROVADO se o conceito for A, B ou C.
b) REPROVADO se o conceito for D ou E.'''

#DADOS DE ENTRADA
print(f'\n{"=":=^40}\n')
print("Digite suas notas:")
n1 = float(input('Nota 1:'))
n2 = float(input('Nota 2:'))

#PROCESSAMENTO

media = (n1 + n2) / 2

#DADOS DE SAÍDA

print('----------------------------')

if media >= 9 and media <= 10:
    print(f'\nNota 1: {n1:.1f}\n\nNota 2: {n2:.1f}')
    print(f'\nMedia: {media:.1f}')
    print('\nConceito: A')
    print(f'\n{"_":_^40}\n')
    print(f'{"APROVADO":*^20}')
    print(f'\n{"=":=^40}\n')
elif media >= 7.5 and media <= 8.9:
    print(f'\nNota 1: {n1:.1f}\n\nNota 2: {n2:.1f}')
    print(f'\nMedia: {media:.1f}')
    print('\nConceito: B')
    print(f'\n{"_":_^40}\n')
    print(f'{"APROVADO":*^20}')
    print(f'\n{"=":=^40}\n')
elif media >= 6 and media <= 7.4:
    print(f'\nNota 1: {n1:.1f}\n\nNota 2: {n2:.1f}')
    print(f'\nMedia: {media:.1f}')
    print('\nConceito: C')
    print(f'\n{"_":_^40}\n')
    print(f'{"APROVADO":*^20}')
    print(f'\n{"=":=^40}\n')
elif media >= 4 and media <= 5.9:
    print(f'\nNota 1: {n1:.1f}\n\nNota 2: {n2:.1f}')
    print(f'\nMedia: {media:.1f}')
    print('\nConceito: D')
    print(f'\n{"_":_^40}\n')
    print(f'{"REPROVADO":*^20}')
    print(f'\n{"=":=^40}\n')
else:
    print(f'\nNota 1: {n1:.1f}\n\nNota 2: {n2:.1f}')
    print(f'\nMedia: {media:.1f}')
    print('\nConceito: E')
    print(f'\n{"_":_^40}\n')
    print(f'{"REPROVADO":*^20}')
    print(f'\n{"=":=^40}\n')
