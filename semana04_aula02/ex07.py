'''Faça uma função que recebe por parâmetro o tempo de duração da produção
de uma peça em uma fábrica expressa em segundos e exibe esse tempo em
horas, minutos e segundos.'''

tempo = int(input('Digite o tempo de duração da produção da peça (em segundos): '))

def t(tempo):
    if tempo >= 3600:
        h = tempo // 3600
        tempo = tempo - (h * 3600)
        m = tempo // 60
        s = tempo % 60     
    elif tempo < 3600 and tempo > 59:
        h = 0
        m = tempo // 60
        s = tempo % 60
    else:
        h = 0
        m = 0
        s = tempo
        
    return f'horas: {h}\nminutos: {m}\nsegundos: {s}'

a = t(tempo)

print(a)