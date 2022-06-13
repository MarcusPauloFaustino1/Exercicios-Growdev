'''Faça um Programa que leia dois vetores com 10 elementos cada. Gere um
terceiro vetor de 20 elementos, cujos valores deverão ser compostos pelos
elementos intercalados dos dois outros vetores.'''


lista1 = []
lista2 = []
lista3 = []

elemento = 1
elemento2 = 1

print(f'\n\nDigite um vetor com 10 elementos\n\n')

for i in range(10):
    vetor1 = input(f'elemento {elemento}: ')
    elemento += 1
    lista1.append(vetor1)

print(f'\n\nDigite outro vetor com 10 elementos\n\n')

for i in range(10):
    vetor2 = input(f'elemento {elemento2}: ')
    elemento2 += 1
    lista2.append(vetor2)

listax = lista1[0]
listay = lista2[0]

for i in range(10):
    lista3.append(lista1[i])
    lista3.append(lista2[i])
    

print(lista3)