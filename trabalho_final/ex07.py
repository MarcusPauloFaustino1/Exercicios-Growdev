'''7) Qual dos anos (1o, 2o ou 3o) mais procura a monitoria?. Crie um gráfico para
mostrar esses dados.'''

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

monitored = {'1º ano': 0, '2º ano': 0, '3º ano':0}

for line in info:
    
    year = line['ano']
    monitoring = line['monitoria']
    
    if year == 1 and monitoring in 'True':
        monitored['1º ano'] += 1
        
    elif year == 2 and monitoring in 'True':
        monitored['2º ano'] += 1
        
    elif year == 3 and monitoring in 'True':
        monitored['3º ano'] += 1


monitored_1 = monitored['1º ano']
monitored_2 = monitored['2º ano']
monitored_3 = monitored['3º ano']

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

print(f'\n\n{bcolors.BLUE}{" "*10}{corner1}{"─"*36}{corner3}{bcolors.RESET}')    
print(f'{bcolors.BLUE}{heightbox}{minibox*9}{bcolors.RESET}{bcolors.BOLD}{"  MAIOR PROCURA POR MONITORIA ─ ANOS  "}{bcolors.BLUE}{minibox*9}{heightbox}{bcolors.RESET}')
print(f'{bcolors.BLUE}{heightlefth}{" "*9}{corner2}{"─"*36}{corner4}{" "*9}{bigheight}{bcolors.RESET}')
print(f'{bcolors.BLUE}{heightlefth}{" "*56}{bigheight}{bcolors.RESET}')
print(f'{bcolors.BLUE}{heightlefth}{bcolors.PURPLE}   {box}{bcolors.RESET}   Ano com maior procura por monitoria{" "*14}{bcolors.BLUE}{bigheight}{bcolors.RESET}')
print(f'{bcolors.BLUE}{heightlefth}{" "*56}{bigheight}{bcolors.RESET}')
print(f'{bcolors.BLUE}{heightlefth}{bcolors.RESET}   {bcolors.GREY}{box}{bcolors.RESET}   Demais anos{" "*38}{bcolors.BLUE}{bigheight}{bcolors.RESET}')
print(f'{bcolors.BLUE}{heightlefth}{bcolors.GREY}{" "*56}{bcolors.BLUE}{bigheight}{bcolors.RESET}')

print(f'{bcolors.BLUE}{heightlefth}{bcolors.GREY}{bcolors.BOLD}{" 1º ano: "}{box*19}{"─"*12}>  Alunos: {monitored_1:,}  {bcolors.BLUE}{bigheight}{bcolors.RESET}')

print(f'{bcolors.BLUE}{heightlefth}{bcolors.GREY}{bcolors.BOLD}{bcolors.PURPLE}{" 2º ano: "}{box*22}{"─"*9}>  Alunos: {monitored_2:,}  {bcolors.BLUE}{bigheight}{bcolors.RESET}')

print(f'{bcolors.BLUE}{heightlefth}{bcolors.GREY}{" 3º ano: "}{box*21}{"─"*10}>  Alunos: {monitored_3:,}{" "*2}{bcolors.BLUE}{bigheight}{bcolors.RESET}')

print(f'{bcolors.BLUE}{heightlefth}{bcolors.GREY}{" "*56}{bcolors.BLUE}{bigheight}{bcolors.RESET}')
        
print(f'{bcolors.BLUE}{inferior_left}{minibox*56}{inferior_right}{bcolors.RESET}\n\n\n')
