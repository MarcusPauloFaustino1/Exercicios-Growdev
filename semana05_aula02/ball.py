class Ball: #difinindo classe
    
    #construtor
    
    def __init__(self, color, circunference, material): #passando atributos da classe como parâmetross
        
        #atributos
        
        self.color = color
        self.circunference = circunference
        self.material = material
    
        #métodos    
    
    def change_color(self, color):
        self.color = color
        
    def show_color(self):
        print(self.color)