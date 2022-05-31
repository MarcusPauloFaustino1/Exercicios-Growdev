'''Faça um algoritmo para ler a temperatura atual e conforme leitura, imprima o
resultado de acordo com a tabela abaixo.

Temperatura              Resultado
até 15°                  Muito frio
de 16° à 22°             Frio
de 23° à 26°             Agradável
de 27° à 30°             Quente
31° ou mais              Muito quente'''

from time import sleep

print(f"\n{'QUENTE OU FRIO?':=^70}")

temperatura = float(input('\nDigite a temperatura atual:'))

print('Medindo a temperatura...')
sleep(2)

print(f"\n{'_':_^70}\n")

if temperatura <= 15:
    print(f'Resultado: {"MUITO FRIO":*^20}')
    print(f"\n{'=':=^70}")
elif temperatura >= 16 and temperatura <= 22:
    print(f'Resultado: {"FRIO":*^20}')
    print(f"\n{'=':=^70}")
elif temperatura >= 23 and temperatura <= 26:
    print(f'Resultado: {"AGRADÁVEL":*^20}')
    print(f"\n{'=':=^70}")
elif temperatura >= 27 and temperatura <= 30:
    print(f'Resultado: {"QUENTE":*^20}')
    print(f"\n{'=':=^70}")
else:
    print(f'Resultado: {"MUITO QUENTE":*^20}')
    print(f"\n{'MISTURANDO AS CORES':=^70}")
