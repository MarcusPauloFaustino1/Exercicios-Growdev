'''3) Quantos alunos do 3o ano reprovaram? e desses quantos procuraram
monitoria?'''

import csv
from dataset import read_data, convert_to_dicionary
import os

os.system('clear')

filename = 'alunos.csv'

#leitura de Arquivo

data = read_data(filename)

register = len(data)

#transformação dos registros para dicionario (convertendo valores)
    
info = convert_to_dicionary(data)

reproved = 0
monitored = 0
for line in info:
    year = line['ano']
    exam = line['nota_exame']
    mean = (line['nota_semestre_2'] + line['nota_semestre_1'])/2
    faults = line['faltas']
    monitoring = line['monitoria']
    if year == 3 :
        if faults > 15:
            reproved += 1
            if monitoring in 'True':
                monitored += 1
        elif mean < 7 and exam <= 5:
            reproved += 1
            if monitoring in 'True':
                monitored += 1
            


class bcolors:
    WHITE = '\033[99m'
    GREEN = '\033[92m'
    BLUE = '\033[94m'
    PURPLE = '\033[95m'
    CIAN = '\033[96m'
    RED = '\033[91m'
    GREY = '\033[90m'
    YELLOW = '\033[93m'
    BOLD = '\033[1m'
    RESET = '\033[0m'

box = u'\u2586'
minibox = u'\u2584'
heightbox = u'\u25A0'
bigheight = u'\u2590'
heightlefth = u'\u258C'
inferior_left = u'\u2599'
inferior_right = u'\u259F'
corner1 = u'\u250C'
corner2 = u'\u2514'
corner3 = u'\u2510'
corner4 = u'\u2518'

print(f'\n\n{bcolors.BLUE}{" "*10}{corner1}{"─"*34}{corner3}{bcolors.RESET}')    
print(f'{bcolors.GREY}{heightbox}{bcolors.RESET}{bcolors.BLUE}{minibox*9}{bcolors.RESET}{bcolors.BOLD}{"     ALUNOS REPROVADOS NO 3º ANO    "}{bcolors.GREY}{minibox*9}{bcolors.RESET}{bcolors.BLUE}{heightbox}{bcolors.RESET}\n{bcolors.GREY}{heightlefth}{" "*9}{bcolors.GREY}{corner2}{"─"*34}{corner4}{bcolors.RESET}{bcolors.BLUE}{" "*9}{bigheight}{bcolors.RESET}')

print(f'{bcolors.GREY}{heightlefth}{bcolors.RESET} {" "*53}{bcolors.BLUE}{bigheight}{bcolors.RESET}')
print(f'{bcolors.GREY}{heightlefth}{bcolors.RESET}{bcolors.BOLD}{"Total de alunos reprovados:"}{bcolors.RED} {box*20}{bcolors.RESET} {reproved}{bcolors.BLUE} {bigheight}{bcolors.RESET}\n{bcolors.GREY}{heightlefth}{bcolors.RESET}{bcolors.BOLD}{"Destes procuraram mentoria:"}{bcolors.RESET}{bcolors.YELLOW} {box*10}{bcolors.RESET} {monitored}{bcolors.BLUE}{" "*12}{bigheight}{bcolors.RESET}\n{bcolors.GREY}{heightlefth}{bcolors.RESET}{" "*54}{bcolors.BLUE}{bigheight}{bcolors.RESET}\n{bcolors.GREY}{heightlefth}{bcolors.RESET}{" "*54}{bcolors.BLUE}{bigheight}{bcolors.RESET}')
print(f'{bcolors.GREY}{inferior_left}{minibox*27}{bcolors.RESET}{bcolors.BLUE}{minibox*27}{inferior_right}{bcolors.RESET}\n\n\n')