'''Após construir o algoritmo anterior, crie mais duas versões dele para prever
as seguintes situações:
a) Um aluno pode ficar em recuperação se possuir frequência suficiente
(superior a 75%) e média superior a 5 mas inferior a 7;
b) Caso um aluno reprove por média e faltas, sua situação deve ser
“Reprovado por Média e Faltas” (ao invés de simplesmente
“Reprovado por Faltas” como antes).'''


from time import sleep


print(f"\n{'RESULTADO ANUAL DE NOTAS':=^70}\n")

n1 = float(input("Digite suas notas:\nNota 1:"))
n2 = float(input("Nota 2:"))
n3 = float(input("Nota 3:"))
n4 = float(input("Nota 4:"))

print(f"\n{'_':_^70}\n")

aulasTotal = int(input("\nDigite o número total de aulas:"))
faltas = int(input("\nDigite o número de faltas:"))

print(f"\n{'_':_^70}\n")
print('Resultado:')
sleep(2)

media = (n1 + n2 + n3 + n4) / 4

if faltas > aulasTotal * 0.25 and media < 5:
    print(f"\n{'REPROVADO por Média e Faltas':*^50}\n")
    print(f"\n{'=':=^70}\n")
elif faltas > aulasTotal * 0.25:
    print(f"\n{'REPROVADO por Faltas':*^50}\n")
    print(f"\n{'=':=^70}\n")
elif media > 5 and media < 7:
    print(f"\n{'RECUPERAÇÃO':*^50}\n")
    print(f"\n{'=':=^70}\n")
elif media < 5:
    print(f"\n{'REPROVADO por Média':*^50}\n")
    print(f"\n{'=':=^70}\n")

else:
    print(f"\n{'APROVADO':*^50}\n")
    print(f"\n{'=':=^70}\n")
