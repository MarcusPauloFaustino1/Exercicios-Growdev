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

box = u'\u2586'
class bcolors:
    WHITE = '\033[99m'
    GREEN = '\033[92m'
    BLUE = '\033[94m'
    PURPLE = '\033[95m'
    RESET = '\033[0m'
    
print(f'\n\n{bcolors.WHITE}{" TOTAL DE COMPRAS ANUAIS ":=^63}{bcolors.RESET}\n')
for key in sorted(purchases.keys()):
    print(f'{bcolors.GREEN}{key}:{bcolors.RESET} {bcolors.BLUE}{box*(int((purchases[key]*2)/72220/1.3))}{bcolors.RESET}{" "*(40 - int((purchases[key]*2)/72220/1.3))} {bcolors.PURPLE}R$ {purchases[key]:,.2f}{bcolors.RESET}')
print(f'\n{bcolors.WHITE}{"="*63}{bcolors.RESET}\n')
