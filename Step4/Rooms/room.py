class Wall:
    def __init__(self, color, description):
        self.color = color
        self.description= description

class Door:
    pass

class Window:
    pass

class Room:
    def __init__(self, **kwargs):
        self.decorate()
        self.builder()
    
    def decorate(self):
        pass
    def builder(self):
        self.south = None  
        self.north = None
        self.east  = None 
        self.west  = None 
    