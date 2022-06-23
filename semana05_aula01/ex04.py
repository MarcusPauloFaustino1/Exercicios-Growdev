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
    CIAN = '\033[96m'
    RED = '\033[91m'
    YELLOW = '\033[90m'
    RESET = '\033[0m'
    
biggest_purchase = 0
for year in purchases:
    if purchases[year] > biggest_purchase:
        biggest_purchase = purchases[year]
        
        
smallest_purchase = 2000000
for year in purchases:
    if purchases[year] < smallest_purchase:
        smallest_purchase = purchases[year]
        
    
print(f'\n\n{bcolors.WHITE}{" TOTAL DE COMPRAS ANUAIS ":=^63}{bcolors.RESET}\n')
for key in sorted(purchases.keys()):
    
    if purchases[key] == biggest_purchase:
        print(f'{bcolors.GREEN}{key}:{bcolors.RESET} {bcolors.GREEN}{box*(int((purchases[key]*2)/72220/1.3))}{bcolors.RESET}{" "*(40 - int((purchases[key]*2)/72220/1.3))} {bcolors.GREEN}R$ {purchases[key]:,.2f}{bcolors.RESET}')
    
    elif purchases[key] == smallest_purchase:
        print(f'{bcolors.RED}{key}:{bcolors.RESET} {bcolors.RED}{box*(int((purchases[key]*2)/72220/1.3))}{bcolors.RESET}{" "*(40 - int((purchases[key]*2)/72220/1.3))} {bcolors.RED}R$ {purchases[key]:,.2f}{bcolors.RESET}')
        
    elif key % 2 == 0:
        print(f'{bcolors.YELLOW}{key}:{bcolors.RESET} {bcolors.YELLOW}{box*(int((purchases[key]*2)/72220/1.3))}{bcolors.RESET}{" "*(40 - int((purchases[key]*2)/72220/1.3))} {bcolors.YELLOW}R$ {purchases[key]:,.2f}{bcolors.RESET}')
    
    elif key % 2 != 0:
        print(f'{bcolors.WHITE}{key}:{bcolors.RESET} {bcolors.YELLOW}{box*(int((purchases[key]*2)/72220/1.3))}{bcolors.RESET}{" "*(40 - int((purchases[key]*2)/72220/1.3))} {bcolors.YELLOW}R$ {purchases[key]:,.2f}{bcolors.RESET}')
    
print(f'\n{bcolors.WHITE}{"="*63}{bcolors.RESET}\n')
