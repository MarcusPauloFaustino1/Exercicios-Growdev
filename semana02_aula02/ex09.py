'''Escreva um programa que peça ao usuário para fornecer um dia, mês e o
ano arbitrários e determine se esses dados correspondem a uma data válida.
Não deixe de considerar que existem meses com 30 e 31 dias, e que
fevereiro pode ter 28 ou 29 dias, dependendo se o ano for bissexto.
Considere que um ano é bissexto quando for divisível por 4.'''

print(f"\n{'DATA VÁLIDA/INVÁLIDA':=^50}\n")

dia = int(input("Digite, em números, um dia do mês:"))
mes = int(input("Digite, em números, um mês:"))
ano = int(input("Digite, em quatro digitos, um ano:"))

ano1 = ano * 0.01
ano1 = int(ano1) * 100
anoFinal = ano - ano1

print(f"\n{'_':_^50}\n")

print(f"Data: {dia} / {mes} / {ano}")

if dia > 31 or mes > 12:
    print("Data INVÁLIDA")
elif dia == 29 and mes == 2 and anoFinal % 4 == 0:
    print("Data VÁLIDA")
elif dia > 28 and mes == 2:
    print("Data INVÁLIDA")
elif dia > 31 and (mes == 1 or mes == 3 or mes == 5 or mes == 7 or mes == 8 or mes == 10 or mes == 12):
    print("Data INVÁLIDA")
elif dia > 30 and (mes == 4 or mes == 6 or mes == 9 or mes == 11):
    print("Data INVÁLIDA")
elif dia <= 31 and (mes == 1 or mes == 3 or mes == 5 or mes == 7 or mes == 8 or mes == 10 or mes == 12):
    print("Data VÁLIDA")
elif dia <= 30 and (mes == 4 or mes == 6 or mes == 9 or mes == 11):
    print("Data VÁLIDA")

print(f"\n{'=':=^50}\n")