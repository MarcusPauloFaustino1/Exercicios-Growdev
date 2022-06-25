'''6) As reprovações são maiores entre os alunos do 1o, 2o ou 3o ano?. Crie um
gráfico para mostrar isso.'''

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

for line in info:
    reproved = {'faults_grade': 0, 'faults': 0,'grade': 0 }

reproved = {'1º ano': 0, '2º ano': 0, '3º ano':0}
for line in info:
    year = line['ano']
    mean = (line['nota_semestre_2'] + line['nota_semestre_1'])/2
    exam = line['nota_exame']
    faults = line['faltas']
    
    if year == 1:
        if exam < 5 and mean < 7 or faults > 15:
            reproved['1º ano'] += 1
    elif year == 2:
        if exam < 5 and mean < 7 or faults > 15:
            reproved['2º ano'] += 1
    elif year == 3:
        if exam < 5 and mean < 7 or faults > 15:
            reproved['3º ano'] += 1

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
        
ano_1 = reproved['1º ano']
ano_2 = reproved['2º ano']
ano_3 = reproved['3º ano']

mais_reprovacoes = 0
for key in reproved:
    if reproved[key] > mais_reprovacoes:
        mais_reprovacoes = reproved[key]
        

print(f'\n\n{bcolors.PURPLE}{" "*10}{corner1}{"─"*37}{corner3}{bcolors.RESET}')    
print(f'{bcolors.PURPLE}{heightbox}{minibox*9}{bcolors.RESET}',end="")
print(f'{bcolors.BOLD}{" MAIORES REPROVAÇÕES ─ 1º, 2º E 3º ANO "}{bcolors.PURPLE}{minibox*9}',end="")
print(f'{heightbox}{bcolors.RESET}')
print(f'{bcolors.PURPLE}{heightlefth}{" "*9}{corner2}{"─"*37}{corner4}{bcolors.RESET}',end="")
print(f'{bcolors.PURPLE}{" "*9}{bigheight}{bcolors.RESET}')
print(f'{bcolors.PURPLE}{heightlefth}{" "*57}{bigheight}{bcolors.RESET}')
print(f'{bcolors.PURPLE}{heightlefth}{bcolors.RED}   {box}{bcolors.RESET}   Ano com maiores reprovações{" "*23}{bcolors.PURPLE}{bigheight}{bcolors.RESET}')
print(f'{bcolors.PURPLE}{heightlefth}{" "*57}{bigheight}{bcolors.RESET}')
print(f'{bcolors.PURPLE}{heightlefth}{bcolors.RESET}   {bcolors.GREY}{box}{bcolors.RESET}   Demais anos{" "*39}{bcolors.PURPLE}{bigheight}{bcolors.RESET}')
print(f'{bcolors.PURPLE}{heightlefth}{" "*57}{bigheight}{bcolors.RESET}')
print(f'{bcolors.PURPLE}{heightlefth}{" "*57}{bigheight}{bcolors.RESET}')










print(f'{bcolors.PURPLE}{heightlefth}{bcolors.RESET}{bcolors.GREY}{bcolors.BOLD}{"1º ano: "}{box*19}{"─"*13}> Alunos: {ano_1:,}  {bcolors.PURPLE}{bigheight}{bcolors.RESET}')

print(f'{bcolors.PURPLE}{heightlefth}{bcolors.RESET}{bcolors.BOLD}{bcolors.RED}{"2º ano: "}{box*30}{"─"*2}> Alunos: {ano_2:,}  {bcolors.PURPLE}{bigheight}{bcolors.RESET}')

print(f'{bcolors.PURPLE}{heightlefth}{bcolors.RESET}{bcolors.GREY}{bcolors.BOLD}{"3º ano: "}{box*24}{"─"*8}> Alunos: {ano_3:,}{" "*2}{bcolors.PURPLE}{bigheight}{bcolors.RESET}')

print(f'{bcolors.PURPLE}{heightlefth}{" "*57}{bigheight}{bcolors.RESET}')
        
print(f'{bcolors.PURPLE}{inferior_left}{minibox*57}{inferior_right}{bcolors.RESET}\n\n\n')
