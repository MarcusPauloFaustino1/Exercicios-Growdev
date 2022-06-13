'''Faça um Programa que leia um vetor de 10 números reais e mostre-os na
ordem inversa.'''


vetor = []


for i in range (10):
    n = float(input('Digite um número real: '))
    vetor.append(n)

vetor.reverse()

print(vetor)