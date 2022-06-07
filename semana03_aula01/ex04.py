'''A prefeitura de uma cidade fez uma pesquisa entre seus habitantes,
coletando dados sobre o salário e número de filhos. A prefeitura deseja
saber:
a) média do salário da população;
b) média do número de filhos;
c) maior salário;
d) percentual de pessoas com salário até R$2000,00.
Escreva um programa que receba as informações necessárias de 5 pessoas
conforme a descrição e responda às questões a, b, c e d anteriores.'''

print(f'\n{"ESTATÍSTICAS DA POPULAÇÃO":=^70}\n')

#DADOS DE ENTRADA

listaSalario = []
lista2000 = []
salariosMed = 0
filhosMed = 0
for n in range(1,6):
    salario = int(input(f'Digite o salário da {n}ª pessoa: '))
    if salario <= 2000:
        lista2000.append(salario)
    filhos = int(input(f'Digite o número de filhos da {n}ª pessoa: '))
    listaSalario.append(salario)
    salariosMed += salario
    filhosMed += filhos

salariosMed /= 5
filhosMed /= 5
salarioMax = max(listaSalario)
percentSal2000 = (100 * len(lista2000))/5

#DADOS DE SAÍDA

print(f'\n{"_"*70}\n')

print(f'Salário médio (R$): {" ":>38}{salariosMed:.2f}\n')
print(f'Média de filhos: {" ":>41}{filhosMed:.2f}\n')
print(f'Maior salário: (R$) {" ":>38}{salarioMax}\n')
print(f'Percentual de pessoal com salário até R$2000: {" ":>12}{percentSal2000}%\n')

print(f'{"="*70}\n')
