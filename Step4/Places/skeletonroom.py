class SkeletonRoom:
    def __init__(self):
        self.decorate()
        self.builder()
    
    def decorate(self):
        pass
    def builder(self):
        self.south = None  
        self.north = None
        self.east  = None 
        self.west  = None 
