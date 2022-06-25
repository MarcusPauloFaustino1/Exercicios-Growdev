import csv
from dataset import read_data, convert_to_dicionary

filename = 'alunos.csv'

#leitura de Arquivo

data = read_data(filename)

register = len(data)

#transformação dos registros para dicionario (convertendo valores)
    
info = convert_to_dicionary(data)

