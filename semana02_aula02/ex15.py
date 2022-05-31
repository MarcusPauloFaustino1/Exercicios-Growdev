'''Construa um algoritmo que, a partir de duas cores primárias fornecidas pelo
usuário, determine qual cor seria obtida pela mistura delas. As cores
vermelho, azul e amarelo são chamadas de cores primárias porque não
podem ser obtidas a partir de outras cores e, quando misturadas, resultam
numa cor secundária, de acordo com as seguintes regras:
a) vermelho + azul = roxo;
b) vermelho + amarelo = laranja;
c) azul + amarelo = verde.
Se o usuário inserir algo diferente de “vermelho”, “azul” ou “amarelo”, o
programa deverá exibir uma mensagem de erro. Caso contrário, o programa
deve exibir o nome da cor secundária resultante.'''

from time import sleep

print(f"\n{'MISTURANDO AS CORES':=^70}")
print('\nVocê sabia que todas as cores derivam das cores primárias?')
print('Misture-as e adquira cores novas!')
print(f"\n{'_':_^70}")
print('As cores primárias são:')
print('\n-> Azul\n-> Amarelo\n-> Vermelho ')
print('\n Vamos misturá-las?')
print(f"\n{'_':_^70}\n")
#DADOS DE ENTRADA 

cor1 = input('Em letras minúsculas, digite uma cor primária:')
cor2 = input('Em letras minúsculas, digite outra cor primária:')

if cor1 in ["azul", "amarelo", "vermelho"] and cor2 in ("azul", "amarelo", "vermelho"):
    print('\n\nMisturando...\n\n')
    sleep(2)
else:
    print('ERRO - Cor inválida!')
    cor1 = input('Em letras minúsculas, digite uma cor primária:')
    cor2 = input('Em letras minúsculas, digite outra cor primária:')
    if cor1 in ["azul", "amarelo", "vermelho"] and cor2 in ("azul", "amarelo", "vermelho"):
        print('\n\nMisturando...\n\n')
        sleep(2)
    else:
        print('ERRO - Cor inválida!')
        print('Encerrando o programa...')
        sleep(2)
        print('Programa encerrado. Tente novamente com CORES VÁLIDAS!')
        exit()

#DADOS DE SAÍDA

if cor1 + cor2 in ["azulvermelho"] or cor1 + cor2 in ["vermelhoazul"]:
    print(f'A mistura do {cor1} com o {cor2} resulta no: {"ROXO":*^20}\n\n')
elif cor1 + cor2 in ["amarelovermelho"] or cor1 + cor2 in ["vermelhoamarelo"]:
    print(f'A mistura do {cor1} com o {cor2} resulta no: {"LARANJA":*^20}\n\n')
elif cor1 + cor2 in ["amareloazul"] or cor1 + cor2 in ["azulamarelo"]:
    print(f'A mistura do {cor1} com o {cor2} resulta no: {"VERDE":*^20}\n')
elif cor1 + cor2 in ["amareloamarelo"]:
    print(f'A mistura do {cor1} com o {cor2} resulta no: {"AMARELO":*^20}\n')
elif cor1 + cor2 in ["azulazul"]:
    print(f'A mistura do {cor1} com o {cor2} resulta no: {"AZUL":*^20}\n')
elif cor1 + cor2 in ["vermelhovermelho"]:
    print(f'A mistura do {cor1} com o {cor2} resulta no: {"VERMELHO":*^20}\n')   

print(f"\n{'=':=^70}")