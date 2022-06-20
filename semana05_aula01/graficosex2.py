import matplotlib.pyplot as plt
import csv  
from functions import purchases_years, read_data, convert_to_dicionary

filename = 'compras.csv'

data = read_data(filename)

info = convert_to_dicionary(data)

purchases_number_years1 = {}

for l in info:
    year = l['ano']
    if year % 2 == 0 and year not in purchases_number_years1:
        purchases_number_years1[year] = 1
    elif year % 2 == 0 and year in purchases_number_years1:
        purchases_number_years1[year] += 1
        
purchases_number_years2 = {}

for l in info:
    year = l['ano']
    if year % 2 != 0 and year not in purchases_number_years2:
        purchases_number_years2[year] = 1
    elif year % 2 != 0 and year in purchases_number_years2:
        purchases_number_years2[year] += 1
        
        
plt.bar(purchases_number_years2.keys(), purchases_number_years2.values(), label = 'Anos ímpares', color = 'c', shadows = True)
plt.bar(purchases_number_years1.keys(), purchases_number_years1.values(), label = 'Anos pares', color = 'b', shadows = True)
plt.legend()
plt.show()
       
