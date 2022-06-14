'''Escreva um programa para solicitar ao usuário o raio r de uma esfera, e
calcular o volume V da esfera usando uma função, e exibir o resultado. Utilize
a seguinte fórmula para determinar o volume:

v = (4.0 / 3.0) * π * r3'''
import math

r = float(input('Digite o valor do raio r de uma esfera: '))
def volRaio(r):
    v = (4 / 3) * math.pi * r**3
    return v

print(volRaio(r))