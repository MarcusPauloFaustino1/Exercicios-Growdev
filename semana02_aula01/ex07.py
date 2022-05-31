'''Escreva um algoritmo que receba 3 números, faça a soma dos dois primeiros
e verifique se o resultado da soma é maior que o terceiro número lido.'''

n1 = float(input("Digite o primeiro número:"))
n2 = float(input("Digite o segundo número:"))
n3 = float(input("Digite o terceiro número:"))



if n1 + n2 > n3:
    print("A soma dos dois primeiros números É MAIOR que o terceiro número.")
else:
    print("A soma dos dois primeiros números NÃO é maior que o terceiro número.")
    