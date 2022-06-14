'''Construa uma função que receba uma data no formato DD/MM/AAAA e
devolva uma string em um formato por extenso. Opcionalmente, valide a data
e retorne NULL caso a data seja inválida.'''

'''d = int(input('Informe um dia do mês: '))
m = int(input('Informe um mês: '))
a = int(input('Informe um ano: '))

data = f'{d} / {m} / {a}'

print(data)'''

import datetime
import os
from dateutil import parser
os.system('clear')



date = input('Informe uma data (DD/MM/AAAA): ')

format = "%d/%m/%Y"
res = True

d = int(date[0:2])
m = int(date[3:5])
y = int(date[6:10])

try:
    res = bool(parser.parser(date))
    res = True
except ValueError:
    res = False
if res == False:
    print('NULL')
    exit()
else:
    pass

def date_in_full(m):
    
    if m == 1:
        m = 'janeiro'
    elif m == 2:
        m = 'fevereiro'
    elif m == 3:
        m = 'março'
    elif m == 4:
        m = 'abril'
    elif m == 5:
        m = 'maio'
    elif m == 6:
        m = 'junho'
    elif m == 7:
        m = 'julho'
    elif m == 8:
        m = 'agosto'
    elif m == 9:
        m = 'setembro'
    elif m == 10:
        m = 'outubro'
    elif m == 11:
        m = 'novembro'
    elif m == 12:
        m = 'dezembro'
  
    return f'dia {d} de {m} de {y}'

result = date_in_full(m)
    
print(result)

