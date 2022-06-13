'''Construa um programa que permita a um usuário informar uma série de
números, até que um número negativo seja fornecido. Ao final, imprima o
somatório desses números, a média, o valor máximo e o mínimo.
Desconsidere o último número (negativo) informado pelo usuário.'''

lista = []
x=1
while x > 0:
    x = float(input('Digite um número positivo ou negativo: '))
    if x > 0:
        lista.append(x)



somatorio = sum(lista)
media = somatorio / len(lista)
maximo = max(lista)
minimo = min(lista)

print(f'\n\nConsiderando somente os valores positivos:\n\nSomatório: {somatorio}\n\nMédia: {media}\n\nValor Máximo: {maximo}\n\nValor Mínimo: {minimo}\n\n')


