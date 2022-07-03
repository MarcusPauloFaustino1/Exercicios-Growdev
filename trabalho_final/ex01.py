'''1) Quantos alunos estudam em cada escola, e qual a escola com mais alunos?'''

from dataset import read_data, convert_to_dicionary
from functions import Box, Colors
import csv
import os

os.system('clear')



''' leitura de Arquivo '''

filename = 'alunos.csv'    # variavel para arquivo

data = read_data(filename)    # variavel leitura de arquivo



''' transformação dos registros para dicionario (convertendo valores) '''
    
info = convert_to_dicionary(data)    # converte para dicionario



''' criando novo dicionario com nomes das escolas e seus respectivos numeros de alunos '''

escolas = {}
for line in info:
    escola = line['escola']
    if escola not in escolas:
        escolas[escola] = 1
    elif escola in escolas:
        escolas[escola] += 1



'''descobrindo qual escola tem mais alunos'''

mais_alunos = 0
for escola in escolas:
    if escolas[escola] > mais_alunos:
        mais_alunos = escolas[escola]
        
        
        
''' outputs '''
        
box = Box()               # classe referente às caixas de contorno

colors = Colors()         # classe referente às cores


print(f'\n\n{colors.cyan}{" "*27}{box.corner1}{"─"*28}{box.corner3}')    # linhas_titulo
print(f'{colors.cyan}{box.heightbox}{box.minibox*26}{colors.reset}{colors.bold}',end="")    # caixas_teto
print(f'{" RELAÇÃO DE ALUNOS POR ESCOLA "}{colors.cyan}{box.minibox*25}{box.heightbox}')    # titulo e caixas_teto
print(f'{box.heightleft}{" "*26}{box.corner2}{"─"*28}{box.corner4}{" "*25}{box.bigheight}')    # caixas_paredes e linhas_titulo

print(f'{colors.cyan}{box.heightleft}   {colors.green}{box.box}{colors.reset}',end="")    # caixa_parede e caixa_legenda
print(f'   Escola com mais alunos{" "*52}{colors.cyan}{box.bigheight}')     # texto_legenda e caixas_parede
print(f'{box.heightleft}{" "*81}{box.bigheight}')    # caixas_parede
print(f'{box.heightleft}',end="")  # caixa_parede
print(f'{colors.grey}   {box.box}{colors.reset}   Demais escolas',end="")    # legenda_1
print(f'{" "*60}{colors.cyan}{box.bigheight}')    # caixa_parede
print(f'{box.heightleft}{" "*81}{box.bigheight}\n{box.heightleft}{" "*81}{box.bigheight}')    # caixas_parede

# mini grafico: escolas - alunos
c = 0
for key in escolas.keys():
    espaco = 17 - len(key)
    if escolas[key] == mais_alunos:
        print(f'{colors.cyan}{box.heightleft}   {colors.green}{colors.bold}{key}:',end="")
        print(f'{" "*espaco} {colors.green}{box.box*(int((escolas[key]*10)/200))}',end="")
        print(f'{" "*(45 - int((escolas[key]*10)/200))} {colors.green}{colors.bold}',end="")
        print(f'Alunos: {escolas[key]}  {colors.cyan}{box.bigheight}')
         
    elif c % 2 == 0:
        print(f'{colors.cyan}{box.heightleft}   {colors.reset}{key}:{" "*espaco}',end="") 
        print(f' {colors.grey}{box.box*(int((escolas[key]*10)/200))}{colors.reset}',end="")
        print(f'{" "*(45 - int((escolas[key]*10)/200))} Alunos: {escolas[key]} ',end="") 
        print(f' {colors.cyan}{box.bigheight}')
    
    elif c % 2 != 0:
        print(f'{colors.cyan}{box.heightleft}   {colors.reset}{key}:',end="")
        print(f'{" "*espaco} {colors.grey}{box.box*(int((escolas[key]*10)/200))}',end="")
        print(f'{colors.reset}{" "*(45 - int((escolas[key]*10)/200))} ',end="") 
        print(f'Alunos: {escolas[key]}  {colors.cyan}{box.bigheight}')
    
    c += 1
    
# parte de baixo da caixa de contorno

print(f'{colors.cyan}{box.heightleft}{" "*81}{box.bigheight}')    # caixas_parede
print(f'{box.heightleft}{" "*81}{box.bigheight}') # caixas_parede
print(f'{box.heightleft}{" "*81}{box.bigheight}\n{box.inferior_left}',end="")   # caixas_parede e quina_esquerda
print(f'{colors.cyan}{box.minibox*81}{box.inferior_right}\n\n\n')    # caixas-piso e quina_direita