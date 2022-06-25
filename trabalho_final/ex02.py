'''2) Quantos alunos do 1o ano foram aprovados sem exame?'''

import csv
from termios import CIBAUD
from dataset import read_data, convert_to_dicionary
import os

os.system('clear')

filename = 'alunos.csv'

#leitura de Arquivo

data = read_data(filename)

register = len(data)

#transformação dos registros para dicionario (convertendo valores)
    
info = convert_to_dicionary(data)

aproved_without_exam = 0
for line in info:
    year = line['ano']
    grade_1 = line['nota_semestre_1']
    grade_2 = line['nota_semestre_2']
    mean = (grade_2 + grade_1)/2
    exam = line['nota_exame']
    faults = line['faltas']
    if year == 1 and exam == 0 and mean >= 7 and faults < 16:
        aproved_without_exam += 1
        
    
class bcolors:
    GREEN = '\033[92m' 
    PURPLE = '\033[95m'
    YELLOW = '\033[93m'
    CYAN = '\033[96m'
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

print(f'\n\n{bcolors.PURPLE}{" "*10}{corner1}{"─"*42}{corner3}{bcolors.RESET}')    
print(f'{bcolors.CYAN}{heightbox}{bcolors.RESET}{bcolors.PURPLE}{minibox*9}{bcolors.RESET}{bcolors.BOLD}{" Nº DE ALUNOS DO 1º ANO APROVADOS SEM EXAME "}{bcolors.CYAN}{minibox*9}{bcolors.RESET}{bcolors.PURPLE}{heightbox}{bcolors.RESET}\n{bcolors.CYAN}{heightlefth}{" "*9}{bcolors.CYAN}{corner2}{"─"*42}{corner4}{bcolors.RESET}{bcolors.PURPLE}{" "*9}{bigheight}{bcolors.RESET}')

print(f'{bcolors.CYAN}{heightlefth}{bcolors.RESET} {" "*61}{bcolors.PURPLE}{bigheight}{bcolors.RESET}')
print(f'{bcolors.CYAN}{heightlefth}{bcolors.RESET}{" "*28}{bcolors.BOLD}{"1 4 9"}{bcolors.PURPLE}{" "*29}{bigheight}{bcolors.RESET}\n{bcolors.CYAN}{heightlefth}{bcolors.RESET}{" "*15}{"alunos foram aprovados no 1º ano"}{" "*15}{bcolors.PURPLE}{bigheight}{bcolors.RESET}\n{bcolors.CYAN}{heightlefth}{bcolors.RESET}{" "*27}{"sem exame"}{" "*26}{bcolors.PURPLE}{bigheight}{bcolors.RESET}\n{bcolors.CYAN}{heightlefth}{bcolors.RESET}{" "*62}{bcolors.PURPLE}{bigheight}{bcolors.RESET}')
print(f'{bcolors.CYAN}{inferior_left}{minibox*31}{bcolors.RESET}{bcolors.PURPLE}{minibox*31}{inferior_right}{bcolors.RESET}\n\n\n')