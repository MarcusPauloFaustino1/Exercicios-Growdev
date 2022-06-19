'''Utilize as seguintes faixas etárias nos exercícios em que for necessário.
● Jovens, 18 a 25 anos
● Adultos, 26 a 59 anos
● Idosos, igual ou maior que 60 anos


Qual é a faixa etária que mais gasta?'''

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
        


ages_purchases = {}
for l in info:
    purchase = l['compra'] 
    if l['idade'] >= 18 and l['idade']<= 25:
       l['idade'] = 'JOVENS'
       if 'JOVENS' not in ages_purchases:
            ages_purchases['JOVENS'] = purchase
       elif 'JOVENS' in ages_purchases:
            ages_purchases['JOVENS'] += purchase
    elif l['idade'] >= 26 and l['idade']<= 59:
        l['idade'] = 'ADULTOS'
        if 'ADULTOS' not in ages_purchases:
            ages_purchases['ADULTOS'] = purchase
        elif 'ADULTOS' in ages_purchases:
            ages_purchases['ADULTOS'] += purchase
    elif l['idade'] >= 60:
        l['idade'] = 'IDOSOS'
        if 'IDOSOS' not in ages_purchases:
            ages_purchases['IDOSOS'] = purchase
        elif 'IDOSOS' in ages_purchases:
            ages_purchases['IDOSOS'] += purchase
            
mean_olds = ages_purchases['IDOSOS'] / idosos 
mean_adults = ages_purchases['ADULTOS'] / adultos
mean_youngs = ages_purchases['JOVENS'] / jovens
        
 

    
biggest_purchase = 0
for age in ages_purchases:
    if ages_purchases[age] > biggest_purchase:
        biggest_purchase = ages_purchases[age]
        current_age = age
    

print(f'\n\n{" FAIXA ETÁRIA QUE MAIS GASTA ":=^40}\n\n{"."*40}\n') 
print('Em valores totais...\n')
print(f'{current_age} tiveram o maior gasto\n\nGasto total: R$ {biggest_purchase:,.2f}')
print(f'\n{"."*40}\n')
print('Em valores proporcionais...\n')
if mean_youngs > mean_adults and mean_youngs > mean_olds:
    print(f'JOVENS gastaram mais  \n\nGasto médio: R$ {mean_youngs:,.2f}\n\n{"."*40}\n')
elif mean_adults > mean_youngs and mean_adults > mean_olds:
    print(f'ADULTOS gastaram mais  \n\nGasto médio: R$ {mean_adults:,.2f}\n\n{"."*40}\n')
elif mean_olds > mean_youngs and mean_olds > mean_adults :
    print(f'IDOSOS gastaram mais  \n\nGasto médio: R$ {mean_olds:,.2f}\n\n{"."*40}\n')
    
print(f'\n{"="*40}\n')