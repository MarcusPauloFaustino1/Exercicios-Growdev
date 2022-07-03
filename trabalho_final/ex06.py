'''6) As reprovações são maiores entre os alunos do 1o, 2o ou 3o ano?. Crie um
gráfico para mostrar isso.'''


from dataset import read_data, convert_to_dicionary
from functions import Box, Colors
import matplotlib.pyplot as plt
import os
import csv

os.system('clear')



''' leitura de Arquivo '''

filename = 'alunos.csv'    # variavel para arquivo

data = read_data(filename)    # variavel leitura de arquivo



''' transformação dos registros para dicionario (convertendo valores) '''
    
info = convert_to_dicionary(data)    # converte para dicionario



''' descobrindo reprovações '''

reproved = {'1º ano': 0, '2º ano': 0, '3º ano':0}    # metodo diconario
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



''' descobrindo ano com maiores reprovações'''

mais_reprovacoes = 0    # método de contador
for key in reproved:
    if reproved[key] > mais_reprovacoes:
        mais_reprovacoes = reproved[key]
        ano_mais_reprovacoes = key
        
count = 0        
for key in reproved:
    if reproved[key] < mais_reprovacoes:
        ano_x = key
        numero_ano_x = reproved[key]
        count += 1
    if count == 1 and reproved[key] < mais_reprovacoes:
        ano_y = key
        numero_ano_y = reproved[key]    
        
        
        
''' outputs '''

box = Box()               # classe referente às caixas de contorno

colors = Colors()         # classe referente às cores

print(f'\n\n{colors.purple}{" "*10}{box.corner1}{"─"*37}{box.corner3}')    
print(f'{box.heightbox}{box.minibox*9}{colors.reset}',end="")
print(f'{colors.bold}{" MAIORES REPROVAÇÕES ─ 1º, 2º E 3º ANO "}{colors.purple}{box.minibox*9}{box.heightbox}')
print(f'{box.heightleft}{" "*9}{box.corner2}{"─"*37}{box.corner4}{" "*9}{box.bigheight}')
print(f'{box.heightleft}{" "*57}{box.bigheight}')
print(f'{box.heightleft}{colors.red}   {box.box}{colors.reset}   ',end="")
print(f'Ano com maiores reprovações{" "*23}{colors.purple}{box.bigheight}')
print(f'{box.heightleft}{" "*57}{box.bigheight}')
print(f'{box.heightleft}   {colors.grey}{box.box}{colors.reset}   ',end="")
print(f'Demais anos{" "*39}{colors.purple}{box.bigheight}')
print(f'{box.heightleft}{" "*57}{box.bigheight}')
print(f'{box.heightleft}{" "*57}{box.bigheight}')


print(f'{colors.purple}{box.heightleft}{colors.grey}{colors.bold}{ano_y}: ',end="")
print(f'{box.box*19}{"─"*13}> Alunos: {numero_ano_y:,}  {colors.purple}{box.bigheight}')

print(f'{box.heightleft}{colors.bold}{colors.red}{ano_mais_reprovacoes}: ',end="")
print(f'{box.box*30}{"─"*2}> Alunos: {mais_reprovacoes:,}  {colors.purple}{box.bigheight}')

print(f'{box.heightleft}{colors.grey}{colors.bold}{ano_x}: ',end="")
print(f'{box.box*24}{"─"*8}> Alunos: {numero_ano_x:,}{" "*2}{colors.purple}{box.bigheight}')

print(f'{box.heightleft}{" "*57}{box.bigheight}')
        
print(f'{box.inferior_left}{box.minibox*57}{box.inferior_right}\n\n\n')



''' plotando grafico '''

plt.bar(ano_y, numero_ano_y, label = f'{ano_x}: {numero_ano_x} reprovações', color = 'C7')
plt.bar(ano_mais_reprovacoes, mais_reprovacoes, label = f'{ano_mais_reprovacoes}: {mais_reprovacoes} reprovações (maior nº)', color = 'r')
plt.bar(ano_x, numero_ano_x, label = f'{ano_y}: {numero_ano_y} reprovações', color = 'C7')

plt.title('ANO COM MAIOR Nº REPROVAÇÕES', fontweight ='bold', fontsize = 15)
plt.ylabel('Nº de reprovações', fontweight ='bold', fontsize = 15)

plt.legend()
plt.show()

