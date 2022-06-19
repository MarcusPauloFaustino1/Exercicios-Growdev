'''Utilize as seguintes faixas etárias nos exercícios em que for necessário.
● Jovens, 18 a 25 anos
● Adultos, 26 a 59 anos
● Idosos, igual ou maior que 60 anos


Utilizando as faixas etárias, diga quantas pessoas há em cada faixa?'''

import csv  
from functions import read_data, convert_to_dicionary

filename = 'compras.csv'

data = read_data(filename)

info = convert_to_dicionary(data)

jovens = 0
adultos = 0
idosos = 0

for line in info:
    if line['idade'] >= 18 and line['idade'] <= 25:
        jovens += 1
    elif line['idade'] >= 26 and line['idade'] <= 59:
        adultos += 1
    elif line['idade'] >= 60:
        idosos += 1

print(f'\n\n{" PESSOAS POR FAIXAS ETÁRIAS ":=^40}\n\n{"."*40}\n')        
print(f'Nº de jovens:{"_"*20}   {jovens:,.0f}\nNº de adultos:{"_"*19} {adultos:,.0f}\nNº de idosos:{"_"*20}   {idosos:,.0f}\n\n{"."*40}\n\n')
print(f'{"="*40}\n')