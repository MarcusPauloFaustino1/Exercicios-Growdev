'''Escreva um algoritmo que leia 3 valores e exiba qual o maior valor entre eles.'''

from time import sleep


print(f"\n{'MAIOR VALOR':=^70}\n")

n1 = float(input("Digite um valor:"))
n2 = float(input("Digite outro valor:"))
n3 = float(input("Digite mais um valor:"))

print('Resultado:')
sleep(2)

print(f"\n{'_':_^70}\n")

if n1 > n2 and n1 > n3:
    print(f"\n\n{n1} é o maior valor.\n\n")
    print(f"\n{'=':=^70}\n")
if n2 > n1 and n2 > n3:
    print(f"\n\n{n2} é o maior valor.\n\n")
    print(f"\n{'=':=^70}\n")
if n3 > n1 and n3 > n2:
    print(f"\n\n{n3} é o maior valor.\n\n")
    print(f"\n{'=':=^70}\n")
if n1 == n2 and n1 == n3:
    print("\n\nOs três valores são iguais.\n\n")
    print(f"\n{'=':=^70}\n")
if n1 == n2 and n1 > n3:
    print(f"\n\n{n1} foi digitado duas vezes, sendo ele o maior valor.\n\n")
    print(f"\n{'=':=^70}\n")
if n1 == n3 and n1 > n2:
    print(f"\n\n{n1} foi digitado duas vezes, sendo ele o maior valor.\n\n")
    print(f"\n{'=':=^70}\n")
if n2 == n3 and n2 > n1:
    print(f"\n\n{n2} foi digitado duas vezes, sendo ele o maior valor.\n\n")
    print(f"\n{'=':=^70}\n")
    