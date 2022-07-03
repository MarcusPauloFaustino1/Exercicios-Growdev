'''2) Quantos alunos do 1o ano foram aprovados sem exame?'''


from dataset import read_data, convert_to_dicionary
from functions import Box, Colors
import os
import csv

os.system('clear')



''' leitura de Arquivo '''

filename = 'alunos.csv'    # variavel para arquivo

data = read_data(filename)    # variavel leitura de arquivo



''' transformação dos registros para dicionario (convertendo valores) '''
    
info = convert_to_dicionary(data)    # converte para dicionario



'''calculando quantos alunos do primeiro ano foram aprovados sem exame '''

aproved_without_exam = 0       # método de contador
for line in info:
    year = line['ano']
    grade_1 = line['nota_semestre_1']
    grade_2 = line['nota_semestre_2']
    mean = (grade_2 + grade_1)/2
    exam = line['nota_exame']
    faults = line['faltas']
    if year == 1 and exam == 0 and mean >= 7 and faults < 16:
        aproved_without_exam += 1
        
        

''' outputs '''        
        
box = Box()               # classe referente às caixas de contorno

colors = Colors()         # classe referente às cores

print(f'\n\n{colors.purple}{" "*10}{box.corner1}{"─"*42}{box.corner3}')    # linhas_titulo_superior    
print(f'{colors.cyan}{box.heightbox}{colors.purple}{box.minibox*9}',end="")    # caixas_teto
print(f'{colors.reset}{colors.bold}{" Nº DE ALUNOS DO 1º ANO APROVADOS SEM EXAME "}',end="")    # titulo
print(f'{colors.cyan}{box.minibox*9}{colors.purple}{box.heightbox}')    # caixas_parede
print(f'{colors.cyan}{box.heightleft}{" "*9}{colors.cyan}{box.corner2}{"─"*42}{box.corner4}',end="")    # linhas_titulo_inferior    
print(f'{colors.purple}{" "*9}{box.bigheight}')    # caixas_parede

print(f'{colors.cyan}{box.heightleft} {" "*61}{colors.purple}{box.bigheight}')    # caixas_parede
print(f'{colors.cyan}{box.heightleft}{" "*28}{colors.bold}',end="")    # caixa_parede
print(f'{colors.green}{aproved_without_exam}{colors.purple}{" "*31}{box.bigheight}')   # resultado e caixa_parede
print(f'{colors.cyan}{box.heightleft}{colors.reset}{" "*15}{"alunos foram aprovados no 1º ano"}',end="") # texto e caixa_parede
print(f'{" "*15}{colors.purple}{box.bigheight}')    # caixas_parede
print(f'{colors.cyan}{box.heightleft}{colors.reset}{" "*27}{"sem exame"}',end="")    # texto e caixa_parede
print(f'{" "*26}{colors.purple}{box.bigheight}')    # caixa_parede
print(f'{colors.cyan}{box.heightleft}{" "*62}{colors.purple}{box.bigheight}')    # caixas_parede
print(f'{colors.cyan}{box.inferior_left}{box.minibox*31}{colors.purple}',end="")    # quina e piso
print(f'{box.minibox*31}{box.inferior_right}\n\n\n')    #    quina e piso