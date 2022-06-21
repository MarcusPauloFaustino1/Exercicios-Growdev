'''6) Faça um programa completo utilizando classes e métodos que:
a) Possua uma classe chamada BombaCombustivel, com no
mínimo esses atributos:
i) tipo_combustivel.
ii) valor_litro
iii) quantidade_combustivel
b) Possua no mínimo esses métodos:

i) abastecer_por_valor() – método onde é informado o
valor a ser abastecido e mostra a quantidade de litros
que foi colocada no veículo
ii) abastecer_por_litro() – método onde é informado a
quantidade em litros de combustível e mostra o valor a
ser pago pelo cliente.
iii) alterar_valor() – altera o valor do litro do
combustível.
iv) alterar_combustivel() – altera o tipo do combustível.
v) alterar_quantidade_combustivel() – altera a
quantidade de combustível restante na bomba.

OBS: Sempre que acontecer um abastecimento é necessário
atualizar a quantidade de combustível total na bomba.'''

class FuelPump:
    def __init__(self, fuel_type, price_liter, quantity):
        self.fuel_type = fuel_type
        self.price_liter = price_liter
        self.quantity = quantity
        
    def to_fuel_per_price(self, price):
        liters = price / self.price_liter
        print(f'Você abasteceu {liters:.2f} litros, em um total de R$ {price:,.2f}')
        self.change_quantity(liters)
        
    def to_fuel_per_liter(self, liters):
        price = liters * self.price_liter
        print(f'Você abasteceu {liters:.2f} litros, em um total de R$ {price:,.2f}')
        self.change_quantity(liters)
        
    def change_price(self, price_liter):
        self.price_liter = price_liter
        
    def change_fueltype(self, fuel_type):
        self.fuel_type = fuel_type
        
    def change_quantity(self, liters):
        if liters <= self.quantity:
            self.quantity -= liters
        else:
           print('Quantidade de litros insuficiente')     