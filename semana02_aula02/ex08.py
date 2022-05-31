'''Um carpinteiro esculpe placas personalizadas para estabelecimentos
comerciais e deseja um programa que faça orçamentos das placas que
produz, considerando as seguintes informações:
a) O valor mínimo de qualquer placa é de R$ 300,00;
b) Placas de angelim custam R$ 150,00 adicionais, mas placas de pinus
não possuem nenhum custo extra;
c) Frases com até 12 caracteres estão incluídas no valor mínimo; para
frases maiores, são cobrados R$ 15,00 por caractere;

d) Para placas com dizeres brancos ou pretos não se cobra adicional,
mas se ele contiver letras douradas, cobra-se R$ 60,00 a mais.
Baseado nessas informações, construa um algoritmo que leia o número de
um orçamento, o nome do cliente, tipo de madeira (angelim ou pinus),
número de caracteres da mensagem e a cor dos caracteres (branco, preto ou
dourado). Ao final, imprima todos os dados de entrada e o preço da placa
orçada.'''

print(f"\n{'ORÇAMENTO DE PLACAS':=^70}\n")

#DADOS DE ENTRADA

nome = input("Digite seu nome:")

print(f"\n{'_':_^50}\n")

quantidade = int(input("\nDigite o número de placas desejadas:"))

print(f"\n{'_':_^50}\n")

madeira = int(input('\nEscolha um tipo de madeira:\n\na) Para escolher ANGELIM digite "1" \n\nb) Para escolher PINUS digite "2" \n\nDigite o tipo de madeira escolhido:'))
if madeira < 1 and madeira > 2:
    print("Opção inválida")
    int(input('\nEscolha um tipo de madeira:\n\na) Para escolher ANGELIM digite "1" \n\nb) Para escolher PINUS digite "2" \n\nDigite o tipo de madeira escolhido:'))

print(f"\n{'_':_^50}\n")

caracteres = input("\nDigite a frase que deseja gravar:")

print(f"\n{'_':_^50}\n")

numCaracteres = len([ele for ele in caracteres])
numEspacos = len([ele for ele in caracteres if ele.isspace()])
numLetras = numCaracteres - numEspacos

cor = int(input('\nEscolha a cor das letras:\n\na) Para escolher BRANCO digite "1" \n\nb) Para escolher PRETO digite "2" \n\nc) Para escolher DOURADO digite "3"\n\nDigite a cor escolhida:'))
if cor < 1 and cor > 2:
    print("Opção inválida")
    cor = int(input('\nEscolha a cor das letras:\n\na) Para escolher BRANCO digite "1" \n\nb) Para escolher PRETO digite "2" \n\nc) Para escolher DOURADO digite "3"\n\nDigite a cor escolhida:'))


#VALORES

minimo = 300 
caracteresExtras = (numLetras - 12) * 15


if madeira == 1 and cor == 3 and numLetras > 12:
    minimo += 150 + 60 + caracteresExtras
elif madeira == 1 and cor == 3:
    minimo += 150 + 60
elif madeira == 1 and numLetras > 12:
    minimo += 150 + caracteresExtras
elif cor == 3 and numLetras > 12:
    minimo += 60 + caracteres
elif madeira == 1 and cor!= 3 and numLetras <= 12:
    minimo += 150
elif cor == 3 and madeira!= 1 and numLetras <= 12:
    minimo += 60
elif numLetras > 12 and madeira != 1 and cor != 3:
    minimo += caracteresExtras
else:
    minimo = 300

final = minimo * quantidade

#DADOS DE SAÍDA

print(f"\n{'DADOS':_^50}\n")

print(f"Nome: {nome}\n\nQantidade de placas: {quantidade}")

if madeira == 1:
    print("\nTipo de madeira: Angelim")
else:
    print("\nTipo de Madeira: Pinus")

print(f"\nMensagem: {caracteres}\n\nNúmero de caracteres da mensagem: {numLetras}")

if cor == 1:
    print("\nCor das letras: Branco")
elif cor == 2:
    print("\nCor das letras: Preto")
else:
    print("\nCor das letras: Dourado")

print(f"\n{'_':_^50}\n")

print(f"Valor total: R$ {final}")

print(f"\n{'=':=^50}\n")

