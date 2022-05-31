'''Escreva um algoritmo que leia três números fornecidos pelo usuário e mostre
se a soma de dois deles resulta no terceiro.'''

n1 = float(input("Digite o primeiro número:"))
n2 = float(input("Digite o segundo número:"))
n3 = float(input("Digite o terceiro número:"))

if n1 + n2 == n3 or n2 + n3 == n1 or n3 + n1 == n2:
    print("A soma de dois dos números RESULTA no terceiro número.")
else:
    print(" A soma de dois dos números NÃO resulta no terceiro número. ")