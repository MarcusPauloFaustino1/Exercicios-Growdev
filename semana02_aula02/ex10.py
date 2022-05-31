'''Construa um algoritmo que leia uma data qualquer (dia, mês e ano) e calcule
a data do próximo dia. Lembre-se que em anos bissextos o mês de fevereiro
tem 29 dias. Lembre-se que um ano é bissexto quando for divisível por 4.'''

from http.client import PROXY_AUTHENTICATION_REQUIRED
from time import sleep

print(f"\n{'CALCULANDO O PRÓXIMO DIA':=^50}\n")
dia = int(input("Digite, em números, um dia do mês:"))
mes = int(input("Digite, em números, um mês:"))
ano = int(input("Digite, em quatro digitos, um ano:"))

ano1 = ano * 0.01
ano1 = int(ano1) * 100
anoFinal = ano - ano1

proxDia = dia  
proxMes = mes 
proxAno = ano 

if dia == 31 and mes == 12:
    proxAno = ano + 1
    proxMes = 1
    proxDia = 1
elif dia < 31 and (mes == 1 and mes == 3 or mes == 5 or mes == 7 or mes == 8 or mes == 10 or mes == 12):
    proxDia = dia + 1
elif dia < 30 and (mes == 4 or mes == 6 or mes == 9 or mes == 11):
    proxDia = dia + 1
elif dia == 31 and (mes == 1 or mes == 3 or mes == 5 or mes == 7 or mes == 8 or mes == 10):
    proxMes = mes + 1
    proxDia = 1
elif dia == 30 and (mes == 4 or mes == 6 or mes == 9 or mes == 11):
    proxMes = mes + 1
    proxDia = 1

print('Calculando...')
sleep(2)

print(f"\n{'_':_^50}\n")

print(f"Data: {dia} / {mes} / {ano}")

if dia > 31 or mes > 12:
    print("Data INVÁLIDA")
    exit()
elif dia == 29 and mes == 2 and anoFinal % 4 == 0:
    print("Data VÁLIDA")
elif dia > 28 and mes == 2:
    print("Data INVÁLIDA")
    exit()
elif dia > 31 and (mes == 1 or mes == 3 or mes == 5 or mes == 7 or mes == 8 or mes == 10 or mes == 12):
    print("Data INVÁLIDA")
    exit()
elif dia > 30 and (mes == 4 or mes == 6 or mes == 9 or mes == 11):
    print("Data INVÁLIDA")
    exit()
else:
    print("Data VÁLIDA")

print(f"\n{'_':_^50}\n")

print(f"Próxima data: {proxDia} / {proxMes} / {proxAno}")

print(f"\n{'=':=^50}\n")