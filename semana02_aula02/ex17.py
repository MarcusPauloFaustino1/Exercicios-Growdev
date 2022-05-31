'''Faça um programa que pergunte ao usuário se ele quer passar uma
temperatura de Fahrenheit para Celsius ou de Celsius para Fahrenheit, e
que, a partir da resposta do usuário, faça a devida conversão.'''

print(f"\n{'CONVERTENDO TEMPERATURAS':=^50}")

escala = input('\nPara converter: \n\nCelsius(°C) para Fahrenheit(°F) -> Digite "cf" \n\nou\n\nFahrenheit(°F) para Celsius(°C) -> Difite "fc"\n\nDigite aqui:')

temperatura = float(input('\nDigite a temperatura que deseja converter:'))

print(f"\n{'_':_^50}")

if escala in ["cf"]:
    temperatura2 = (9 / 5) * temperatura + 32
    print(f"\nResultado: {temperatura}°C = {temperatura2:.1f}°F")
elif escala in ["fc"]:
    temperatura2 = (temperatura - 32) / (9 / 5)
    print(f"\nResultado: {temperatura}°F = {temperatura2:.1f}°C")
print(f"\n{'=':=^50}")


