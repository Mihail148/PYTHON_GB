class Rectangle:
    
    def __init__(self, length, width = None):
        self.length = length
        self.width = width if width else length
        
    def len(self):
        return (self.width + self.length) * 2
    
    def area(self):
        return self.width * self.length
    
d = Rectangle(4)
print(d.len())
print(d.area())        