'''7) Escreva um programa que leia 10 valores e encontre o maior e o menor
deles. Mostre o resultado.'''

print(f'\n{" MAIOR E MENOR DENTRE 10 VALORES ":=^60}\n')

lista = []
for i in range(10):
    x = int(input('Digite um valor:'))
    lista.append(x)

maior = max(lista)
menor = min(lista)

print(f'\n{"─"*60}\n')

print(f'O maior valor é {maior} e o menor é {menor}   .')

print(f'\n{"="*60}\n')