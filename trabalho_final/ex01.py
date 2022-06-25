'''1) Quantos alunos estudam em cada escola, e qual a escola com mais alunos?'''

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

escolas = {}
for line in info:
    escola = line['escola']
    if escola not in escolas:
        escolas[escola] = 1
    elif escola in escolas:
        escolas[escola] += 1

mais_alunos = 0
for escola in escolas:
    if escolas[escola] > mais_alunos:
        mais_alunos = escolas[escola]
        
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


print(f'\n\n{bcolors.CIAN}{" "*27}{corner1}{"─"*28}{corner3}{bcolors.RESET}')    
print(f'{bcolors.CIAN}{heightbox}{minibox*26}{bcolors.BOLD}{" RELAÇÃO DE ALUNOS POR ESCOLA "}{minibox*25}{heightbox}\n{heightlefth}{" "*26}{corner2}{"─"*28}{corner4}{" "*25}{bigheight}{bcolors.RESET}')

print(f'{bcolors.CIAN}{heightlefth}{bcolors.RESET}   {bcolors.GREEN}{box}{bcolors.RESET}   Escola com mais alunos{" "*52}{bcolors.CIAN}{bigheight}{bcolors.RESET}')
print(f'{bcolors.CIAN}{heightlefth}{bcolors.RESET}{" "*81}{bcolors.CIAN}{bigheight}{bcolors.RESET}\n{bcolors.CIAN}{heightlefth}{bcolors.RESET}   {bcolors.GREY}{box}{bcolors.RESET}   Demais escolas{" "*60}{bcolors.CIAN}{bigheight}{bcolors.RESET}\n{bcolors.CIAN}{heightlefth}{bcolors.RESET}{" "*81}{bcolors.CIAN}{bigheight}{bcolors.RESET}\n{bcolors.CIAN}{heightlefth}{bcolors.RESET}{" "*81}{bcolors.CIAN}{bigheight}{bcolors.RESET}')

c = 0
for key in escolas.keys():
    espaco = 17 - len(key)
    if escolas[key] == mais_alunos:
        print(f'{bcolors.CIAN}{heightlefth}{bcolors.RESET}   {bcolors.GREEN}{bcolors.BOLD}{key}:{" "*espaco}{bcolors.RESET} {bcolors.GREEN}{box*(int((escolas[key]*10)/200))}{bcolors.RESET}{" "*(45 - int((escolas[key]*10)/200))} {bcolors.GREEN}{bcolors.BOLD}Alunos: {escolas[key]}{bcolors.RESET}  {bcolors.CIAN}{bigheight}{bcolors.RESET}')
         
    elif c % 2 == 0:
        print(f'{bcolors.CIAN}{heightlefth}{bcolors.RESET}   {key}:{" "*espaco} {bcolors.GREY}{box*(int((escolas[key]*10)/200))}{bcolors.RESET}{" "*(45 - int((escolas[key]*10)/200))} Alunos: {escolas[key]}  {bcolors.CIAN}{bigheight}{bcolors.RESET}')
    
    elif c % 2 != 0:
        print(f'{bcolors.CIAN}{heightlefth}{bcolors.RESET}   {key}:{" "*espaco} {bcolors.GREY}{box*(int((escolas[key]*10)/200))}{bcolors.RESET}{" "*(45 - int((escolas[key]*10)/200))} Alunos: {escolas[key]}  {bcolors.CIAN}{bigheight}{bcolors.RESET}')
    
    c += 1
    
print(f'{bcolors.CIAN}{heightlefth}{" "*81}{bigheight}\n{heightlefth}{" "*81}{bigheight}\n{heightlefth}{" "*81}{bigheight}\n{inferior_left}{bcolors.RESET}',end="")
print(f'{bcolors.CIAN}{minibox*81}{inferior_right}{bcolors.RESET}\n\n\n')