'''Supondo que a população de um país A seja da ordem de 80000 habitantes
com uma taxa anual de crescimento de 3% e que a população de B seja
200000 habitantes com uma taxa de crescimento de 1.5%. Faça um
programa que calcule e escreva o número de anos necessários para que a
população do país A ultrapasse ou iguale a população do país B, mantidas as
taxas de crescimento.'''

print(f'\n{" PAIS A e PAÍS B ":=^60}\n')

print(f'País A: 80.000 habitantes\nCrescimento: 3%\n\nPaís B: 200.000\nCrescimento: 1.5%')

paisA = 80000

paisB = 200000

anos = 0

while paisB > paisA:
    paisA += paisA*0.03
    paisB += paisB* 0.015
    anos += 1

print(f'\n{"─"*60}\n')
print(f'O país A ultrapassará o país B em {anos} anos')
print(f'\n{"="*60}\n')