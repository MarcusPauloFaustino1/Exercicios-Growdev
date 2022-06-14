'''Construa uma função que desenhe um retângulo usando os caracteres ‘+’ ,
‘−’ e ‘| ‘. Esta função deve receber dois parâmetros, linhas e colunas, sendo
que o valor por omissão é o valor mínimo igual a 1 e o valor máximo é 20. Se
valores fora da faixa forem informados, eles devem ser modificados para
valores dentro da faixa.'''

from random import randint


linhas = int(input('Informe um valor de (1 a 20) para o tamanho das linhas: '))
colunas = int(input('Informe um valor de (1 a 20) para o tamanho das colunas: '))

if linhas < 1 or linhas > 20:
    linhas = randint(1, 21)
if colunas < 1 or colunas > 20:
    colunas = randint(1, 21)

def retangulo(linhas, colunas):
    l = f"+{'─' * linhas}+"
    print(l)
    for i in range((colunas-2)):
        c = f"|{'+' * (linhas)}|"
        print(c)
    print(l)
    
print(retangulo(linhas, colunas))