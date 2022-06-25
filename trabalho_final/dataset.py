'''Dataset: o dataset ‘alunos.csv’ contém o seguinte cabeçalho.
nome, ano, escola, nota_semestre_1, nota_semestre_2, faltas,
nota_exame, monitoria'''

import csv

def read_data(filename):
    file = open(filename, encoding='utf-8')
    data = csv.reader(file, delimiter=',')
    data = list(data)
    return(data)

def convert_to_dicionary(data):
    info = []
    register = len(data)
    for i in range(1, register):
        info.append(
            {
            'nome': data[i][0],
            'ano': int(data[i][1]),
            'escola': data[i][2],
            'nota_semestre_1': float(data[i][3]),
            'nota_semestre_2': float(data[i][4]),
            'faltas': int(data[i][5]),
            'nota_exame': float(data[i][6]),
            'monitoria': (data[i][7])
            }
        )
    return info