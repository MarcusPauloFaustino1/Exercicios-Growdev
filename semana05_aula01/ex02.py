'''2) Busque qual são os anos da base de dados?'''

import csv
from functions import read_data, convert_to_dicionary

filename = 'compras.csv'

data = read_data(filename)

info = convert_to_dicionary(data)

year = []

def all_years():
    for line in info:
        year.append(line['ano'])
    list_years = sorted(set(year))
    return(list_years)

all_years = all_years()




print(f'\n{"ANOS DA BASE DE DADOS":=^40}\n\nAnos:\n ')
print(all_years[:6])
print(all_years[6:12])
print(all_years[12:])

print(f'\n\n{"="*40}\n')
