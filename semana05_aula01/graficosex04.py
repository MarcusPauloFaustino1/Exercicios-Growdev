'''4) Exiba o valor total de compras por modo de pagamento.'''

import matplotlib.pyplot as plt
import csv  
from functions import purchases_years, read_data, convert_to_dicionary

filename = 'compras.csv'

data = read_data(filename)

info = convert_to_dicionary(data)

payments = ['Débito','Crédito','Dinheiro']
c = ['c','y','g']
debito = 0
credito = 0
dinheiro = 0

for l in info:
    payment = l['pagamento']
    if payment in 'debito':
        debito += 1
    elif payment in 'credito':
        credito += 1
    elif payment in 'dinheiro':
        dinheiro += 1
        
n_payments = [debito,credito,dinheiro]


plt.bar(payments,n_payments, color = c )

plt.legend()
plt.show()