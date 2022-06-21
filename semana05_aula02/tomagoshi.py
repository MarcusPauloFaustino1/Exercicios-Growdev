'''4) Crie uma classe que modele um Tamagochi (Bichinho Eletrônico):
a) Atributos
i) Nome
ii) Fome
iii) Saúde
iv) Idade.
b) Métodos
i) alterar_nome,
ii) alterar_fome
iii) alterar_saude
iv) alterar_idade
v) retornar_nome
vi) retornar_nome
vii) retornar_saude

viii) retornar_idade'''

class Tomagoshi:
    
    def __init__(self):
        self.name = None
        self.hungry = None
        self.health = None
        self.age = None
        
    def name_change(self, name):
        self.name = name
    
    def hungry_change(self, hungry):
        self.hungry = hungry
        
    def health_change(self, health):
        self.health = health
        
    def age_change(self, age):
        self.age = age
        
    def show_name(self):
        return self.name
        
    def show_hungry(self):
        return self.hungry
        
    def show_health(self):
        return self.health
        
    def show_age(self):
        return self.age
        
    def show_info(self):
        print(f'\n\nNome: {self.name}\nFome: {self.hungry}\nSaúde: {self.health}\nIdade: {self.age}\n\n')
        
        
    