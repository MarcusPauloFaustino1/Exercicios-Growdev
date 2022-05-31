coordenada_1_x = float(input("Digite a posição x do primeiro ponto:"))

coordenada_1_y = float(input("Digite a posição y do primeiro ponto"))

coordenada_2_x = float(input("Digite a posição x do segundo ponto:"))

coordenada_2_y = float(input("Digite a posição y do segundo ponto:"))

distancia = ((coordenada_1_x - coordenada_1_y)**2 + (coordenada_2_x - coordenada_2_y)**2)**0.5

print(f"A dintâcia entre os dois pontos é de {distancia:.2f}   .")