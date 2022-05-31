'''18)As Organizações XTC resolveram dar um aumento de salário aos seus
colaboradores e lhe contrataram para desenvolver o programa que calcula os
reajustes. Faça um programa que recebe o salário de um colaborador e o
reajuste segundo o seguinte critério, baseado no salário atual:
a) salários até R$ 280,00 (incluindo): aumento de 20%
b) salários entre R$ 280,00 e R$ 700,00: aumento de 15%
c) salários entre R$ 700,00 e R$ 1500,00: aumento de 10%
d) salários de R$ 1500,00 em diante: aumento de 5%
Após o aumento ser realizado informe na tela:
a) o salário antes do reajuste;

b) o percentual de aumento aplicado;
c) o valor do aumento;
d) o novo salário, após o aumento.'''

print(f'{"REAJUSTE DE SALÁRIO":=^50}')
salario = float(input("Digite seu salário:"))
salario1 = salario

if salario <= 280:
    salario += salario * 0.2    
    print(f"{'_':_^50}\n")
    print(f'Salário atual: R$ {salario1:.2f}')
    print('Percentual de aumento: 20%')
    print(f'Valor do aumento: R$ {salario1 * 0.2}')
    print(f'Novo salário: R$ {salario:.2f}')
    print(f"\n{'=':=^50}")
elif salario > 280 and salario <= 700:
    salario += salario * 0.15
    print(f"{'_':_^50}\n")
    print(f'Salário atual: R$ {salario1:.2f}')
    print('Percentual de aumento: 15%')
    print(f'Valor do aumento: R$ {salario1 * 0.15}')
    print(f'Novo salário: R$ {salario:.2f}')
    print(f"\n{'=':=^50}")
elif salario > 700 and salario <= 1500:
    salario += salario * 0.1
    print(f"{'_':_^50}\n")
    print(f'Salário atual: R$ {salario1:.2f}')
    print('Percentual de aumento: 10%')
    print(f'Valor do aumento: R$ {salario1 * 0.1}')
    print(f'Novo salário: R$ {salario:.2f}')
    print(f"\n{'=':=^50}")
else: 
    salario += salario * 0.05
    print(f"{'_':_^50}\n")
    print(f'Salário atual: R$ {salario1:.2f}')
    print('Percentual de aumento: 5%')
    print(f'Valor do aumento: R$ {salario1 * 0.05}')
    print(f'Novo salário: R$ {salario:.2f}')
    print(f"\n{'=':=^50}")

