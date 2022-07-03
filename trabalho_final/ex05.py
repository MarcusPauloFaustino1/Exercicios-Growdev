'''5) Qual a média de todas as notas (do 1o e 2o semestre) dos alunos do 2o ano?'''

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



''' descobrindo as medias dos alunos do 2º ano '''

grades = []    # metodo lista
for line in info:
    year = line['ano']
    grade_1 = line['nota_semestre_1']
    grade_2 = line['nota_semestre_2']
    
    if year == 2:
        grades.append(grade_1)
        grades.append(grade_2)
    
mean = sum(grades) / len(grades)    # calculando media geral 



''' outputs '''        

box = Box()               # classe referente às caixas de contorno

colors = Colors()         # classe referente às cores


print(f'\n\n{colors.yellow}{box.corner1}{"─"*23}{box.corner3}{colors.reset}')   # linhas_titulo
print(f'{colors.bold}{colors.cyan}  MÉDIA GERAL DO 2º ANO')   # titulo
print(f'{colors.yellow}{box.heightbox}{box.minibox*23}{box.heightbox}')    # caixas_teto
print(f'{box.heightleft}{" "*23}{box.bigheight}')    # caixas_parede
print(f'{box.heightleft}{" "*23}{box.bigheight}')    # caixas_parede
print(f'{box.heightleft}{colors.reset}   Média:{colors.bold}',end="")    # caixa_parede e texto_media
print(f'{colors.cyan}{mean:^ 14.2f}{colors.yellow}{box.bigheight}')      # resultado e caixa_parede
print(f'{box.heightleft}{" "*23}{box.bigheight}')    # caixas_parede
print(f'{box.heightleft}{" "*23}{box.bigheight}')    # caixas_parede
print(f'{box.inferior_left}{box.minibox*23}{box.inferior_right}\n\n\n')    # quina e piso
    