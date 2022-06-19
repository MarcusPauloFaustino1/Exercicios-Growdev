'''12)Qual o valor gasto em compras por jovens do ano de 2010 até 2015?'''

import csv  
from functions import read_data, convert_to_dicionary

filename = 'compras.csv'

data = read_data(filename)

info = convert_to_dicionary(data)

total_purchase = 0
for l in info:
    year = l['ano']
    age = l['idade']
    purchase = l['compra'] 
    
    if age >= 18 and age <= 25 and year >= 2010 and year <= 2015:
        total_purchase += purchase

print(f'\n{" VALOR GASTO POR JOVENS DE 2010 ATÉ 2015 ":=^50}\n')     
print(f'Total: R$ {total_purchase:,.2f}')
print(f'\n{"="*50}\n')