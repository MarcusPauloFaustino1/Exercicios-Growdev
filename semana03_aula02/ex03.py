'''Modifique o programa anterior para que utilize apenas uma lista e em cada
posição da lista armazene um dicionário com o nome e a média.'''


lista = []



for i in range (5):
    nome = input('Digite o nome: ')
    n1 = float(input('Digite a nota 1: '))
    n2 = float(input('Digite a nota 2: '))
    media = (n1 + n2) / 2
    dic = {'Nome': nome, 'Média': media}
    lista.append(dic)
    
#print("\nAPROVADO(S):\n")    
for i in range (len(lista)):
    d = lista[i]
    cont = 1
    for a, b in d.items():
        x = d.get('Média')
        if x > 7:
            print(a + ": " + str(b) + "  ─>  ", end=" ") 
            if cont % 2 == 0:
                print("     APROVADO(A)\n")
        cont += 1
