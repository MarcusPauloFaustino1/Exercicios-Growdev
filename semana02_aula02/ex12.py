'''Uma certa operadora de telefonia móvel cobra R$ 5,00 mensais pelo seu
plano básico de transmissão de SMS (mensagens de texto), sendo que taxas
adicionais são cobradas conforme as regras abaixo:
a) As primeiras 60 mensagens estão incluídas no plano básico;

b) b. Se o usuário mandar mais de 60 mensagens, cada mensagem
adicional custará R$ 0.05, até o limite de 180 mensagens.
c) c. Acima de 180 mensagens, o valor de cada uma delas passa a R$
0,10;
d) d. A soma dos impostos estaduais e federais amonta a 12% do valor
de cada fatura.
Com base nessas informações, crie um algoritmo para ler o número total de
mensagens enviadas por um usuário. Ao final, calcule o valor da conta e
mostre todos os dados, incluindo o valor da conta com e sem impostos.'''

print(f"\n{'FATURA SMS':=^90}\n")

sms = int(input("Digite o número de SMS enviados: "))
mensalidade = 5
acim60 = mensalidade + 0.05 * (sms - 60)
acim180 = mensalidade + (0.05 * 120) + (0.1 * (sms - 180))

if sms <= 60:
    valorTotal = mensalidade
elif sms > 60 and sms < 180:
    valorTotal = acim60
elif sms > 180:
    valorTotal = acim180

imposto = valorTotal * 0.12

valorFatura = valorTotal + imposto

print(f"\n{'_':_^90}\n")

print("Plano:                                                               60 SMS")
print(f"\nNúmero de SMS enviados:                                              {sms} ")
print("\nMensalidade:                                                         R$ 5.00")

if sms <= 60:
    print(" ")
elif sms > 60 and sms < 180:
    print(f"\nCusto por SMS acima do plano (até 180: R$ 0.05/SMS):                 R$ {acim60:.2f}\n")
elif sms > 180:
    print("\nCusto por SMS acima do plano (até 180 SMS: R$ 0.05/SMS):             R$ 6.00")
    print(f"\nCusto por SMS acima do plano (acima de 180 SMS: R$ 0.10/SMS):        R$ {(0.1 * (sms - 180)):.2f}")
    print("\nCusto por SMS acima do plano (até 180: R$ 0.05/SMS):                 R$ 0.05\n")
print(f"Impostos:                                                            R$ {imposto:.2f}")
print(f"\n{'_':_^90}\n")
print(f"O valor da sua fatura é de:                                          R$ {valorFatura:.2f}")
print(f"\n{'=':=^90}\n")

