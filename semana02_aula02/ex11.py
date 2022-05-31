'''Crie um algoritmo para um jogo de adivinhação, onde o usuário tenta
adivinhar um número aleatório gerado pelo computador. Esse número
aleatório é inteiro e não negativo, e deve ser escolhido dentro de uma faixa
estabelecida pelo usuário (por exemplo, o usuário pode estipular que esse
número varie entre 0 e 10 ou entre 22 e 48, por exemplo). Após o usuário
tentar adivinhar qual foi o número gerado, o algoritmo deve escrever esse
número e dizer se indicar se o palpite do jogador estava correto, muito alto ou
muito baixo.
Dica: Para gerar um número aleatório utilize a função randint do módulo
random.'''

from random import randint
from time import sleep

print(f"\n{'JOGO DA ADIVINHAÇÃO':=^90}\n")

print("\nVamos tentar adivinhar qual número o computador vai escolher?")
print("\nVocê precisa dizer em qual faixa de valor o número varia. ")
print("\nPor exemplo: diga se este número varia entre 1 e 42 ou entre 22 e 69.")
print("\nDetalhe... Essa faixa de valor deve ser de numeros inteiros e não negativos.")
print("\nVamos lá!")

lim1 = int(input("\nO número escolhido pelo computador está entre:"))
lim2 = int(input("e:"))

chute = int(input("\nAgora adivinhe qual número o computador escolheu:"))

print("\nSerá que você acertou?...")
sleep(3)

nRandom = randint(lim1, lim2)

print(f"\n{'_':_^90}\n")

print("O comptador escolheu o número:\n")
print(nRandom)
if chute == nRandom:
    print('\nParabéns! Você acertou na mosca!!!')
elif chute > nRandom:
    print('\nNão foi dessa vez! Você chutou um valor muito alto.')
elif chute < nRandom:
    print('\nNão foi dessa vez! Você chutou um valor muito baixo.')

print(f"\n{'=':=^90}\n")