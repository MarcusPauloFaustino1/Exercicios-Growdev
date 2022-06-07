'''A série de Fibonacci é formada pela sequência 1,1,2,3,5,8,13,21,34,55,...
Faça um programa capaz de gerar a série até o n−ésimo termo.'''


print(f'{" SEQUÊNCIA FIBONACCI ":=^60}\n') 

n = int(input('Digite o número de termos da sequência: '))

lista = []


num = 1
numAnt = 0
aux = numAnt
lista.append(num)

for i in range(0, n):
    aux = num
    num += numAnt
    lista.append(num)
    numAnt = aux
    
print(f'\n{"─"*60}\n')      
print(f'\nOs {n} termos da Sequência Fibonacci são:\n\n{lista}\n')
print(f'{"="*60}\n')    