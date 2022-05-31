'''Escreva um algoritmo para ler uma temperatura em graus Fahrenheit,
calcular e escrever o valor correspondente em graus Celsius (baseado na
fórmula abaixo):

C / 9 = (F - 32) * 5             '''

from time import sleep


print(f"\n{'FAHRENHIT -> CELSIUS':=^70}\n")

F = float(input("Digite a temperatura em Fahrenheit(°F):"))

C = ((F - 32) * 5) / 9

print('Convertendo...')
sleep(2)
print(f"\n{'_':_^70}\n")
print(F"A temperatura de {F}°F (Fahrenheit) corresponde a {C:.1f}°C (Celsius).")
print(f"\n{'=':=^70}\n")

