'''Escreva um programa que receba o nome de 10 pessoas e para cada
pessoa, o lugar para o qual ela já viajou. Sendo que existem 3 possibilidades:
a) Rio de Janeiro
b) Bahia
c) Minas Gerais
Após, informar qual foi o destino mais visitado e qual o menos visitado.'''

lista = []
lista2 = []

print(f'\n{"ESTADOS VISITADOS":=^90}\n')

print(f'\nInforme quais desses locais voram visitados: \n+ {"─"*47} +\n| - Bahia:                            (digite 1)  |\n|{" "*49}|')
print(f'| - Rio de Janeiro:                   (digite 2)  |')
print(f'|{" "*49}|\n| - Minas Gerais:                     (digite 3)  |')
print(f'|{" "*49}|\n| - Bahia e Rio de janeiro:           (digite 12) |\n|{" "*49}|\n| - Bahia e Minas Gerais:             (digite 13) |')
print(f'|{" "*49}|\n| - Rio de Janeiro e Minas Gerais:    (digite 23) |')
print(f'|{" "*49}|\n| - Se visitou todos os locais:       (digite 123)|')
print(f'|{" "*49}|\n| - Se não visitou nenhum local:      (digite 0)  |')
print(f'+ {"─"*47} +')

for i in range(3):
    nome = input('\n\nInforme o nome: ')
    cidade = int(input('\n\nInforme aqui o número correspondente às cidades visitadas: '))
             
    if cidade > 9 and cidade < 99:
        cidade1 = cidade// 10
        cidade2 = cidade % 10
        lista.append(cidade1)
        lista.append(cidade2)

    elif cidade > 99:
        cidade1 = cidade // 100
        cidade2 = (cidade % 100)//10
        cidade3 = (cidade % 100)%10
        lista.append(cidade1)
        lista.append(cidade2)
        lista.append(cidade3)
    elif cidade == 0:
        pass 
    else:
        lista.append(cidade)

print(f'\n{"─"*90}\n')

if sum(lista) == 0:
    print(f'{" NENHUM estado foi visitado ":*^45}\n')
    print(f'\n{"="*90}\n')
    exit()

bahia = lista.count(1)
rio = lista.count(2)
minas = lista.count(3)


if rio == minas and rio == bahia:
    mais = 'IGUALMENTE VISITADOS'
elif rio == minas and rio > bahia:
    mais = 'RIO DE JANEIRO e MINAS GERAIS'
    menos = 'BAHIA'
elif rio == minas and rio < bahia:
    mais = 'BAHIA' 
    menos = 'RIO DE JANEIRO e MINAS GERAIS'
elif rio == bahia and rio > minas:
    mais = 'RIO DE JANEIRO e BAHIA'
    menos = 'MINAS GERAIS'
elif rio == bahia and rio < minas:
    mais = 'MINAS GERAIS' 
    menos = 'RIO DE JANEIRO e BAHIA'
elif minas == bahia and minas > rio:
    mais = 'MINAS GERAIS e BAHIA'
    menos = 'RIO DE JANEIRO'
elif minas == bahia and minas < rio:
    mais = 'RIO DE JANEIRO' 
    menos = 'MINAS GERAIS e BAHIA'
else:    
    lista2.append(bahia)
    lista2.append(rio)
    lista2.append(minas)

    mais = max(lista2)
    menos = min(lista2)

    if mais == bahia:
        mais = 'BAHIA' 
    elif mais == rio:
        mais = 'RIO DE JANEIRO'
    elif mais == minas:
        mais = 'MINAS GERAIS'
    if menos == bahia:
        menos = 'BAHIA' 
    elif menos == rio:
        menos = 'RIO DE JANEIRO'
    elif menos == minas:
        menos = 'MINAS GERAIS'

print(f'\n{"─"*90}\n')

print(f'Bahia: {bahia} visitas')
print(f'Rio de Janeiro: {rio} visitas')
print(f'Minas Gerais: {minas} visitas')

print(f'\n{"─"*90}\n')

print(f'O estado mais visitado é {mais} ')
try:
    print(f'O estado menos visitado é: {menos} ')
except NameError:
    print(f'\n{"="*90}\n')
    exit()
print(f'\n{"="*90}\n')