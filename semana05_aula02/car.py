'''7) Implemente uma classe chamada Carro com as seguintes
propriedades:
a) Um veículo tem um certo consumo de combustível (medidos
em km / litro) e uma certa quantidade de combustível no
tanque.
b) O consumo é especificado no construtor e o nível de
combustível inicial é 0.
c) Forneça um método andar() que simula o ato de dirigir o
veículo por uma certa distância, reduzindo o nível de
combustível no tanque de gasolina.

d) Forneça um método obter_gasolina(), que retorna o nível
atual de combustível e forneça um método
adicionar_gasolina(), para abastecer o tanque.
Exemplo:
meu_fusca = Carro(15)
meuFusca.adicionar_gasolina(20)
meuFusca.andar(100)
meuFusca.obter_gasolina()'''


from xml.sax.handler import feature_validation


class Car:
    
    def __init__(self, consumption):
        self.consumption = consumption
        self.fuel_in_tank = 0
        
    def drive(self, distance):
        max_distance = self.consumption * self.fuel_in_tank
        tank = max_distance - distance 
        if tank < 0:
            while tank <= 0 and distance >= 0:
                max_distance = self.consumption * self.fuel_in_tank
                tank = max_distance - distance 
                print(f'Você dirigiu por {max_distance:,.1f}, porém infelizmente seu combustível acabou!')
                self.fuel_in_tank = 0
                distance = distance - max_distance
                fill_tank = input('Deseja abastecer?[s / n]: ')
                if fill_tank in 's':
                    liters_add = int(input('Quantos litros?: '))
                    self.fuel_in_tank = int(liters_add)
                elif fill_tank in 'n':
                    print('Péssima escolha!')
                    self.fuel_in_tank = 0
                if tank == 0:
                    print('\nSeu combustível acabou... Mas você chegou ao seu destino!')
                elif tank >= 0:
                    self.fuel_in_tank -= distance / self.consumption
        
        elif self.fuel_in_tank == 0:
            print('\nSeu combustível acabou... Mas você chegou ao seu destino!')
            
        elif self.fuel_in_tank >= 0:
            self.fuel_in_tank -= distance / self.consumption
            
        
                
            
    def show_fuel(self):
        return self.fuel_in_tank
    
    def add_gas(self, liters):
        self.fuel_in_tank += liters
        
        