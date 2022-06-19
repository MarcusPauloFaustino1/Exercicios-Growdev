'''1) Procure quem foi a pessoa que mais gastou?'''

import csv
from functions import read_data, convert_to_dicionary 

filename = 'compras.csv'

#leitura de Arquivo

data = read_data(filename)

register = len(data)

#transformação dos registros para dicionario (convertendo valores)
    
info = convert_to_dicionary(data)
    
#processamento

biggest_purchase = -1

index_biggest_purchase = 0

header = data[0]

for index, line in enumerate(info):
    if line['compra'] > biggest_purchase:
        biggest_purchase = line['compra']
        index_biggest_purchase  = index
        
person = info[index_biggest_purchase]
        
#saída de dados        
        
print(f'\n{" MAIOR COMPRA ":=^30}\n\n{"."*30}\n\nNome: {person["nome"]} {person["sobrenome"]}\n\nValor da Compra: R$ {person["compra"]:,.2f}\n\n{"."*30}\n\n{"="*30}\n')



    

    