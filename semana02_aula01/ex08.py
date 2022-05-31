'''Crie um algoritmo para uma empresa de transportes que, a partir do peso de
uma encomenda fornecida pelo usuário, calcule o preço da remessa
conforme a seguinte tabela:
PESO                                        VALOR
500g ou menos                                R$ 1,10
Mais de 500g, menos ou igual a 2kg           R$ 2,20
Mais de 2kg, menos ou igual a 10             R$ 3,70
Mais de 10kg                                 R$ 5,00 mais R$ 3,80/kg pelo peso que ultrapassar 10 Kg'''

pE = float(input("Digite o peso da encomenda, em kilogramas(kg):"))

pExtra = pE - 10

fExtra = pExtra * 3.8 + 5

if pE <= 0.500001:
    print("Valor do frete:    R$ 1,10")
elif pE > 0.500001 and pE <= 2.00001:
    print("Valor do frete:    R$ 2,20")
elif pE > 2.00001 and pE <=  10.00001:
    print("Valor do frete:    R$ 3,70")
else:
    print(f"Valor do frete:    R$ {fExtra:.2f}")
    