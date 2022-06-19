'''4) Qual foi o gasto por ano?'''

import csv  
from functions import read_data, convert_to_dicionary

filename = 'compras.csv'

data = read_data(filename)

info = convert_to_dicionary(data)

purchases = {}

for l in info:
    year = l['ano']
    purchase = l['compra'] 
    if year not in purchases:
        purchases[year] = purchase
    else:
        purchases[year] += purchase 

print(f'\n\n{"TOTAL DE COMPRAS ANUAIS":=^40}\n')
for key in sorted(purchases.keys()):
    print(f'{key}:{"_"*19} R$ {purchases[key]:,.2f}')
print(f'\n{"="*40}\n')