from audioop import add
from car import Car

car = Car(13)

car.add_gas(67)

#print(car.show_fuel())

car.drive(900)

print(f'{car.show_fuel():.2f}')

