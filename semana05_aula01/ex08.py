'''A opção de débito é mais utilizada entre homens ou mulheres?'''

import csv
from time import sleep  
from functions import read_data, convert_to_dicionary

filename = 'compras.csv'

data = read_data(filename)

info = convert_to_dicionary(data)

m = 0
f = 0
for line in info:
    if line['sexo'] in 'M' and line['pagamento'] in 'debito':
        m += 1
    elif line['sexo'] in 'F' and line['pagamento'] in 'debito':
        f += 1

print(f'\n\n{" Quem Compra Mais no Débito? ":=^40}\n') 
print('Homens ou Mulheres?')
print(f'\n{"."*40}\n')
print('RESULTADO:\n\n')
sleep(2)
if m > f:
    print('*** HOMENS *** compram mais no débito.')
elif f > m:
    print('*** MULHERES *** compram mais no débito.')
print(f'\n{"="*40}\n')
