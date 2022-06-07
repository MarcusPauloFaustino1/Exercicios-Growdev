'''Escreva um programa que leia a idade e salário de 10 pessoas. Informe em
seguida:
a) Qual é a média de idade entre as pessoas?
b) Quantas pessoas há por faixa etária, considerando:
i) jovens < 18
ii) 18 <= adultos < 60
iii) idosos >= 60
c) Em seguida, mostre qual é a faixa etária que acumula o maior salário.'''

listaIdade = []

listaMenor = []
listaMenorSal = []

listaAdultos = []
listaAdultosSal = []

listaIdosos = []
listaIdososSal = []


print(f'\n{" IDADES E SALÁRIOS ":=^60}\n')

for i in range(10):
    idade = int(input('Digite sua idade: '))
    salario = float(input('Digite seu salário: '))
    listaIdade.append(idade)
    if idade < 18:
        listaMenor.append(idade)
        listaMenorSal.append(salario)
    elif idade >= 18 and idade < 60:
        listaAdultos.append(idade)
        listaAdultosSal.append(salario)
    else:
        listaIdosos.append(idade)
        listaIdososSal.append(salario)

mediaIdade = sum(listaIdade) / len(listaIdade)

numeroMenor = len(listaMenor)
numeroAdultos = len(listaAdultos)
numeroIdosos = len(listaIdosos)

try: 
    idososMax = max(listaIdososSal)
except ValueError:
    idososMax = 0
try: 
    adultosMax = max(listaAdultosSal)
except ValueError:
    adultosMax = 0    
try: 
    menorMax = max(listaMenorSal)
except ValueError:
    menorMax = 0   


if menorMax > adultosMax and menorMax > idososMax:
    maiorSal = "JOVENS"
elif adultosMax > menorMax and adultosMax > idososMax:
    maiorSal = "ADULTOS"
elif idososMax > menorMax and idososMax > adultosMax:
    maiorSal = "IDOSOS"


print(f'\n{"─"*60}\n')


print(f'Média da Idade:{mediaIdade:.2f}\n')
print(f'Número de Jovens:{numeroMenor}\n')
print(f'Número de Adultos:{numeroAdultos}\n')
print(f'Número de Idosos:{numeroIdosos}\n')
print(f'Maior Salário (pertence):{maiorSal}\n')

print(f'{"="*60}\n')



