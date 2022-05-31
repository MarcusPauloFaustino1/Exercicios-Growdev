'''Construa um algoritmo que, a partir do valor do comprimento dos três lados
de um triângulo, classifique-o em equilátero, isósceles ou escaleno. Lembre,
um triângulo é equilátero quando o comprimento de todos os seus lados for
igual, é isósceles quando apenas um dos lados tiver comprimento diferente e
é escaleno quando todos os lados tiverem comprimentos diferentes dos
demais lados.'''


from time import sleep


print(f"\n{'CLASSIFICANDO TRIÂNGULOS':=^50}")

print('\nDigite os lados do triângulo')

l1 = float(input('Lado 1: '))

l2 = float(input('Lado 2: '))

l3 = float(input('Lado 3: '))

print('Considerando os lados, seu triângulo é...')
sleep(2)

if l1 == l2 == l3:
    print(f"\n{'EQUILÁTERO':*^30}\n")
elif l1 == l2 != l3 or l1 == l3 != l2 or l2 == l3 != l1:
    print(f"\n{'ISÓSCELES':*^30}\n")
else:
    print(f"\n{'ESCALENO':*^30}\n")

print(f"\n{'=':=^50}")