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
            'sobrenome': data[i][1],
            'idade': int(data[i][2]),
            'sexo': data[i][3],
            'compra': float(data[i][4]),
            'ano': int(data[i][5]),
            'pagamento': data[i][6]
            }
        )
    return info

def all_years(info):
    year = []
    for line in info:
        year.append(line['ano'])
    list_years = sorted(set(year))
    return(list_years)

def purchases_years(info):
    purchases = {}

    for l in info:
        year = l['ano']
        purchase = l['compra'] 
        if year not in purchases:
            purchases[year] = purchase
        else:
            purchases[year] += purchase 