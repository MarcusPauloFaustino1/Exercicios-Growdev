'''Chico tem 1,50 metro e cresce 2 centímetros por ano, enquanto Zé tem 1,10
metro e cresce 3 centímetros por ano. Construa um programa que calcule e
imprima quantos anos serão necessários para que Zé seja maior que Chico.'''

chico = 1.5
ze = 1.1

anos = 0
while chico > ze:
    chico += 0.02
    ze += 0.03
    anos +=1

print(f'\n{"ZÉ MAIOR QUE CHICO":=^40}\n')    
print(f'Zé será maior que Chico em: {anos} anos.')
print(f'\n{"=":=^40}\n')