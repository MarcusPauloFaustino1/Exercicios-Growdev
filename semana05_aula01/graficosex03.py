'''3) Mostre a quantidade de homens e mulheres na base de dados.'''

import numpy as np
import matplotlib.pyplot as plt
import csv  
from functions import purchases_years, read_data, convert_to_dicionary

filename = 'compras.csv'

data = read_data(filename)

info = convert_to_dicionary(data)

m_gender = 0
f_gender = 0
genders = ["Homens","Mulheres"]
c = ['c','m']
for l in info:
    gender = l['sexo']
    if gender in 'M':
        m_gender += 1
    elif gender in 'F':
        f_gender += 1

n_genders = [m_gender,f_gender]

def func(pct, allvals):
    absolute = int(pct/100.*np.sum(allvals))
    return "{:.1f}%\n({:d})".format(pct, absolute)

fig, ax = plt.subplots(figsize=(6, 6), subplot_kw=dict(aspect="equal"))

wedges, texts, autotexts = ax.pie(n_genders, autopct=lambda pct: func(pct, n_genders), textprops=dict(color='w'))

ax.legend(wedges, genders, title = "Legenda", loc = "upper left", bbox_to_anchor = (1,0.5))

plt.setp(autotexts, size=8, weight="bold")

ax.set_title('Quantidade de Homens e Mulheres.')

plt.show()
       