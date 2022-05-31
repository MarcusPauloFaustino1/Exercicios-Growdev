'''Escreva um algoritmo que receba dois números, exiba as opções:
a) 1 - adição
b) 2 - subtração
Então peça ao usuário para escolher uma das opções. Caso escolha a opção
1 o algoritmo deve realizar a soma dos dois números lidos e exibir. Caso
escolha a opção 2 o algoritmo deve realizar a subtração dos dois números
lidos e exibir.'''
from time import sleep


print(f"\n{'ADIÇÃO OU SUBTRAÇÃO':=^40}\n")
n1 = float(input("Digite um número:"))
n2 = float(input("Digite outro número:"))

print(f'\n{"_":_^40}\n')

opcao = int(input('\nEscolha uma opção:\n\na) Para escolher ADIÇÃO digite "1" \n\nb) Para escolher SUBTRAÇÃO digite "2"\n\nDigite a opção escolhida:'))

print(f'\n{"_":_^40}\n')

print('Resultado:')
sleep(2)

if opcao < 1 and opcao > 2:
    print("Opção inválida")
    opcao = int(input('\nEscolha uma opção:\n\na) Digite "1" para escolher adição\n\nb) Digite "2" para escolher subtração\n\nDigite a opção escolhida:'))

if opcao == 1:
    print(f"\n {n1} + {n2} = {n1 + n2}")
    print(f'\n{"=":=^40}\n')
elif opcao == 2:
    print(f"\n {n1} - {n2} = {n1 - n2}")
    print(f'\n{"=":=^40}\n')
