'''10)Qual foi o ano em que os homens mais usaram o crédito?'''

import csv
from statistics import median_grouped  
from functions import read_data, convert_to_dicionary

filename = 'compras.csv'

data = read_data(filename)

info = convert_to_dicionary(data)

years = []
for line in info:   
    if line['sexo'] in 'M' and line['pagamento'] in 'credito':
        year = line['ano']
        years.append(year)
        
def main_year(years):
    return max(set(years), key = years.count)

men_2007_credit = 0
for line in info:
    if line['sexo'] in 'M' and line['pagamento'] in 'credito' and line['ano'] == main_year(years):
        men_2007_credit += 1

print(f'\n{" ANO EM QUE HOMENS MAIS USARAM CRÉDITO ":=^50}\n')
print(f'Ano:  ', end="")
print(main_year(years))
print('\nPagaram com crédito:  ', end="")
print(f'{men_2007_credit} vezes')
print(f'\n{"="*50}\n')