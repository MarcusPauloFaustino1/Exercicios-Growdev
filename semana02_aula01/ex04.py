'''O programa de fidelidade de uma determinada livraria premia seus clientes
de acordo com o número de livros comprados a cada mês. Os pontos são
atribuídos da seguinte forma:
a) Se um cliente comprar 0 livros, ele ganhará 0 pontos.
b) Se um cliente comprar um livro, ele ganhará 5 pontos.
c) Se um cliente comprar dois livros, ele ganhará 15 pontos.
d) Se um cliente comprar 3 livros, ele ganhará 30 pontos.
e) Se um cliente comprar 4 ou mais livros, ele ganhará 60 pontos.
Crie um algoritmo que leia o número de livros comprados por um cliente e
exiba o número de pontos correspondentes.''' 

nL = int(input("Digite quantos livros você comprou neste mês: "))

if nL == 0:
    print("Pontos recebidos:   0 ")
elif nL == 1:
    print("Pontos recebidos:   5 ")
elif nL == 2:
    print("Pontos recebidos:   15 ")
elif nL == 3:
    print("Pontos recebidos:   30 ")
elif nL >= 4:
    print("Pontos recebidos:   60 ")
    