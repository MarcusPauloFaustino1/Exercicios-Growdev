'''Escreva uma função que conte o número de espaços em branco em uma
frase passada como parâmetro.'''

frase = input('Digite uma frase: ')

espacos = 0

def spaces(frase):
    espacos = 0
    for i in range(len(frase)):
        if frase[i] in " ":
            espacos = espacos + 1
    return f'Número de espaços em branco na frase: {espacos}'

print(spaces(frase))
            
    
    

    
