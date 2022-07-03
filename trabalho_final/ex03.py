'''3) Quantos alunos do 3o ano reprovaram? e desses quantos procuraram
monitoria?'''

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




''' descobrindo quantos alunos foram reprovados e quantos desses buscaram monitoria '''

reproved = 0    # método de contador
monitored = 0    # método de contador
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
            


''' outputs '''

box = Box()    # classe referente às caixas de contorno

colors = Colors()    # classe referente às cores

print(f'\n\n{colors.blue}{" "*10}{box.corner1}{"─"*34}{box.corner3}')    # linhas_titulo_superior    
print(f'{colors.grey}{box.heightbox}{colors.blue}{box.minibox*9}',end="")    # caixas_teto
print(f'{colors.reset}{colors.bold}{"     ALUNOS REPROVADOS NO 3º ANO    "}',end="")    # titulo
print(f'{colors.grey}{box.minibox*9}{colors.blue}{box.heightbox}')    # caixas_teto
print(f'{colors.grey}{box.heightleft}{" "*9}{box.corner2}{"─"*34}{box.corner4}',end="")    # linhas_titulo_inferior
print(f'{colors.blue}{" "*9}{box.bigheight}')

print(f'{colors.grey}{box.heightleft} {" "*53}{colors.blue}{box.bigheight}')    # caixas_parede
print(f'{colors.grey}{box.heightleft}{colors.reset}{colors.bold}{"Total de alunos reprovados:"}',end="")    # caixa_parede e texto
print(f'{colors.red} {box.box*20} {colors.reset}{reproved}{colors.blue} {box.bigheight}')    # resultado e caixa_parede
print(f'{colors.grey}{box.heightleft}{colors.reset}{colors.bold}{"Destes procuraram mentoria:"}',end="")
print(f'{colors.yellow} {box.box*10} {colors.reset}{monitored}',end="")    # resultado 
print(f'{colors.blue}{" "*12}{box.bigheight}')    # caixa_parede
print(f'{colors.grey}{box.heightleft}{" "*54}{colors.blue}{box.bigheight}')    # caixas_parede
print(f'{colors.grey}{box.heightleft}{" "*54}{colors.blue}{box.bigheight}')    # caixas_parede
print(f'{colors.grey}{box.inferior_left}{box.minibox*27}',end="")    # quina e piso
print(f'{colors.blue}{box.minibox*27}{box.inferior_right}\n\n\n')    # quina e piso 