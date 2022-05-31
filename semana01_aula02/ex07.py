ano = int(input("Quantos anos você tem?"))

mes = int(input("Quantos meses já se passaram desde seu aniversário?"))

dia = int(input("Quantos dias sobraram além desses meses?"))

ano_dia = ano*365

mes_dia = mes*31

diasTotais = ano_dia + mes_dia + dia

print(f"\nVocê já viveu {diasTotais} dias!")