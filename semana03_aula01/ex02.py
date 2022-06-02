'''Escrever um programa que lê um valor N inteiro e positivo e que calcula seu
valor fatorial. Ex: 5! = 5 * 4 * 3 * 2 * 1'''



from time import sleep


print(f"\n{'CALCULANDO FATORIAIS':=^40}\n")


n = int(input('Digite um valor inteiro e positivo: '))

fatorial = 1



for num in range(n,0,-1):
    fatorial *= num
    


print('\nRESULTADO:')
sleep(2)

print(f"{'_'*40}\n")

print(f'{n}! = {fatorial}\n')

print(f'{"="*40}\n')

   

