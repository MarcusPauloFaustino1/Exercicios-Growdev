'''Quadrado mágico. Um quadrado mágico é aquele dividido em linhas e
colunas, com um número em cada posição e no qual a soma das linhas,
colunas e diagonais é a mesma. Por exemplo, veja um quadrado mágico de
lado 3, com números de 1 a 9:
8 3 4
1 5 9
6 7 2
Elabore uma função que identifica e mostra na tela todos os quadrados
mágicos com as características acima. Dica: produza todas as combinações
possíveis e verifique a soma quando completar cada quadrado.'''

l_1 = [8,3,4]
l_2 = [1,5,9]
l_3 = [6,7,2]
l_a = [2,9,4]
l_b = [7,5,3]
l_c = [6,1,8]

a = b = c = d = e = f = g = h = 0

def magic_squares():
    a = [l_1,l_2,l_3]
    b = a[::-1]
    c = [l_1[::-1],l_2[::-1],l_3[::-1]]
    d = [l_3[::-1],l_2[::-1],l_1[::-1]]
    e = [l_a,l_b,l_c]
    f = e[::-1]
    g = [l_a[::-1],l_b[::-1],l_c[::-1]]
    h = [l_c[::-1], l_b[::-1], l_a[::-1]]
    
    return '{}\n{}\n{}\n{}\n{}\n{}\n{}\n{}'.format(a,b,c,d,e,f,g,h)

print(magic_squares())
