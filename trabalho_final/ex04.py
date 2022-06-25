'''4) De todos os alunos que reprovaram quantos foram por falta e quantos foram
por nota, e quantos foram por ambas as causas?'''

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

for line in info:
    
    exam = line['nota_exame']
    faults = line['faltas']
    mean = (line['nota_semestre_2'] + line['nota_semestre_1'])/2
    
    if exam < 5 and mean < 7 and faults > 15:
        reproved['faults_grade'] += 1
    elif exam < 5 and mean < 7:
        reproved['grade'] += 1
    elif faults > 15:
        reproved['faults'] += 1
        
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

print(reproved)

grade = reproved['grade']
faults_grade = reproved['faults_grade']
faults = reproved['faults']

print(f'\n\n{bcolors.RED}{" "*10}{corner1}{"─"*36}{corner3}{bcolors.RESET}')    
print(f'{bcolors.GREY}{heightbox}{bcolors.RESET}{bcolors.RED}{minibox*9}{bcolors.RESET}{bcolors.BOLD}{" QUANTIDADES E MOTIVOS DE REPROVAÇÕES "}{bcolors.GREY}{minibox*8}{bcolors.RESET}{bcolors.RED}{heightbox}{bcolors.RESET}\n{bcolors.GREY}{heightlefth}{" "*9}{bcolors.GREY}{corner2}{"─"*36}{corner4}{bcolors.RESET}{bcolors.RED}{" "*8}{bigheight}{bcolors.RESET}')
print(f'{bcolors.GREY}{heightlefth}{bcolors.RESET} {" "*54}{bcolors.RED}{bigheight}{bcolors.RESET}')

print(f'{bcolors.GREY}{heightlefth}{bcolors.RESET}{bcolors.BOLD}{"nota e faltas: "}{bcolors.YELLOW}{box*18}{"─"*13}>   {bcolors.RESET}{faults_grade:,}  {bcolors.RED}{bigheight}{bcolors.RESET}')

print(f'{bcolors.GREY}{heightlefth}{bcolors.RESET}{bcolors.BOLD}{"nota:          "}{bcolors.CIAN}{box*20}{"─"*11}> {bcolors.RESET}{grade:,}  {bcolors.RED}{bigheight}{bcolors.RESET}')

print(f'{bcolors.GREY}{heightlefth}{bcolors.RESET}{bcolors.BOLD}{"faltas:        "}{bcolors.PURPLE}{box*28}{"─"*3}> {bcolors.RESET}{faults:,}{" "*2}{bcolors.RED}{bigheight}{bcolors.RESET}')

print(f'{bcolors.GREY}{heightlefth}{bcolors.RESET} {" "*54}{bcolors.RED}{bigheight}{bcolors.RESET}')
        
print(f'{bcolors.GREY}{inferior_left}{minibox*27}{bcolors.RESET}{bcolors.RED}{minibox*28}{inferior_right}{bcolors.RESET}\n\n\n')
