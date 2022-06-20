import matplotlib.pyplot as plt
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

purchases1 = {}

for l in info:
    year = l['ano']
    purchase = l['compra'] 
    if year % 2 == 0 and year not in purchases1:
        purchases1[year] = purchase
    elif year % 2 == 0 and year in purchases1:
        purchases1[year] += purchase 
        
purchases2 = {}

for l in info:
    year = l['ano']
    purchase = l['compra'] 
    if year % 2 != 0 and year not in purchases2:
        purchases2[year] = purchase
    elif year % 2 != 0 and year in purchases2:
        purchases2[year] += purchase         
        
      
        
plt.bar(purchases2.keys(), purchases2.values(), label = 'Anos ímpares', color = 'c')
plt.bar(purchases1.keys(), purchases1.values(), label = 'Anos pares', color = 'b')
plt.legend()
plt.show()


