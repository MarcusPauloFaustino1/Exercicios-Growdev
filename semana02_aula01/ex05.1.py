'''Escreva um algoritmo que leia três números fornecidos pelo usuário e mostre
se a soma de dois deles resulta no terceiro.'''

n1 = float(input("Digite o primeiro número:"))
n2 = float(input("Digite o segundo número:"))
n3 = float(input("Digite o terceiro número:"))

_1 = n1 + n2 == n3
_2 = n2 + n3 == n1
_3 = n3 + n1 == n2

if _1:
    print("A soma do primeiro número com o segundo RESULTA  no terceiro número.")
elif _2:
    print("A soma do segundo número com o terceiro RESULTA  no segundo número.")
elif _3:
    print("A soma do terceiro número com o primeiro RESULTA  no segundo número.")
else:
    print("A soma de dois dos números NÃO RESULTA  no terceiro número.")