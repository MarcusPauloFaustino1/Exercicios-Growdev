'''5) Qual a média de todas as notas (do 1o e 2o semestre) dos alunos do 2o ano?'''

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

reproved = {'faults_grade': 0, 'faults': 0,'grade': 0 }

grades = []
for line in info:
    year = line['ano']
    grade_1 = line['nota_semestre_1']
    grade_2 = line['nota_semestre_2']
    
    if year == 2:
        grades.append(grade_1)
        grades.append(grade_2)
    
mean = sum(grades) / len(grades) 

print(f'{mean:.2f}')

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


print(f'\n\n{bcolors.YELLOW}{corner1}{"─"*23}{corner3}{bcolors.RESET}')   
print(f'{bcolors.BOLD}{bcolors.CIAN}  MÉDIA GERAL DO 2º ANO{bcolors.RESET}') 
print(f'{bcolors.YELLOW}{heightbox}{minibox*23}{heightbox}{bcolors.RESET}')
print(f'{bcolors.YELLOW}{heightlefth}{" "*23}{bigheight}{bcolors.RESET}')
print(f'{bcolors.YELLOW}{heightlefth}{" "*23}{bigheight}{bcolors.RESET}')
print(f'{bcolors.YELLOW}{heightlefth}   Média:{bcolors.BOLD}{bcolors.CIAN}{mean:^ 14.2f}{bcolors.YELLOW}{bigheight}{bcolors.RESET}')
print(f'{bcolors.YELLOW}{heightlefth}{" "*23}{bigheight}{bcolors.RESET}')
print(f'{bcolors.YELLOW}{heightlefth}{" "*23}{bigheight}{bcolors.RESET}')
print(f'{bcolors.YELLOW}{inferior_left}{minibox*23}{inferior_right}{bcolors.RESET}\n\n\n')
    