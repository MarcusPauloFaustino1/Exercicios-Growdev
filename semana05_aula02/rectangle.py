class Rectangle:
    
    def __init__(self, base, height):
        self.base = base
        self.height = height
        
    def change_sides(self, base, height):
        self.base = base
        self.height = height
        
    def sides(self):
        return self.base, self.height
        
    def area(self):
        return self.base * self.height
        
    def perimeter(self):
        return 2 * self.base + 2 *  self.height
        
        
        