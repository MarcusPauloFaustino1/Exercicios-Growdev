'''4) De todos os alunos que reprovaram quantos foram por falta e quantos foram
por nota, e quantos foram por ambas as causas?'''

from functions import Box, Colors
from dataset import read_data, convert_to_dicionary
import os
import csv

os.system('clear')


''' leitura de Arquivo '''

filename = 'alunos.csv'    # variavel para arquivo

data = read_data(filename)    # variavel leitura de arquivo



''' transformação dos registros para dicionario (convertendo valores) '''
    
info = convert_to_dicionary(data)    # converte para dicionario




''' descobrindo numero de reprovações por seus respectivos motivos'''

reproved = {'faults_grade': 0, 'faults': 0,'grade': 0 }    # metodo diconario

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



''' outputs '''        

box = Box()               # classe referente às caixas de contorno

colors = Colors()         # classe referente às cores


grade = reproved['grade']    # separando número de reprovados por nota
faults_grade = reproved['faults_grade']    # separando número de reprovados por nota e faltas
faults = reproved['faults']    # separando número de reprovados por faltas

print(f'\n\n{colors.red}{" "*10}{box.corner1}{"─"*36}{box.corner3}')    # linhas_titulo_superior     
print(f'{colors.grey}{box.heightbox}{colors.red}{box.minibox*9}{colors.reset}',end="")    # caixas_teto
print(f'{colors.bold}{" QUANTIDADES E MOTIVOS DE REPROVAÇÕES "}{colors.grey}{box.minibox*8}',end="")    # titulo e caixas_teto
print(f'{colors.red}{box.heightbox}')    # caixas_teto
print(f'{colors.grey}{box.heightleft}{" "*9}{box.corner2}{"─"*36}{box.corner4}',end="")    # linhas_titulo_inferior
print(f'{colors.red}{" "*8}{box.bigheight}')    # caixa_parede
print(f'{colors.grey}{box.heightleft} {" "*54}{colors.red}{box.bigheight}')    # caixa_parede

print(f'{colors.grey}{box.heightleft}{colors.reset}{colors.bold}{"nota e faltas: "}{colors.yellow}',end="")    # caixa_parede e texto_notas_faltas
print(f'{box.box*18}{"─"*13}>   {colors.reset}{faults_grade:,}  {colors.red}{box.bigheight}')    # resultado notas_faltas


print(f'{colors.grey}{box.heightleft}{colors.reset}{colors.bold}{"nota:          "}',end="")    # caixa_parede e texto_notas
print(f'{colors.cyan}{box.box*20}{"─"*11}> {colors.reset}{grade:,}  {colors.red}{box.bigheight}')    # resultado notas


print(f'{colors.grey}{box.heightleft}{colors.reset}{colors.bold}{"faltas:        "}',end="")    # caixa_parede e texto_faltas
print(f'{colors.purple}{box.box*28}{"─"*3}> {colors.reset}{faults:,}{" "*2}{colors.red}{box.bigheight}')    # resultado faltas


print(f'{colors.grey}{box.heightleft} {" "*54}{colors.red}{box.bigheight}')    # caixas_parede
        
print(f'{colors.grey}{box.inferior_left}{box.minibox*27}',end="")   # quina e piso
print(f'{colors.red}{box.minibox*28}{box.inferior_right}\n\n\n')    # quina e piso
