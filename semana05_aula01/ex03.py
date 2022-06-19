'''3) Qual a porcentagem de homens e mulheres na base de dados?'''

import csv
from functions import read_data, convert_to_dicionary

filename = 'compras.csv'

data = read_data(filename)

info = convert_to_dicionary(data)

m = 0
f = 0

for line in info:
    if line['sexo'] in 'M':
        m += 1
    elif line['sexo'] in 'F':
        f += 1
    
total = m + f

m_percent = (100*m)/total
f_percent = (100*f)/total

print(f'\n{" compras.csv ":=^40}\n\n{"."*40}\n\nPorcentagem de mulheres: {f_percent} %\n\nPorcentagem de homens: {m_percent} %\n\n{"."*40}\n\n{"="*40}\n\n')