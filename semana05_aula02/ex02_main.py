'''Crie um programa que utilize esta classe. Ele deve pedir
ao usuário que informe as medidas de um local. Depois,
deve-se criar um objeto com as medidas e calcular a
quantidade (em m2) de pisos (1 x 1 m2) e de rodapés
necessários para o local.'''

from math import ceil, floor
from rectangle import Rectangle

base = float(input('Informe a medida (metros) do lado 1: '))
height = float(input('Informe a medida (metros) do lado 2: '))

rectangle = Rectangle(base, height)

floors = 1

baseboard = floors / 10

num_baseboards = 0

num_floors_x = rectangle.area() / floors

if num_floors_x // 1 != 0:
    num_floors = ceil(num_floors_x)
    floor_remnant = num_floors - num_floors_x
    
    if floor_remnant > baseboard:
        num_baseboards = num_baseboards - floor_remnant // baseboard
        floor_remnant = floor_remnant - ((num_baseboards * -1) / 10)
        
        


num_baseboards_y = rectangle.perimeter() + num_baseboards

if num_baseboards_y < 0:
    num_baseboards = 0

elif num_baseboards_y > 0 and floor_remnant > 0:
    num_floors += ceil(num_baseboards_y / 10) 
    floor_remnant = floor_remnant + ((num_baseboards_y/10) - floors) * -1
    
elif num_baseboards_y > 0 and floor_remnant == 0:
    num_floors += ceil(num_baseboards_y / 10) 
    floor_remnant = floor_remnant + ((num_baseboards_y/10) - (floors*2)) * -1



print(f'Pisos totais: {num_floors}\nNº de pisos para o chão: {ceil(num_floors_x)}\nNº de pisos para rodapés: {num_floors - ceil(num_floors_x)}\nNº de rodapés: {rectangle.perimeter()}\nPiso sobressalente: {floor_remnant:.2f}')