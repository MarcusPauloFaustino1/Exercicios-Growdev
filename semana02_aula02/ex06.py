'''Numa determinada escola, os critérios de aprovação são os seguintes:
a) O aluno deve ter, no máximo, 25% de faltas;
b) A nota final deve ser igual ou superior a 7,00.
Construa um algoritmo para ler as notas que um aluno tirou nos 4 bimestres,
o número total de aulas e o número de faltas, mostrando ao final a situação
do aluno como sendo “Aprovado”, “Reprovado por Faltas” e “Reprovado por
média”, considerando que a reprovação por faltas se sobrepõe a reprovação
por nota.'''

from time import sleep


print(f"\n{'RESULTADO ANUAL DE NOTAS':=^70}\n")

n1 = float(input("Digite suas notas:\nNota 1:"))
n2 = float(input("Nota 2:"))
n3 = float(input("Nota 3:"))
n4 = float(input("Nota 4:"))

print(f"\n{'_':_^70}\n")

aulasTotal = int(input("\n\Digite o número total de aulas:"))
faltas = int(input("\nDigite o número de faltas:"))

print(f"\n{'_':_^70}\n")
print('Resultado:')
sleep(2)

media = (n1 + n2 + n3 + n4) / 4

if faltas > aulasTotal * 0.25:
    print(f"\n{'REPROVADO por Faltas':*^50}\n")
    print(f"\n{'=':=^70}\n")
elif media < 7:
    print(f"\n{'REPROVADO por Média':*^50}\n")
    print(f"\n{'=':=^70}\n")
else:
    print(f"\n{'APROVADO':*^50}\n")
    print(f"\n{'=':=^70}\n")
