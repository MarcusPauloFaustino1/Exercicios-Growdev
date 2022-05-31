'''Escreva um algoritmo que receba um número e escreva “Par” caso esse
número seja par e escreva “Impar” caso esse número seja impar.'''

n = int(input("Digie um número inteiro:"))

if n % 2 == 0:
    print("\nO número digitado é PAR.")
    if n == 0:
        print("\nHá controvérsias sobre a classificação do 0 como número par...\nHá que diga que é um número neutro.\nPorém os matemáticos especialistas o consideram como número PAR.")
else:
    print("O número digitado é ÍMPAR.")
    
    
