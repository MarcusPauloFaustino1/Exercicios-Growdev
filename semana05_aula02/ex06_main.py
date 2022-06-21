from fuel_pump import FuelPump

fuelpump = FuelPump('gasolina', 7.4, 500)

fuelpump.to_fuel_per_liter(5)

print(fuelpump.quantity)

fuelpump.to_fuel_per_price(50)

print(f'{fuelpump.quantity:.1f}')

fuelpump.to_fuel_per_liter(500)