'''7) Qual dos anos (1o, 2o ou 3o) mais procura a monitoria?. Crie um gráfico para
mostrar esses dados.'''

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



''' descobrindo quantos buscaram monitoria em cada ano '''

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


''' descobrindo ano com maior busca por monitorias'''

mais_monitorias = 0    # método de contador
for key in monitored:
    if monitored[key] > mais_monitorias:
        mais_monitorias = monitored[key]
        ano_mais_monitorias = key
        
count = 0        
for key in monitored:
    if monitored[key] < mais_monitorias:
        ano_x = key
        numero_ano_x = monitored[key]
        count += 1
    if count == 1 and monitored[key] < mais_monitorias:
        ano_y = key
        numero_ano_y = monitored[key]
        
        
        
''' outputs '''

box = Box()               # classe referente às caixas de contorno

colors = Colors()         # classe referente às cores

print(f'\n\n{colors.blue}{" "*10}{box.corner1}{"─"*36}{box.corner3}')    
print(f'{box.heightbox}{box.minibox*9}{colors.reset}{colors.bold}',end="")
print(f'{"  MAIOR PROCURA POR MONITORIA ─ ANOS  "}{colors.blue}{box.minibox*9}{box.heightbox}')
print(f'{box.heightleft}{" "*9}{box.corner2}{"─"*36}{box.corner4}{" "*9}{box.bigheight}')
print(f'{box.heightleft}{" "*56}{box.bigheight}')
print(f'{box.heightleft}{colors.purple}   {box.box}{colors.reset}   ',end="")
print(f'Ano com maior procura por monitoria{" "*14}{colors.blue}{box.bigheight}')
print(f'{box.heightleft}{" "*56}{box.bigheight}')
print(f'{box.heightleft}   {colors.grey}{box.box}{colors.reset}   ',end="")
print(f'Demais anos{" "*38}{colors.blue}{box.bigheight}')
print(f'{box.heightleft}{colors.grey}{" "*56}{colors.blue}{box.bigheight}')

print(f'{box.heightleft}{colors.grey}{colors.bold} {ano_y}: {box.box*19}{"─"*12}',end="")
print(f'>  Alunos: {numero_ano_y:,}  {colors.blue}{box.bigheight}')

print(f'{box.heightleft}{colors.bold}{colors.purple}',end="")
print(f' {ano_mais_monitorias}: {box.box*22}{"─"*9}>  Alunos: {mais_monitorias:,}  {colors.blue}{box.bigheight}')

print(f'{box.heightleft}{colors.grey} {ano_x}: {box.box*21}{"─"*10}',end="")
print(f'>  Alunos: {numero_ano_x:,}{" "*2}{colors.blue}{box.bigheight}')

print(f'{box.heightleft}{colors.grey}{" "*56}{colors.blue}{box.bigheight}')
        
print(f'{box.inferior_left}{box.minibox*56}{box.inferior_right}\n\n\n')



''' plotando grafico'''

plt.bar('1º ', numero_ano_y, label = f'{ano_y}: {numero_ano_y} alunos', color = 'C7')
plt.bar('2º ', mais_monitorias, label = f'{ano_mais_monitorias}: {mais_monitorias} alunos (maior procura)', color = 'm')
plt.bar('3º ', numero_ano_x, label = f'{ano_x}: {numero_ano_x} alunos', color = 'C7')

plt.title('ANO COM MAIOR PROCURA POR MONITORIA', fontweight ='bold', fontsize = 15)
plt.ylabel('Nº de reprovações', fontweight ='bold', fontsize = 15)
plt.xlabel('ANOS', fontweight ='bold', fontsize = 15)

plt.legend()
plt.show()