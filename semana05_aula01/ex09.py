'''Qual o sobrenome que mais aparece na base de dados?'''

import csv  
from functions import read_data, convert_to_dicionary

filename = 'compras.csv'

data = read_data(filename)

info = convert_to_dicionary(data)

last_names = []
for line in info:
    last_name = line['sobrenome']
    last_names.append(last_name)
    
def most_frequent(last_names):
    return max(set(last_names), key = last_names.count)

mostfrequent = most_frequent(last_names)

frequency = 0
for line in info:
    if line['sobrenome'] == mostfrequent:
        frequency += 1
        
        
print(f'\n{" SOBRENOME MAIS RECORRENTE ":=^36}\n')
print('Sobrenome: ', end="")
print(most_frequent(last_names))
print(f'\nRecorrência: {frequency} vezes\n')
print(f'{"="*36}\n')

