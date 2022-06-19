'''Qual opção de pagamento é mais utilizada em cada faixa etária?'''

import csv  
from functions import read_data, convert_to_dicionary

filename = 'compras.csv'

data = read_data(filename)

info = convert_to_dicionary(data)

y_payment = []
a_payment = []
o_payment = []

for l in info:
    payment = l['pagamento']
    age = l['idade'] 
    
    if age >= 18 and age <= 25 and payment in 'debito':
       y_payment.append('DÉBITO')
    elif age >= 18 and age <= 25 and payment in 'credito':
       y_payment.append('CRÉDITO')
    elif age >= 18 and age <= 25 and payment in 'dinheiro':
       y_payment.append('DINHEIRO')
       
       
    elif l['idade'] >= 26 and l['idade']<= 59 and payment in 'debito':
       a_payment.append('DÉBITO')
    elif l['idade'] >= 26 and l['idade']<= 59 and payment in 'credito':
       a_payment.append('CRÉDITO')
    elif l['idade'] >= 26 and l['idade']<= 59 and payment in 'dinheiro':
       a_payment.append('DINHEIRO')
       
    elif l['idade'] >= 60 and payment in 'debito':
       o_payment.append('DÉBITO')
    elif l['idade'] >= 60 and payment in 'credito':
       o_payment.append('CRÉDITO')
    elif l['idade'] >= 60 and payment in 'dinheiro':
       o_payment.append('DINHEIRO')
       
       
def main_young(y_payment):
    return max(set(y_payment), key = y_payment.count)
def main_adult(a_payment):
    return max(set(a_payment), key = a_payment.count)
def main_old(o_payment):
    return max(set(o_payment), key = o_payment.count)

print(f'\n\n{" PRINCIPAL OPÇÃO DE PAGAMENTO ":=^40}\n')
print('Jovens:   ', end="")
print(main_young(y_payment))
print('\nAdultos:  ', end="")
print(main_adult(a_payment))
print('\nIdosos:   ', end="")
print(main_old(o_payment))
print(f'\n{"="*40}\n')

       
