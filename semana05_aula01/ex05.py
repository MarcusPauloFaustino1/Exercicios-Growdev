'''5) Qual foi o ano com maior gasto?'''

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
        
biggest_purchase = []        
for i in sorted(purchases, key = purchases.get):
    biggest_purchase.append(purchases[i])
    
biggest_purchase = max(biggest_purchase)

for key in purchases:
    if purchases[key] == biggest_purchase:
        year_biggest_purchase = key
        
#outra opção (sem usar lista)

#biggest_purchase = 0
#for year in purchases:
#    if purchases[year] > biggest_purchase:
#        biggest_purchase = purchases[year]
#        biggest_year = year



print(f'\n\n{" ANO COM MAIOR GASTO ":=^30}\n\n{"."*30}\n')
print(f'Ano: {year_biggest_purchase}\n\nGasto: R$ {biggest_purchase:,.2f}\n{"."*30}\n\n')
print(f'{"="*30}\n')
        


