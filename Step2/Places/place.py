class Place:
    def __init__(self, **kwargs):
        self.neighbour_map={}
    
    def add_neighbour(self, direction, neighbour):
        self.neighbour_map[direction] = neighbour
        
    def get_neighbour(self, direction):
        return self.neighbour_map[direction]