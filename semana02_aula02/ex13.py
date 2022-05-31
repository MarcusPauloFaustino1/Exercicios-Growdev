'''Sabendo que há 60 segundos em um minuto, 3.600 segundos em uma hora
e 86.400 segundo em um dia, crie um algoritmo que a partir de uma
determinada quantidade de segundos fornecida pelo usuário, converte-a da
seguinte maneira:
a) Se a quantidade de segundos for maior ou igual a 60, o programa
deverá exibir o número de minutos equivalente;
b) Se a quantidade de segundos for maior ou igual a 3.600, o programa
deverá exibir o número de horas equivalente;
c) Se a quantidade de segundos for maior ou igual a 86.400, o programa
deverá exibir o número de dias equivalente.'''

from time import sleep


print(f"\n{'SEGUNDOS: DIAS, HORAS, MINUTOS E SEGUNDOS':=^70}\n")

min = 60
hora = 3600
dia = 86400

seg = int(input("Digite uma quantidade de segundos:"))

print('Convertendo...')
sleep(2)

nDia = seg / 86400
rDia = seg % 86400 
nHora = rDia / 3600
rHora = rDia % 3600
nMin = rHora / 60
rMin = rHora % 60

print(f"\n{'_':_^70}\n")
if seg >= 86400:
    print(f'Dias: {nDia:.0f}')
    if rDia >= 3600:
        print(f'Horas: {nHora:.0f}')
        if rHora >= 60:
            print(f'Minutos: {nMin:.0f}')
            if (rHora - 60) > 0:
                print(f'Segundos: {rMin}')
                print(f"\n{'=':=^70}\n")
elif seg < 86400 and seg >=3600:
    print(f'Horas: {nHora:.0f}')
    if rHora >= 60:
        print(f'Minutos: {nMin:.0f}')
        if (rHora - 60) > 0:
            print(f'Segundos: {rMin}')
            print(f"\n{'=':=^70}\n")
elif seg < 3600 and seg > 60:
    print(f'Minutos: {nMin:.0f}')
    if (rMin % 60) != 0:
        print(f'Segundos: {rMin}')
        print(f"\n{'=':=^70}\n")
elif seg<= 60:
    print(f'Segundos: {rMin}')
    print(f"\n{'=':=^70}\n")

