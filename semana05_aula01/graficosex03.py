'''3) Mostre a quantidade de homens e mulheres na base de dados.'''

import matplotlib.pyplot as plt
import csv  
from functions import purchases_years, read_data, convert_to_dicionary

filename = 'compras.csv'

data = read_data(filename)

info = convert_to_dicionary(data)

m_gender = 0
f_gender = 0
genders = ['Homens','Mulheres']
c = ['c','m']
for l in info:
    gender = l['sexo']
    if gender in 'M':
        m_gender += 1
    elif gender in 'F':
        f_gender += 1

n_genders = [m_gender,f_gender]

plt.pie(n_genders, labels = genders, colors = c, startangle = 90, shadow = True, explode = (0.1, 0) )

plt.legend()
plt.show()
       